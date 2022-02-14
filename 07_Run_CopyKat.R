rm(list = ls())

library(Seurat)
library(copykat)
library(pheatmap)

input.dir = "~/Analysis/Seurat/RNA"
output.dir = "~/Analysis/CopyKat"

seurat.obj = readRDS(paste0(input.dir, "/Harmony.RDS"))
subset.obj = subset(seurat.obj, celltypes %in% c("ccRCC", "Tcell") & groups == "Resistant")

setwd(output.dir)
counts = subset.obj@assays$RNA@counts
normal.cells = colnames(subset(subset.obj, celltypes == "Tcell"))

copykat.res = copykat(rawmat = counts, id.type = "S", norm.cell.names = normal.cells, n.cores = 1, ngene.chr = 5, LOW.DR = 0.05, UP.DR = 0.2, win.size = 25, KS.cut = 0.15)

