## Identification / quantification of intercellular signaling pathways

<p align="center">
  <img width="700" alt="image" src="https://user-images.githubusercontent.com/47490862/212537508-b1344f17-6f92-4416-bafd-be3586464e22.png">
<p/>

- PPI database의 확장 -> 보통 **ligand-receptor pair**를 기반으로 intercellular communication을 추론함.
- CCI 분석에서 사용되는 ligand type : hormone, growth factor, chemokine, cytokine, and neurotransmitter.
- Ligand를 받은 receiver cell : trigger downstream signaling -> altered transcription factor activity / gene expression.
- 이러한 CCI 분석은 사실 proteomics + transcriptomics를 함께 보는게 최적이긴 하지만, RNA-seq data가 더 많고, 쉽고, 직관적인 분석이 가능. 
  - 또한 Transcriptomic data는 Bulk, microdissected tisuse, single-cell suspension 등 다양한 resolution을 가질 수 있지만, proteomics를 single-cell level에서 하는 것은 아직 개발중.
  - 단, transcriptomics에서의 추론 결과는 false positive에 대해 신중한 고려와 검증이 필요하다!

## 1. CCI 분석이 적용되는 분야
###  Cell development
 - Fate decisions are regulated by megakaryocyte-derived stimulatory factors and monocyte-derived inhibitory factors.
 - Ligand production : cell type specific. Limited ligand signaling -> stem cell fate에 speicificity를 부여.
### Organ development and homeostasis
 - Progenitor cell이 send / receive하는 signal에 의존. (ex. brain : neurogenesis에서 CCC가 작용)
 - Aging, disease, infection, injuries -> multicellular communication이 작용.
### Immune interaction
 - Recruitment and positioning of immune cells, response to viral infection, tumor microenvironment (EMT)

## 2. CCI 분석에 사용되는 데이터베이스와 수학적 모델
### Buildling from PPIs.
- 여러 연구는 모든 유전자 또는 특정 세포 마커의 co-expression, 발현 프로파일 또는 regulatory network의 유사성에 초점을 맞추는데, 대부분의 연구는 결과의 생물학적 해석을 용이하게 하는 상호 작용 단백질의 literature-curated list에 의존한다.
- 이러한 literature-curated list는 false positive가 많고, protein complex와 subunit에 대한 정보가 부족하다는 한계가 있다.
- 최근의 computational tool (ex. CellPhoneDB, CellChat, ICELLNET) 은 이러한 multimeric protein / complex interaction 정보를 포함함.
- LR pair를 통한 CCI 유추 외에도, enzyme 생산 유전자의 발현량을 기반으로 metabolite secretion data를 유추하거나, downstream signaling gene product / regulatory netowrk를 함께 보는 등의 보완 연구가 가능.
- 이렇게 많은 보완이 필요하긴 하지만, PPIs, expecially ligand-receptor pairs have been central to decipher CCC in all strategies.
- Score : expression을 기반으로 계산됨 -> gene expression이 protein abundance를 나타내고 / protein abundance만으로 PPI binding을 추론하기에 충분하다고 가정 (PTM, complex 등을 무시)
  - **Binary ('expression thresholding', 'differential combinations') or Continuous ('expression product', 'expression correlation')**

### Binary score.
- *Expression thresholding* : LR pair에서 각각 expression value를 thresholding -> 두 gene이 모두 통과하면 'active', 통과하지 못하면 'inactive'.
- *Differential combintations* : 'active' interacting partner를 확인하기 위해 differential gene expression 분석을 활용 (sample or cell-type specific manner)
- Simple하다는 장점은 있지만, threshold를 직접 선정해야 하기 때문에 false positive / negative를 많이 만들어낸다. 

### Continuous score.
- *Expression product* : 양쪽 gene의 expression을 곱함. 다만 한 쪽 gene만 아주 다른 expression을 가지는 경우 한쪽이 signal을 dominate하게 되므로 문제가 있음. 미리 housekeeping gene 등을 써서 cell-type normalization을 하는 등 전처과정을 거치면 이 영향을 완화할 수 있다.
- *Expression correlation* : Correlation between the expression of interacting proteins. 이 경우 data sparsity가 correlation coefficient에 영향을 크게 줄 수 있다. 

=> limitation을 이해하고 data set processing을 알맞게 진행하는 것이 false discovery를 최소화하는 방법!!

## 3. 사용되는 툴들의 특징과 강/약점



## 4. CCI 분석 결과를 검증하는 방법
