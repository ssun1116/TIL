rm(list = ls())

library(Seurat)
library(SeuratData)
library(SeuratWrappers)
library(flexmix)
library(miQC)
library(ggplot2)

input.dir = "~/Analysis/Seurat/RNA/Complete"
input.file = paste0(input.dir, "/Seurat.RDS")
seurat.obj = readRDS(input.file)

##### Run miQC
seurat.obj = RunMiQC(seurat.obj, percent.mt = "percent.mt", nFeature_RNA = "nFeature_RNA", posterior.cutoff = 0.75, model.slot = "flexmix_model")
PlotMiQC(seurat.obj, color.by = "miQC.probability") + scale_color_gradient(low = "grey", high = "purple")
PlotMiQC(seurat.obj, color.by = "miQC.keep")

VlnPlot(object = seurat.obj, features = c("nFeature_RNA", "percent.mt"), group.by = "miQC.keep")
DimPlot(object = seurat.obj, reduction = "umap", group.by = "miQC.keep")

##### Filter low quality cells
###   Option 1.
seurat.qc.obj = subset(seurat.obj, miQC.keep == "keep")

###   Option 2.
seurat.qc.obj = subset(seurat.obj, nFeature_RNA > 500 & percent.mt < 10)

##### Plot 
DimPlot(object = seurat.qc.obj, reduction = "umap")

##### Identification of highly variable features
seurat.qc.obj = FindVariableFeatures(object = seurat.qc.obj, selection.method = "vst")

##### Scaling the data
seurat.qc.obj = ScaleData(object = seurat.qc.obj, features = rownames(seurat.qc.obj))

##### Perform linear dimensional reduction
seurat.qc.obj = RunPCA(object = seurat.qc.obj, features = VariableFeatures(object = seurat.qc.obj))

##### Determine the dimensionality of the dataset
ElbowPlot(object = seurat.qc.obj, ndims = 50)

seurat.qc.obj = JackStraw(object = seurat.qc.obj, num.replicate = 100, dims = 50)
seurat.qc.obj = ScoreJackStraw(object = seurat.qc.obj, dims = 1:50)
JackStrawPlot(object = seurat.qc.obj, dims = 1:50)

##### Cluster the cells
seurat.qc.obj = FindNeighbors(object = seurat.qc.obj, dims = 1:11, force.recalc = T)
seurat.qc.obj = FindClusters(object = seurat.qc.obj, resolution = 0.6)

##### Run non-linear dimensional reduction (UMAP)
seurat.qc.obj = RunUMAP(object = seurat.qc.obj, dims = 1:11)
DimPlot(object = seurat.qc.obj, reduction = "umap", label = T, pt.size = 0.5, label.size = 10)

##### Save Seurat object
saveRDS(object = seurat.qc.obj, file = paste0(input.dir, "/Seurat.QC.RDS"))
