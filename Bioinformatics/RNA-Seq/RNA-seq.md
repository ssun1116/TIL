<p align = "center"> <img width="600" alt="image" src="https://user-images.githubusercontent.com/47490862/216755181-578ff856-c0d0-41c3-887d-43f232b3c810.png">

### 전사체 분석의 목적: 유전체 발현량의 측정.
- microarray : probe를 직접 디자인해야함. 알고있는 서열 내에서만 측정이 가능.
- RNA-Seq : probe 디자인 없이, SBS 방식으로 시퀀싱.
   1) DNA 상에 exon, intron이 함게 존재 -> alternative splicing.
   2) RNA 서열에는 3'말단에 polyA tail이 존재. 이 poly A tail을 oligo(dT) detection, RNA만 따로 뽑는다.
   3) 불안정한 RNA를 cDNA synthesis한 후, PCR 증폭하여 library를 만든다.
   4) PCR 이후 유전자 서열을 fragment로 잘라주는 과정을 거침. 유전자 길이를 읽을 수 있는 정도로 자르는 것.
 
<p align = "center"> <img width="600" alt="image" src="https://user-images.githubusercontent.com/47490862/216755195-cc4db2dc-20c1-4cce-8ea8-70f0592770da.png">

### RNA-seq fragment
- 길이는 보통 500bp 정도 (fragment length). 양쪽 끝 말단만 읽는다 -> paired end read. 75 bp 정도 (read length). 
- paired end read 사이의 염기는 읽지 않는다 (insert size). 300bp 정도.
- 결과적으로 만들어진 paired end read가 모든 gene A의 모든 부분을 커버하는 것을 목표로 함.

<p align = "center"> <img width="581" alt="image" src="https://user-images.githubusercontent.com/47490862/216755219-439c2179-6741-4695-b217-4db624465c4c.png">

### RNA-seq 분석 1단계 : QC
- read 양 쪽 끝의 adapter sequence, 혹은 quality가 낮은 서열을 제거하는 것.
- cutadapt 툴로 read를 trimming -> Illumina TruSeq adapter를 제거하고, 동시에 read quality 가 낮은 것들을 제외.
- Read quality에 따라 너무 잘라지면, read가 짧아질 수 있으므로 minimum 길이를 지정해야함 (정해진 값은 없으나, 모든 샘플에 동일하게 적용해야 batch effect가 생기지 않음)

<p align = "center"> <img width="580" alt="image" src="https://user-images.githubusercontent.com/47490862/216755228-b5f414e7-a919-4035-89ae-3ffafe719886.png">

### RNA-seq 분석 2단계 : READ 정렬.
- RNA가 어디서 왔는지 알아보기 위해 reference DNA (참조 유전체 FASTA) 에 RNA를 align.
- RNA는 exon 절로 이루어져있으므로, splicing을 고려하여 정렬되어야 함. 인트론 파트가 포함되거나, read가 두 exon절의 일부를 각각 갖고 있을 수도 있음!
- **strand-specific RNA-seq**인지를 매핑 이전에 확인해야 함. 시퀀싱 회사에서 온 레포트를 확인하거나, 논문을 참고하거나, 정보가 없으면 RF/FR 두 매핑방식 모두 시도해보고 맵핑 레이트를 비교한다.
- samtools : 매핑된 output 파일을 bam 파일로 변환 (read가 reference에 어떻게 붙어있는지 보기 위한 파일)
- 혹은, salmon과 같은 psueoalign tool을 사용하기도 함. 
  
<p align = "center"> <img width="582" alt="image" src="https://user-images.githubusercontent.com/47490862/216755243-3bbbab6a-1cc7-4830-af1d-a3e6802875c3.png">
  
### RNA-seq 분석 3단계 : 정량화.
  
<p align = "center"> <img width="565" alt="image" src="https://user-images.githubusercontent.com/47490862/216756131-8f6ae8e4-fd81-4a00-b229-58d535991140.png">
  
- Gene annotation (gtf) : 해당 유전체의 어떤 지역이 유전자 지역인지에 대한 정보. 위치별 read 개수를 세서 read count를 진행한다.
- 만약 특정 read의 region이 gtf 파일에 없는 경우? StringTie. gtf 파일 외에도 자체 알고리즘으로 assmebly도 가능하고, quantification이 transcript level로 이루어질 수 있다.  
  - 특정 exon이 여러 transcript에 복합적으로 나타날 수 있으므로, transcript level count는 gene level보다 조금 더 까다롭다.
- FeatureCounts : gene count에서는 transcript A, B가 같은 exon을 공유하더라도 어차피 transcript A, B가 같은 gene을 이루므로 상관 없어서 transcript level보다 가볍게 진행할 수 있음.
  
### RNA-seq 분석 4단계 : DEG 분석 (edgeR)
- MDS plot testing -> Case-Control간 차이가 있는지 우선 검증.
  - Normalization : Generalized linear model을 통해 read length에 대한 정규화를 진행.
  - Likelihood-ratio test : p-value, FDR. 
  
