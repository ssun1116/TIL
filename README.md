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
