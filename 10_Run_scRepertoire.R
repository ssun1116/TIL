rm(list = ls())

library(scRepertoire)
library(Seurat)

input.dir = "~/Analysis/TCR"
seurat.obj = readRDS(paste0(input.dir, "/Harmony.RDS"))

sample.1 = read.csv("~/Analysis/CellRanger/VDJ/Resistant/outs/filtered_contig_annotations.csv")
sample.1$barcode = paste0("Tumor_", sample.1$barcode)
sample.1$contig_id = paste0("Tumor_", sample.1$contig_id)
sample.1 = sample.1[sample.1$barcode %in% rownames(seurat.obj@meta.data),]

sample.2 = read.csv("~/Analysis/CellRanger/VDJ/Resistant-Normal/outs/filtered_contig_annotations.csv")
sample.2$barcode = paste0("Normal_", sample.2$barcode)
sample.2$contig_id = paste0("Normal_", sample.2$contig_id)
sample.2 = sample.2[sample.2$barcode %in% rownames(seurat.obj@meta.data),]

contig_list = list(sample.1, sample.2)

combined = combineTCR(contig_list, samples = c("Resistant", "Resistant"), ID = c("Tumor", "Normal"), cells ="T-AB", filterMulti = F)

quantContig(combined, cloneCall = "gene+nt", scale = T)

clonalDiversity(combined, cloneCall = "gene", group = "ID", n.boots = 100)

cells = paste0("Resistant_", seurat.obj@meta.data$groups, "_", rownames(seurat.obj@meta.data))
seurat.obj = RenameCells(object = seurat.obj, new.names = cells)
seurat.combined.obj <- combineExpression(combined, seurat.obj, cloneCall = "gene", proportion = F)

DimPlot(seurat.combined.obj , group.by = "cloneType")

combined2 <- expression2List(seurat.combined.obj, group = "seurat_clusters")

clonalDiversity(combined2, cloneCall = "nt")

compareClonotypes(combined, numbers = 10, samples = c("Resistant_Tumor", "Resistant_Normal"), cloneCall="aa", graph = "alluvial")
clone.df <- compareClonotypes(combined, numbers = 10, samples = c("Resistant_Tumor", "Resistant_Normal"), cloneCall="aa", graph = "alluvial", exportTable = T)

clone <- as.character(subset(clone.df, Proportion == max(clone.df$Proportion))$Clonotypes)
clone.df <- data.frame(table(subset(seurat.combined.obj@meta.data, CTaa == clone)$celltypes))

ggplot(clone.df, aes(x = "", y = Freq, fill = Var1)) + 
  geom_bar(stat="identity", width = 1) + 
  coord_polar("y", start = 0)
