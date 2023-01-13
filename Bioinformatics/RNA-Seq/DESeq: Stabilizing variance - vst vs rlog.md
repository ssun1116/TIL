## Variance Stabilizing Transformation (VST) and rlog

DESeq 이용한 PCA plotting의 흐름
1) dds <- DESeqDataSet(txi, design = ~ ... )
2) Pre-filtering
3) variance stabilizing transformation and rlog
4) PCA plotting

PCA와 같은 multidimensional data 분석은 다음 조건에서 work best!

- **same range of variance, different ranges of mean value** (homoskedastic)

PCA를 그냥 matrix of counts나 normalized counts (corrected for differences in sequencing depth)에다가 바로 하게 되면, highest count를 가진 gene들이 샘플들 사이에서 가장 큰 absolute difference를 보이게 되어 highest counts gene들에 대해 엄청나게 큰 영향을 받게 된다. 

이러한 현상을 피하기 위해서는, 두 가지 전략을 취할 수 있다.

1) **Take logarithm of the normalized count values**
2) **Plus a pseudocount of 1** : but, lowest count를 가진 gene의 variance가 부풀려지면서 noise를 상당히 만들 수 있음.

이를 보완하고 variance를 stabilize해주는 함수가 `vst()`와 `rlog()`
-> For genes with lower counts, the values are **shrunken towards a middle value** : become approximately **homoskedastic** and can be used directly for **computing distances between samples**, making PCA plots.
-> assay 형태로 object를 return.

## Which transformation to choose?

`vst()` : 계산 빠르고 outlier에 덜 sensitive. medium-to-large dataset (n > 30)에 적합.
`rlog()` : small dataset에 잘 작동하며 (n < 30) 샘플들 간의 sequencing depth가 다양할 때 outperform.

**BUT** differential analysis할 때는 transformation하면 안 됨. **raw count**에 DESeq function을 사용하는 것을 추천! 
