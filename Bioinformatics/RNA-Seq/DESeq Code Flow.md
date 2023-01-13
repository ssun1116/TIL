# Quick Start

```
dds <- DESeqDataSetFromMatrix(countData = cts, 
       colData = coldata, design = ~ batch + condition)
dds <- DESeq(dds)
resultNames(dds) # lists the coefficients
res <- results(dds, name = "condition_trt_vs_untrt")
res_2 <- lfcShrink(dds, coef="condition_trt_vs_untrt_", type = "apeglm") # shrink log fold changes association with condition
```
 - `dds`: DESeqDataSet. read counts를 `dds`라는 object class로 저장한다.
  - RangedSummarizedExperiment. Ranged : counts are associated with genomic ranges (exons)
 - `design` : how to model the samples
  - want to measure the effect of condition, controlling for batch differences.
  - `~` 부터 시작해서 `+` 기호로 variables 덧붙여가는 것이 design formula for robust analysis. 
  - the factor `batch` and `condition` should be columns of `coldata`

# Input data

- DESeq2 packages는 input 데이터로 integer matrix 형태의 sequence 데이터를 필요로 하며, input 데이터는 un-normalized sequencing reads여야 한다. 
 - **row** : gene | binding region | peptide sequence , **column** : sample
 - RNA-seq workflow의 count matrice 생성 techniques 참고할 것! (http://www.bioconductor.org/help/workflows/rnaseqGene/)

## Transcript abundance files and tximport/ tximeta

- **recommended pipeline**
 - use fast transcript abundance quantifiers upstream of DESeq2
 - create gene-level count matrices by importing quantification data using `tximport`
 - applicable for *Salmon, Sailfish, kallisto, RSEM* data
- This approach is for **estimated** counts, not for *normalized* counts.

## Tutorial using *Salmon*

```
library("tximport")
library("readr")
library("tximportData")
```
- Import data from *Salmon* `quant.sf` files stored in the **tximportData** package.

```
dir <- system.file("extdata", package = "tximportData")
```
- `system.file` 함수 사용 대신 quant file이 존재하는 path를 직접 저장할 수도 있다.

```
samples <- read.table(file.path(dir, "samples.txt"), header = TRUE)
samples$condition <- factor(rep(c("A", "B"), each = 3))
```
- 임의의 data이기 때문에 condition을 A, B로 직접 정해주었다.

```
rownames(samples) <- samples$run
samples[,c("pop", "center", "run", "condition")]
```
- data 가공 완료.

```
files <- file.path(dir, "salmon", samples$run, "quant.sf.gz")
names(files) <- samples$run
tx2gene <- read_csv(file.path(dir, "tx2gene.gencode.v27.csv"))
```
- Specify path to the files!

```
txi <- tximport(files, type = "salmon", tx2gene = tx2gene)
```
- Import necessary quantification data for DESeq2
- `tx2gene` 등의 정보에 대해 더 알고 싶다면 논문 참고, 기본 공식처럼 사용하면 될 듯 하다!

```
library("DESeq2")
ddsTxi <- DESeqDataSetFromTximport(txi,
                                   colData = samples,
                                   design = ~ condition)
```
- Construct DESeqDataSet from `txi` and `samples` data

## Tximeta for import with automatic metadata

- tximeta는 `tximport`와 같은 기능에 추가로 GENCODE, Ensembl, RefSeq 등의 annotation metadata를 자동으로 추가해준다는 장점이 있다.

```
coldata <- samples
coldata$files <- files
coldata$names <- coldata$run
library("tximeta"
se <- tximeta(coldata)
ddsTxi <- DESeqDataSet(Se, design  = ~ condition)
```
## Count matrix input

- 만약 read counts matrix를 가지고 있다면, `DESeqDataSetFromMatrix` 함수를 사용하자. 
 - 단, 사용자가 counts matrix, samples data, design formula를 직접 제공할 수 있어야 함.

```
library("pasilla")
pasCts <- system.file("extdata", "pasilla_gene_counts.tsv", package = "pasilla", mustWork = TRUE)
pasAnno <- system.file("extdata", "pasilla_sample_annotation.csv", pacakge = "pasilla", mustWork = TRUE)
cts <- as.matrix(read.csv(pasCts, sep = "\t", row.names = "gene_id"))
coldata <- read.csv(pasAnno, row.names = 1)
coldata <- coldata[ ,c("condition", "type")]
```
- *pasilla* package를 이용한 함수사용 튜토리얼. 
 - `cts` : count matrix
 - `coldata` : sample information table.

- DESeq2에서는 count matrix의 column 순서와 column data의 row 순서가 같아야 하기 때문에 DESeq2로 데이터가 **consistent order**로 전달되어야 한다. 따라서 correct order로 되어 있지 않다면 re-arrange 과정을 필수적으로 거쳐야 한다.

```
all(rownames(coldata) == colnames(cts))
```
- 즉, 위 코드의 실행 결과가 **TRUE**여야 함.
 - count matrix의 column names와 col data의 rownames가 all SAME!

```
rownames(coldata) <- sub("fb", " ", rownames(coldata))
cts <- cts[, rownames(coldata)]
library("DESeq2")
dds <- DESeqDataSetFromMatrix(countdata = cts, colData = coldata, design = ~condition)
```
- 이렇게 가공 과정을 마친 뒤에 DESeqDataSet을 만들 수 있다!

## Note on factor levels

- R은 default로 reference level을 factor로 받아 알파벳 순서로 정렬한다. 
 - 따라서 부가적인 조건을 달지 않으면 자동으로 comparison이 level들을 알파벳 순서로 이루어진다!
 - factor level의 comparison 방법을 설정하려면 `contrast` argument 사용하거나 직접 factor level을 설정해주면 된다.

```
dds$condition <- factor(dds$condition, levels = c("untreated", "treated")
```
- DESeqDataSet의 column을 subset하려면 (특정 샘플들 제거) `droplevels` 함수 사용
 - current DESeqDataSet에 sample 정보가 없는 level들을 제거

```
dds$condition <- droplevels(dds$condition)
```
- `collapseReplicates` 함수를 사용하면 technical replicate(multiple sequencing runs of same library)로부터의 count들을 count matrix의 single column으로 통합할 수 있다.

# Differential expression analysis

- DESeq : standard differential expression analysis step.
- `results` : log2 fold changes, p value, adjusted p value 정보를 포함하는 results table을 생성하는 함수.
 - `results` function은 자동적으로 each gene의 normalized counts 평균을 기반으로 특정 cutoff에 따라 adjusted p value를 보고 filtering 작업을 수행한다.
 - default로 `alpha`값은 0.1로 세팅되어있으며 이 값은 조절될 수 있다.

```
dds <- DESeq(dds)
res <- results(dds)
res05 <- results(dds, alpha = 0.05)
```
- 특정한 coefficient or contrast에 대해서 result table을 생성하려면 다음과 같은 코멘드를 작성하면 된다:

```
res <- results(dds, contrast = c("condition", "treated", "untreated"))
```

## Log fold change shrinkage

- LFC로 shrinkage를 사용하는 것은 visualization과 gene ranking을 위해서이다.
 - `lfcShrink` 함수를 사용, method는 `apeglm`으로 사용하였다.
 - object, shrink하려는 coefficient의 이름 혹은 숫자(resultsNames 함수 사용했을 때 string의 순서가 곧 숫자)를 입력하면 된다.

```
resLFC <- lfcShrink(dds, coef = "condition_untreated_vs_treated", type = "apeglm")
```

# Exploring and exporting results
## MA-plot

- `plotMA` 함수를 사용하면 DESeqDataSet normalized counts들에 적용 가능한 log2 fold changes를 알 수 있다.
 - adjusted p value값이 0.1 이하면 빨간색 점으로 표시된다.
- shrunken log2 fold changes 값으로 plot을 그리면 noise가 제거된다.

```
plotMA(res, ylim = c(-2, 2))
plotMA(resLFC, ylim = c(-2, 2))
```
- 단, 지금까지 사용된 LFC 방식은 certain dataset에는 too strong. 따라서 adaptive shrinkage estimator가 필요할 수 있다. 
- argument인 `type`을 조정하는 것으로 가능!
 - `apeglm` : adaptive t prior shrinkage estimator
 - `ashr` : fit a mixture of Normal distributions to form the prior, with method = "shrinkage"
 - `normal` : original. adaptive Normal distribution as prior.
- 더 자세한 내용은 extended section on shrinkage estimators 참고! (note 캡처해둠)

## Plot counts

- `plotCounts` : single gene에 대해서 특정 기준으로 분류한 group의 **count**를 확인하는 데 사용하는 함수.
 - `intgroup` argument의 variable에 따라 count들이 그룹화됨.

```
plotCounts(dds, gene = which.min(res$padj), intgroup = "condition")
```
- results table에서 가장 작은 p value를 가진 gene으로 specify한 뒤 condition에 따라 *treated*와 *untreated*로 그룹화한 뒤 plot을 통해 count를 확인하는 커맨드.
- customizing을 추가하고 싶으면 `returnData = TRUE` argument를 추가하고 plot 결과를 변수에 저장한 뒤 ggplot으로 custom을 추가할 수 있다.

```
d <- plotCounts(dds, gene = which.min(res$padj), intgroup = "condition", returnData = TRUE)
ggplot(d, aes(x = condition, y = count)) +
           geom_point(position = position_jitter(w = 0.1, h = 0)) +
           scale_y_log10(breaks = c(25, 100, 400))
```

- `mcols` : more information on results columns.

# Data transformations and visualizations

- test for differential expression : raw counts, discrete distribution으로 작업
- downstream analysis (visualization or clustering) : transformed version으로 작업 (e.g. logarithm - pseudocounts)

```
vsd <- vst(dds, blind = FALSE)
rld <- rlog(dds, blind = FALSE)
head(assay(vsd), 3))
```
- `assay` : extract matrix of normalized values.

# Sample clustering

## Heatmap of sample-to-sample distances

- 우선 `dist` function을 사용하여 count matrix transpose 처리한다.

```
sampleDists <- dist(t(assay(vsd)))
sampleDistMAtrix <- as.matrix(sampleDists)                                                                                                                                                                                                                                                                                           
rownames(sampleDistMatrix) <- paste(vsd$condition, vsd$type, sep = "-")
colnames(sampleDistMatrix) <- NULL
pheatmap(sampleDistMatrix, clustering_distance_rows = sampleDists, clustering_distance_cols = sampleDists, col = colors)
```

## PCA plot

- shows samples spanned by first two principal components.
 - 크로마토그래피와 같다고 보면 됨!

```
plotPCA(vsd, intgroup = c("condition", "type"))
```

## Dispersion plot

- plotting dispersion estimates

```
plotDispEsts(dds)
```

