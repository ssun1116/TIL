rm(list = ls())

library(Seurat)

input.dir = "~/Analysis/Seurat/RNA"
seurat.obj = readRDS(paste0(input.dir, "/Seurat.merge.RDS"))
cell.markers = c("PTPRC", "CD3D", "CD4", "CD8A", "CD14", "CD79A", "CA9", "VWF", "COL1A1")

VlnPlot(object = seurat.obj, features = cell.markers, pt.size = 0)
FeaturePlot(object = seurat.obj, reduction = "umap", order = T, features = cell.markers)
DotPlot(object = seurat.obj, features = cell.markers, cols = c("blue", "red")) + RotatedAxis()

cluster.celltype = c("Myeloid", "Tcell", "Myeloid", "ccRCC", "Tcell", "Tcell", "Myeloid", "ccRCC", "Myeloid", "Tcell", "Fibroblast", "Myeloid", "Endothelial", "Tcell", "Bcell", "Bcell")
names(cluster.celltype) = levels(seurat.obj)
seurat.obj = RenameIdents(seurat.obj, cluster.celltype)

seurat.obj = AddMetaData(object = seurat.obj, metadata = as.character(Idents(seurat.obj)), col.name = "celltypes") 

DimPlot(seurat.obj, reduction = "umap", label = TRUE, pt.size = 0.5, label.size = 10) + NoLegend()

saveRDS(object = seurat.obj, file = paste0(input.dir, "/Seurat.final.RDS"))
