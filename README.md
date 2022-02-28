# Today I Learned 📒
기억은 기록을 이길 수 없다 - Started on February 14th, 2022.

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
- 그러나 scRNA-seq 분석은 생체 내에서 꺼냈을 때 그 때의 그 기능을 잴 수 있다. Interferon을 내고 있었는지의 여부를 알 수 있다.
