rm(list = ls())

library(Seurat)

cellranger.dir = "~/Analysis/CellRanger/RNA/Complete/outs/filtered_feature_bc_matrix"
output.dir = "~/Analysis/Seurat/RNA/Complete"

##### Load raw count data
seurat.counts = Read10X(data.dir = cellranger.dir)

##### Create a Seurat Object
seurat.obj = CreateSeuratObject(counts = seurat.counts)

##### QC and selecting cell
seurat.obj[["percent.mt"]] = PercentageFeatureSet(object = seurat.obj, pattern = "^MT-")

VlnPlot(object = seurat.obj, features = c("nFeature_RNA", "nCount_RNA", "percent.mt"), ncol = 3)

##### Normalizing the data
seurat.obj = NormalizeData(object = seurat.obj, normalization.method = "LogNormalize")

##### Identification of highly variable features
seurat.obj = FindVariableFeatures(object = seurat.obj, selection.method = "vst")
VariableFeaturePlot(object = seurat.obj)

##### Scaling the data
seurat.obj = ScaleData(object = seurat.obj, features = rownames(seurat.obj))

##### Perform linear dimensional reduction
seurat.obj = RunPCA(object = seurat.obj, features = VariableFeatures(object = seurat.obj))

##### Determine the dimensionality of the dataset
ElbowPlot(object = seurat.obj, ndims = 50)

seurat.obj = JackStraw(object = seurat.obj, num.replicate = 100, dims = 50)
seurat.obj = ScoreJackStraw(object = seurat.obj, dims = 1:50)
JackStrawPlot(object = seurat.obj, dims = 1:50)

##### Cluster the cells
seurat.obj = FindNeighbors(object = seurat.obj, dims = 1:11, force.recalc = T)
seurat.obj = FindClusters(object = seurat.obj, resolution = 0.6)

##### Run non-linear dimensional reduction (UMAP)
seurat.obj = RunUMAP(object = seurat.obj, dims = 1:11)
DimPlot(object = seurat.obj, reduction = "umap", label = T, pt.size = 0.5, label.size = 5)

##### Cell-Cycle Scoring
seurat.obj = CellCycleScoring(seurat.obj, s.features = cc.genes$s.genes, g2m.features = cc.genes$g2m.genes)
## cc genes -> provided in Seurat package.                                                              

FeaturePlot(object = seurat.obj, reduction = "umap", features = c("nFeature_RNA", "percent.mt", "S.Score"), order = T)
VlnPlot(object = seurat.obj, features = "percent.mt")


##### Save Seurat object
saveRDS(object = seurat.obj, file = paste0(output.dir, "/Seurat.RDS"))




