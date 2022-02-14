rm(list = ls())

library(Seurat)

seurat.obj.1 = readRDS("~/Analysis/Seurat/RNA/Complete/Seurat.QC.RDS") # Complete sample
seurat.obj.2 = readRDS("~/Analysis/Seurat/RNA/Resistant/Seurat.QC.RDS") # Resistant sample
output.dir = "~/Analysis/Seurat/RNA"

##### Merging Two Seurat Objects 
seurat.obj = merge(x = seurat.obj.1, y = seurat.obj.2, add.cell.ids = c("Complete", "Resistant"))
seurat.obj@meta.data$groups = do.call(rbind, strsplit(x = rownames(seurat.obj@meta.data), split = "_"))[,1]

##### Identification of highly variable features
seurat.obj = FindVariableFeatures(object = seurat.obj, selection.method = "vst")

VariableFeaturePlot(object = seurat.obj)

##### Scaling the data
seurat.obj = ScaleData(object = seurat.obj, features = rownames(seurat.obj))

##### Perform linear dimensional reduction
seurat.obj = RunPCA(object = seurat.obj, features = VariableFeatures(object = seurat.obj))

##### Determine the dimensionality of the dataset
ElbowPlot(object = seurat.obj, ndims = 50)

# seurat.obj = JackStraw(object = seurat.obj, num.replicate = 100, dims = 50)
# seurat.obj = ScoreJackStraw(object = seurat.obj, dims = 1:50)
# JackStrawPlot(object = seurat.obj, dims = 1:50)

##### Cluster the cells
seurat.obj = FindNeighbors(object = seurat.obj, dims = 1:12, force.recalc = T)
seurat.obj = FindClusters(object = seurat.obj, resolution = 0.6)

##### Run non-linear dimensional reduction (UMAP)
seurat.obj = RunUMAP(object = seurat.obj, dims = 1:12)

DimPlot(object = seurat.obj, reduction = "umap", label = T, pt.size = 0.5, label.size = 10)
DimPlot(object = seurat.obj, group.by = "groups", reduction = "umap", label = T, pt.size = 0.5, label.size = 10)

##### Save Seurat object
saveRDS(object = seurat.obj, file = paste0(output.dir, "/Seurat.merge.RDS"))
