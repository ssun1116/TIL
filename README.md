# Today I Learned 📒
기억은 기록을 이길 수 없다 - Started on February 14th, 2022.
Daily Report : https://trello.com/c/CVVDi7Hh
===========
### KOGO Winter Workshop 0210 [ Single Cell RNA-Seq Analysis ]
- Seurat : PCA + Graph-based method.
- Features -> 많이 쓸수록 continuous한 분포가, 적게 쓸수록 discrete한 분포가 나타남
- UMAP -> tSNE보다 distance. lineage 분석에 유리함. Seurat -> Single cell 분석에서 가장 보편적으로 사용되는 tool.
- vars.to.regress : percent.mt, mito gene등이 DEG로 뜨는 것을 방지.
- CellCycleScoring : phase를 판단. QC metric으로 사용 (FeaturePlot으로 결과 출력해서 확인) -> cell 특성일지, 원하지 않는 요인일지 고민필요!
- miQC : Seurat의 애매한 QC선정 기준을 개선시켜줌! DimPlot으로 보여준다.
- Merge Seurat : 단순 merge시 batch가 나타나므로 normalization 과정이 필요함. DimPlot 확인 시 batch가 너무 크지 않으면 잘 제거하지 X.
- FindAllMarkers -> only.pos = TRUE로 설정하기.
- monocle2 -> UMAP X. Linear 형태의 tree를 만든다. monocle3 -> UMAP을 강조. root를 직접 설정해야하는 한계.

### KOGO Plenary lecture [ Studying immune mechanisms of human diseases by single-cell transcriptomics ] (KAIST 신의철 교수님)
- FACS의 단점: Ex-vivo stimulation-based assay라는 것.
- FACS는 cell의 capacity, ability를 보여준다. T cell에 항원 자극을 주면 Interferon을 잘 낸다라는 결과를 FACS에서 얻었다고 했을 때, 이것은 T cell이 항원 자극을 받으면 기능을 한다는 capacity, ability를 보여주는 것이지 in vivo에서 내고있다는 것을 의미하는 것이 아니다. 능력을 재는 것이지, in vivo 현장에서 내고 있다는 것은 아님.
- 그러나 scRNA-seq 분석은 생체 내에서 꺼냈을 때 당시의 기능을 잴 수 있다. Interferon을 내고 있었는지의 여부를 알 수 있다.
- Inversion Simpson Index (Complexity), Cytotoxicity score.
- **What is Cite-Seq?** : Antibody의 constant region에 unique barcode를 부착. Ab-derived tag를 기반으로 cell을 관찰하는 싱글셀 기법.
- Combined method of highly multiplexed protein marker detection with unbiased transcriptome profiling for thousands of single cells.
- Cite-seq에서 발견한 novel cell type를 FACS로 분석함. (40%가 Cite-seq, 나머지는 FACS 기반의 분석을 진행하심)
- Question. Cite-seq은 surface marker를 target하는 antibody를 사용하는 방법임은 이해했음. 그런데 cite-seq이 RNA-seq이랑은 어떻게 연결되는거지? Cite-seq이 RNA-seq의 범주에 들어가는 것이 맞나? 좀 더 자세한 공부가 필요.

## 집사TV [CITE-seq을 통해 수용체의 세포 표면 발현량을 단일세포 단위에서 대량으로 정량해 봅시다]
- Link : https://www.youtube.com/watch?v=rA7Hqq52-Ug
- Fluorescence-activated cell sorting (FACS) : Surface receptor를 정량하는 전통적인 방법. Antibody 끝부분에 fluorophore를 붙여둠으로써, 특정 wavelength의 빛을 쬐였을 때 emission되는 signal를 정량하여 detect하는 방법, 즉 fluorescent antibody를 사용하는 방법. 
- CD8 / CD4를 target하는 FACS 분석을 통해 T cell이 분화해나갈 때, CD4-/CD8- (Double negative) -> CD4+/CD8+ (Double positive) -> CD4+ 혹은 CD8+ (Single positive)로 분화한다는 것을 발견할 수 있었음.
- 한계 : 수많은 surface marker 중 여러 개를 한번에 분석하고 싶을 때, fluorophore 시그널의 중복 + 다차원 데이터 시각화 문제로 인해 여러 receptor를 detect하기가 어려움.
- Fluorophore마다 emission되는 range가 넓기 때문에, 특정 범위에 속하는 fluorophore가 한 가지가 아님. 여러 개가 detect되어지게 되면서, 정확한 정량이 어렵다.
- 이러한 한계를 극복하기 위해, 항체에 fluorophore를 붙이는 게 아니라 barcode를 붙이는 방식이 바로 **Cite-seq**.
- Droplet level에서 PCR을 할 때 RNA와 barcode를 동시에 정량 (transcriptome 분석 + epitope 분석). 따라서 sscRNA-seq과 Antibody barcode analysis를 parallel하게 분석한다고 이해하면 됨. 세포가 갖고 있는 RNA와 surface protein을 함께 정량 가능하다.
- **Barcode : cell specific. Bead에 고유함, UMI : mRNA specific. mRNA에 고유함.**
- Barcode는 하나하나의 cell을 표시하므로, cell 내에 적정 수의 UMI가 들어가있어야 함. 따라서 Barcode와 UMI를 Compare함으로써 QCfmf gksek.
- Gene expression을 분석하는 최종 목표는 protein의 정량임. RNA-seq은 RNA expression과 Protein 발현간의 correlation이 높다고 가정하고 분석을 하는 것임.
- 그러나 실제로는 RNA, Protein의 correlation은 R^2 = 0.5~0.6 정도. RNA expression이 곧 protein expression을 100% 의미하는 것이 아님. 그러나 protein의 정량은 어렵고 비용이 매우 비싸기 때문에 가성비에 따라 RNA 분석을 하는 것인데, 궁극적으로는 결국 Protein을 보는 걸 목표로 한다. 현재 기술로는 200여개의 surface marker를 관찰 가능!

## git - 간편 안내서
- `git clone 사용자명@호스트:/원격/저장소/경로` : 원격 서버의 저장소를 Local에 복제.
- 로컬 저장소는 git이 관리하는 세 그루의 나무로 구성 -> 첫번째 나무인 작업 디렉토리(Working directory)는 실제 파일들로 이루어져있고, 두번째 나무인 인덱스(Index)는 준비 영역(staging area)의 역할을 하며, 마지막 나무인 HEAD는 최종 확정본(commit)을 나타낸다.
- working directory -> `git add <파일>` -> 변경된 파일이 index에 추가됨 ->`git commit -m "이번 확정본에 대한 설명"` -> 변경 내용이 확정되어 로컬 저장소의 HEAD에 반영됨 -> `git push origin master` -> 변경 내용을 원격 서버에 올림. remote git update! 원격 저장소에 변경 내용이 반영됨.

## edX Statistics and R (Rafael Irizarry)
- Notion에 정리중. Link : https://www.notion.so/Statistics-and-R-df761a6d4626401b8ca0e6a4fbcd9b00
