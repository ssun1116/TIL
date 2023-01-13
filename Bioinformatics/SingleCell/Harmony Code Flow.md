vignette link : http://htmlpreview.github.io/?https://github.com/immunogenomics/harmony/blob/master/docs/SeuratV3.html

Harmony removes the influence of **dataset-of-origin** from the embedding. We can run Harmony with Seurat workflow. It only requires two changes to the Seurat code.

1. Run Harmony with the `RunHarmony()` function.
2. In downstream analyses, use the Harmony embeddings instead of PCA.

```
seuratObj <- RunHarmony(seuratObj, "dataset")
seuratObj <- RunUMAP(seuratObj, reduction = "harmony")
```

## Initialize Seurat Object

```
pbmc <- CreateSeuratObject(counts = cbind(stim.sparse, ctrl.sparse), project = "PBMC", min.cells = 5)
```

**IMPORTANT DIFFERENCE** : With Harmony integration, need to create only one Seurat object with all cells.

- Harmony의 object를 만들 때는 single cell 데이터들을 `cbind` 통해 묶어서 SeuratObject를 생성해야 함.

```
pbmc <- pbmc %>% NormlizeData(verbose = FALSE)
pbmc <- pbmc %>% FindVariableFeatures(selection.method = "vst", nfeatures = 2000)
pbmc <- pbmc %>% ScaleData(verbose = FALSE)
pbmc <- pbmc %>% RunPCA(pc.genes = pbmc@var.genes, npcs = 20, verbose = FALSE)
```

## Make dataset ID

```
pbmc@meta.data$stim <- c(rep("STIM", ncol(stim.sparse)), rep("CTRL", ncol(stim.sparse))
```

## Run Harmony
```
pbmc <- pbmc %>% RunHarmony("stim", plot_convergence = TRUE)
DimPlot(object = pbmc, reduction = "harmony", pt.size = .1, ground.by = "stim", do.return = TRUE)
VlnPlot(object = pbmc, features = "harmony_1", group.by = "stim", do.return = TRUE, pt.size = .1)
```

## Donwstream analysis
To use the corrected Harmony embeddings rather than PCs,  should set `reduction = 'harmony'`. 

```
pbmc <- pbmc %>% RunUMAP(reduction = "harmony", dims = 1:20)
pbmc <- pbmc %>% FindNeighbors(reduction = "harmony", dims = 1:20)
pbmc <- pbmc %>% FindClusters(resolution = 0.5) %>% identity()
```

## Identify shared cell types with clustering analysis

```
DimPlot(pbmc, reduction = "umap", label = TRUE, pt.size = .1)
```
