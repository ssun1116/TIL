rm(list = ls())

library(monocle3)
library(Seurat)
library(SeuratData)
library(SeuratWrappers)
library(ggplot2)
library(patchwork)
library(magrittr)

input.dir = "~/Analysis/Seurat/RNA"
seurat.obj = readRDS(paste0(input.dir, "/Harmony.Tcell.RDS"))

cds = as.cell_data_set(seurat.obj, reductions = "umap")
cds = estimate_size_factors(cds)
rowData(cds)$gene_short_name = row.names(rowData(cds))
rowData(cds)$gene_name = row.names(rowData(cds))

cds = cluster_cells(cds)
cds = learn_graph(cds)

plot_cells(cds, color_cells_by = "celltypes", label_groups_by_cluster = F, label_leaves = F, label_branch_points = F, group_label_size=5)

root.cells = rownames(subset(seurat.obj@meta.data, seurat_clusters == "7"))
cds = order_cells(cds, root_cells = root.cells)

plot_cells(cds, color_cells_by = "pseudotime", label_cell_groups = F, label_leaves = F, label_branch_points = F)

cds.test = graph_test(cds, neighbor_graph = "principal_graph", cores = 1)
cds.test = subset(cds.test, q_value < 0.05)
cds.test = cds.test[order(cds.test$morans_I, decreasing = T),]

plot_cells(cds, genes = c("NKG7", "FOXP3"), show_trajectory_graph = F, label_cell_groups = F, label_leaves = F)

