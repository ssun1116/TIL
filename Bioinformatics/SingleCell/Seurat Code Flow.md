## Creating count data - Read10X

https://hbctraining.github.io/scRNA-seq/lessons/readMM_loadData.html

**All single-cell RNA-seq datasets contain three files**:

- `barcodes.tsv` : cellular barcodes present in dataset representing all cells quantified
- `features.tsv` : IDs of quantified genes representing all genes quantified
- `matrix.mtx` : a matrix of count values, where rows are associated with the gene IDs above and columns correspond to the cellular barcodes.

```
# Read in `matrix.mtx`
counts <- readMM("Data/SinglecellPapers/GSE122712_Miller/GSE122712_matrix.mtx.gz")
# Read in `genes.tsv` : genes -> rownames
genes <- read_tsv("Data/SinglecellPapers/GSE122712_Miller/GSE122712_genes.tsv.gz", col_names = FALSE)
gene_ids <- genes$X1
# Read in `barcodes.tsv` : cells -> colnames
cell_ids <- read_tsv("Data/SinglecellPapers/GSE122712_Miller/GSE122712_barcodes.tsv.gz", col_names = FALSE)$X1
# Make the column names as the cell IDs and the row names as the gene IDs
rownames(counts) <- gene_ids
colnames(counts) <- cell_ids

```

위처럼 barcodes 파일과 features (gene) 파일을 직접 불러와서 counts 데이터를 만들게 되는데, 
**이걸 한번에 해주는 함수가 Seurat 패키지의** `Read10X`**이다.**

```
miler.data <- Read10X(data.dir = "Data/SinglecellPapers/GSE122712_Miller/")
```

**디렉토리**만 설정해주면 한번에 세 가지 파일을 모두 찾고 알아서 count data로 만들어줌.

### Seurat Code flow

```
pbmc.counts <- Read10X(data.dir = "~/Downloads/pbmc3k/filtered_gene_bc_matrices/hg19/")
pbmc <- CreateSeuratObject(counts = pbmc.counts)
pbmc <- NormalizeData(object = pbmc)
pbmc <- FindVariableFeatures(object = pbmc)
pbmc <- ScaleData(object = pbmc)
pbmc <- RunPCA(object = pbmc)
pbmc <- FindNeighbors(object = pbmc)
pbmc <- FindClusters(object = pbmc)
pbmc <- RunTSNE(object = pbmc)
DimPlot(object = pbmc, reduction = "umap")
```
