### Quick start for DESeq2 gene-level DE
```
library(DESeq2)
dds <- DESeqDataSet(se, design=~batch + condition)
dds <- DESeq(dds) # fits the DESeq2 model
res <- results(dds, contrast=c("condition","trt","ctl"))
lfc <- lfcShrink(dds, coef="condition_trt_vs_ctl")
```

sva -> hidden batch. structural difference.

pseudoaligner : rapid quantify of transcript abundance without alignment step. ex> salmon.
These pseudoaligners quickly generate gene count matrices -> tximport로 gene level로 변환해서 DE에 사용 가능! 


## How do I use VST or rlog data for differential testing?
The variance stabilizing and rlog transformations are provided for applications other than differential testing, for example clustering of samples or other machine learning applications. For differential testing we recommend the DESeq function applied to raw counts as outlined above.

## Why after VST are there still batches in the PCA plot?
The transformations implemented in DESeq2, vst and rlog, compute a variance stabilizing transformation which is roughly similar to putting the data on the log2 scale, while also dealing with the sampling variability of low counts. It uses the design formula to calculate the within-group variability (if blind=FALSE) or the across-all-samples variability (if blind=TRUE). It does not use the design to remove variation in the data. It therefore does not remove variation that can be associated with batch or other covariates (nor does DESeq2 have a way to specify which covariates are nuisance and which are of interest).

It is possible to visualize the transformed data with batch variation removed, using the removeBatchEffect function from limma. This simply removes any shifts in the log2-scale expression data that can be explained by batch. The paradigm for this operation for designs with balanced batches would be:

```
mat <- assay(vsd)
mm <- model.matrix(~condition, colData(vsd))
mat <- limma::removeBatchEffect(mat, batch=vsd$batch, design=mm)
assay(vsd) <- mat
plotPCA(vsd)
```

The design argument is necessary to avoiding removing variation associated with the treatment conditions. See ?removeBatchEffect in the limma package for details.
