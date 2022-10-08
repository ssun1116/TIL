# Salmon Quantification

- Pseudo-aligner Salmon allows rapid quantification of transcript abundance without alignment step.
- Quickly generate gene count matrices -> tximport로 gene level로 변환해서 DE에 사용 가능! 

### Difference between Alignment vs Mapping

> When we align a read, we're asking for not just where it likely came in the genome, but the exact base to base correspondence. For example, we'd like to get something like, "Read foo likely originated from chr1 positions 123 through 140. The first 7 bases are exact matches between foo and the reference, there's then a 3 base insertion, then the remaining bases match between foo and the reference." When we map a read, we're just asking, "where did it come from?" We don't necessarily care about the exact alignment between the read and where it came from, though. Until recently, "alignment" and "mapping" were pretty much synonymous. Tools like Kallisto and Salmon have changed that, since they can assign reads to genes/features/whatever without needing to look at exact alignments. Since (A) this is faster and (B) we often don't actually care about the alignment, this is a HUGE advantage in some applications.



# Quick start for DESeq2 gene-level DE
```
library(DESeq2)
dds <- DESeqDataSet(se, design=~batch + condition)
dds <- DESeq(dds) # fits the DESeq2 model
res <- results(dds, contrast=c("condition","trt","ctl"))
lfc <- lfcShrink(dds, coef="condition_trt_vs_ctl")
```

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
