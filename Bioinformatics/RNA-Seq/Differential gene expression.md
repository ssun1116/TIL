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
