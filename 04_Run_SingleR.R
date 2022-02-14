rm(list = ls())

library(Seurat)
library(SingleR)
library(celldex)
library(scuttle)
library(scran)
library(ggplot2)

#####	Load Seurat object
input.file = "~/Analysis/Seurat/RNA/Seurat.merge.RDS"
seurat.obj = readRDS(input.file)

#####	Load reference database
ref.obj = HumanPrimaryCellAtlasData()

sce.obj = as.SingleCellExperiment(seurat.obj)
genes = intersect(rownames(sce.obj), rownames(ref.obj))
sce.obj = sce.obj[genes,]
ref.obj = ref.obj[genes,]
sce.pred = SingleR(test = sce.obj, ref = ref.obj, labels = ref.obj$label.main, de.method = "wilcox")

seurat.obj = AddMetaData(object = seurat.obj, metadata = sce.pred$labels, col.name = "labels")

DimPlot(object = seurat.obj, reduction = "umap", group.by = "labels")


##### Dot plot
labels.count.df = aggregate(cbind(count = labels) ~ seurat_clusters+labels, data = seurat.obj@meta.data, FUN = function(x){NROW(x)})

ggplot(labels.count.df, aes(x = seurat_clusters, y = labels, size = count))+ geom_point()

