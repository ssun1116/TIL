rm(list = ls())

library(Seurat)
library(harmony)

input.dir = "~/Analysis/Seurat/RNA"
seurat.obj = readRDS(paste0(input.dir, "/Seurat.final.RDS"))

DimPlot(object = seurat.obj, reduction = "umap", group.by = "groups")

##### Run harmony
harmony.obj <- RunHarmony(object = seurat.obj, group.by.vars = "groups")

harmony.obj <- FindNeighbors(object = harmony.obj, dims = 1:12, force.recalc = T, reduction = "harmony")
harmony.obj <- FindClusters(object = harmony.obj, resolution = 0.6)
harmony.obj <- RunUMAP(object = harmony.obj, reduction = "harmony", dims = 1:12)

##### Plot
DimPlot(object = harmony.obj, reduction = "umap", group.by = "groups")
DimPlot(object = harmony.obj, reduction = "umap", group.by = "celltypes", label = T, label.size = 10)

##### Cell type annotation
DimPlot(object = harmony.obj, reduction = "umap", label = T, label.size = 10)

cell.markers = c("PTPRC", "CD3D", "CD4", "CD8A", "CD14", "CD79A", "CA9", "VWF", "COL1A1")
VlnPlot(object = harmony.obj, features = cell.markers, pt.size = 0)

cluster.celltype = c("Tcell", "Tcell", "ccRCC", "Myeloid", "Myeloid", "Myeloid", "Myeloid", "ccRCC", "Myeloid", "Tcell", "Fibroblast", "Myeloid", "Bcell", "Endothelial", "Bcell")
names(cluster.celltype) = levels(harmony.obj)
harmony.obj = RenameIdents(harmony.obj, cluster.celltype)

harmony.obj@meta.data$celltypes <- NULL
harmony.obj = AddMetaData(object = harmony.obj, metadata = as.character(Idents(harmony.obj)), col.name = "celltypes") 
DimPlot(harmony.obj, reduction = "umap", label = T, pt.size = 0.5, label.size = 10) + NoLegend()

saveRDS(object = harmony.obj, file = paste0(input.dir, "/Harmony.RDS"))
