rm(list = ls())

library(Seurat)
library(harmony)
library(dplyr)

input.dir = "~/Analysis/Seurat/RNA"

seurat.obj = readRDS(paste0(input.dir, "/Harmony.RDS"))
subset.obj = subset(seurat.obj, celltypes == "Tcell")

subset.obj = FindVariableFeatures(object = subset.obj, selection.method = "vst")
subset.obj = ScaleData(object = subset.obj, features = rownames(subset.obj))
subset.obj = RunPCA(object = subset.obj, features = VariableFeatures(object = subset.obj))

harmony.obj = RunHarmony(subset.obj, "groups")

harmony.obj = FindNeighbors(object = harmony.obj, dims = 1:15, force.recalc = T, reduction = "harmony")
harmony.obj = FindClusters(object = harmony.obj, resolution = 0.6)
harmony.obj = RunUMAP(object = harmony.obj, reduction = "harmony", dims = 1:15)

DimPlot(object = harmony.obj, reduction = "umap", label = T, label.size = 10)
DimPlot(object = harmony.obj, reduction = "umap", group.by = "groups")

##### Finding differentially expressed features
marker.df = FindAllMarkers(object = harmony.obj, logfc.threshold = 0.25, min.pct = 0.25,  only.pos = T)

marker.df <- subset(marker.df, p_val_adj < 0.05)
marker.df %>% group_by(cluster) %>% top_n(n = 10, wt = avg_log2FC) -> top10

DoHeatmap(harmony.obj, features = top10$gene) + NoLegend()

##### Cell type identity
cell.markers = c("CD4", "CD8A", "LAG3", "FOXP3", "CTLA4", "CCR7", "SELL", "KLRF1")

FeaturePlot(object = harmony.obj, reduction = "umap", order = T, features = cell.markers)
VlnPlot(object = harmony.obj, features = cell.markers, pt.size = 0)

cluster.celltype = c("CD8", "CD4", "CD8", "NK", "Treg", "CD8", "NK", "CD8")
names(cluster.celltype) = levels(harmony.obj)
harmony.obj = RenameIdents(harmony.obj, cluster.celltype)
harmony.obj = AddMetaData(object = harmony.obj, metadata = as.character(Idents(harmony.obj)), col.name = "celltypes") 

DimPlot(object = harmony.obj, reduction = "umap", group.by = "celltypes", label = T, label.size = 10)


saveRDS(object = harmony.obj, file = paste0(input.dir, "/Harmony.Tcell.RDS"))



