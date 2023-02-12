# Deep learning based approaches for WGS 
### Deep-learning prediction on noncoding variants from WGS data

## WGS (Whole Genome Sequencing)
- 가장 원시적인 형태의 분석. **Genome의 모든 genetic variant를 찾는 것.** SNV부터 큰 규모의 염기서열 변화인 SV까지. 특정 형질 / 질환과의 연관성을 평가하거나, noncoding 지역에 나타나는 rare variant를 찾음.
- 특정 질환을 설명하는 pathogenic noncoding mutation를 찾을 때, fully penetrant하지는 않을 수 있음. 한두개의 변이가 질환 전체를 설명하지 못하고 어느정도씩 기여하는 것일 수 있음. 
- *Noncoding genome이 왜 중요한가?* 유전자 발현을 조절하는 조절자 -> 보통 유전자 밖에 존재하며 transcription을 일으키는 promoter 지역 혹은 멀리 떨어져서 전사조절 인자를 안정적으로 조절하는 enhancer 지역. 혹은 methyl group, insulator, CTCF binding factor 등이 발현을 조절한다.
	- 즉, **유전자의 1차적 지역 외에도 여러 전사조절, 형질 발현에 기여하는 요인이 있다.**
- WGS 전에는 주로 WES (단백질 만드는 지역) 의 mutation을 평가했음. Exome sequencing이 처음 나왔을 때, 평가 기준은 **mutation이 발생하는 단백질 위치가 얼마나 생물종에 걸쳐서 진화적으로 보존되어 있는가 (conserved)** 를 평가하였음 -> 단백질의 중요성을 평가하는 것.
	- 평가하는 알고리즘 : Nucleotide conservation (GERP, PhyloP, PhastCons) or Protein sequence conservation (SIFT, PolyPhen2) -> score가 높으면 deleterious / highly conserved.
- 이러한 시스템을 통합해서 평가하는 알고리즘을 제작 : **Ensemble methods** 중에서도 **CADD** algorithm. 여러 individual predictor의 결과를 통합해서 performance를 향상시킴.
- 그러나 이러한 알고리즘은 "Noncoding mutation"에 대해서는 predictive power가 낮다. 
	- Why? 두 가지 가설 - 1. noncoding mutation은 원래부터 질병에 미치는 영향이 적다, 2. CADD는 noncoding mutation을 정확하게 selection할 수 있는 알고리즘이 아니다. 
	- 그러면 어떻게 개선할 수 있는가? **딥러닝 방식을 활용**

## Deep Learning Approach
- 특정 현상에 나타나는 패턴, feature들을 학습해서 실제적으로 그 현상을 예측할 수 있는 기술. 즉, regulatory element가 나타나는 noncoding 지역 중 실제로 functional하다고 예측되는 지역들 (ex. TF binding site) 의 pattern / feature를 학습해서 실제 regulatory element의 구성을 살펴볼 수 있는 접근법. Genome-wide evaluation이 가능해진다. 
- Approaches : DeepSEA, Basenji2, **Enformer, Sei, Orca**
- 딥러닝이 왜 필요한가? 특정 발달 시점 / cell type / condition 상에서 나타나는 Regulatory element (enhancer, promoter) 를 측정할 때 Chip-Seq이나, ATAC-Seq을 사용해서 open chromatin 지역을 추출할 수 있음. 여기서 peak이 잡히지 않은 region에 대해서 deep learning method로 보완이 가능. motif 조합을 학습해서 예측할 수도 있고...
- TF -> domain-motif간 결합을 바탕으로 붙는다. motif 학습의 결과를 바탕으로 random sequence를 주었을 때 TF가 어디에 붙을지를 예측할 수 있음.

###  Enformer (2021)
- 200kb정도의 input sequence를 주었을 때, 이 염기서열을 바탕으로 특정 cell type/ tissue (?) 등을 예측.
- VCF 형식으로 mutation을 주면 FASTQ로부터 200kb 정도의 주위 서열을 input으로 하여 예측함.
- 질문. 여기서 score 예측이 곧 conservation score인가...? eQTL ? Conservation Score?
- 특정 mutation에 대한 예측값을 얻게 되면 실제로 mutation이 발생했을 때 얼만큼의 효과를 주게 되는지도 측정 가능. 

### Sei (2022)
- Updated model of DeepSEA. Enformer가 제공하는 정보에 더불어, 상위 개념 추출도 가능 (?)
- 40개 정도의 각기다른 regulatory element -> 특정 지역이 갖고 있는 regulatory 특성을 제공...
- Pattern이 어떻게 학습되나 - convolutional network를 사용, attention layer 대신 dual linear layer를 사용해서 모델을 구축... 여러 가지 iteration을 거치면서 가장 optimized performance를 보이는 모델을 최종 평가하여 제시한다. 

## Tutorial
1. Prioritizing qualifying variants from WGS (분석에 맞는 특정 변이만 추출하는 것) - **Hail**
2. Finding noncoding variants from qualifying variants
3. Predicting functional impact of noncoding variants using Enformer model

- Qualifying variant = genome에는 굉장히 많은 variant가 나타난다. Qualifying variant는 이중에서도 분석에 사용할 수 있는 variant를 일컬음.
 - Complication 1. false positive call이 많기 때문에 high quality variant만 추출해야 함 2. 추출된 변이로부터 어떤 식의 association test를 할지 고민해야함.
- **Variant calling** : 하나의 locus에서 특정 샘플이 갖는 유전형을 찾는 과정. *Joint-call pipeline*에서는 하나의 VCF dataset의 여러 샘플이 한번에 genotyping이 되는데 그 과정에서 여러 품질 지표가 나오고, 이 품질 지표를 바탕으로 qualifying variant를 추출하게 됨.
	- Heterozygous mutation : 한쪽은 reference allele이, 한쪽은 alternative (variant) allele이 나타나는 것. 8번 정도 sequencing을 했을 때, 특정 allele이 5:5 비율로 나타나는 경우 heterozygous mutation이라고 보게 됨. 다만 sequencing은 확률적, stochastic process이기 때문에 자주 5:5 비율이 깨진다. 혹은 PCR과정에서 우연하게 strand bias 혹은 염기서열 구성에 따라 mapping 차이가 발생하여 7:3비율로 나타나기도. 따라서 처음 얻은 데이터로부터 여러 quality metrics를 사용하여 좋은 변이만 추출해야 함. 
- 품질지표 1 : AN (Allele number) - 하나의 locus에 나타난 모든 allele의 숫자. 이상적으로는 샘플수의 두배로 AN이 나타나야 하지만, 몇몇 genotype는 quality 이슈로 누락되어 더 낮은 숫자가 관찰되기도 함. 
- 품질지표 2 : FS, SOR - 특정 strand에 의한 systemic bias. GC / AT 결합력 차이로 인해 PCR에서 sequencing read 수가 달라질 수도 있다. 
- 품질지표 3 : Mapping quality. Mapping이 정확한지에 대한 지표.
- 품질지표 4 : DP, QD. Variant가 발생한 위치의 read depth가 얼마나 충분한가. Sequence coverage를 나타내는 지표. 너무 낮은 경우 low-confidence call, 너무 높은 경우는 sequencing에 systemic bias가 발생했다는 것을 암시. 
