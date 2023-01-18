# Imputation of CoghelpDC

From Braun et al. (2020), Immunity, 
> Cells were then split into Cd226 high, dim, and neg populations based on Cd226 protein expression level. **Cd226hi and Cd226neg cells represent the top and bottom 25% of expression whereas Cd226dim population consists of the middle 50%**. For heatmap generation, the dataset was first down sampled to 300 cells per group, where **indicated imputed gene expression values were used for data visualization**. Imputation was performed on all genes in the dataset using the RunALRA function in Seurat.

- Dividing CoghelpDC into Ccr7 high / low groups → imputation이 필요할 것으로 생각됨.
- Imputation → Processed seurat object에 바로 적용해도 되는 것인지??
    - **As a general rule, imputation should be restricted to visualization and expression filtering and *not* used for differential expression or dimensionality reduction/clustering.**
    - Imputation → Ccr7에 대해서… coghelpDC를 나누는 기준으로만 사용. 전처리 완료된 데이터에 적용해야 함 (전처리에 imputated value를 사용 X)
- Imputation에 사용되는 툴은 크게 세 가지가 존재.
1. **ALRA** ([https://github.com/KlugerLab/ALRA](https://github.com/KlugerLab/ALRA))
2. **scRecover** ([https://bioconductor.org/packages/release/bioc/html/scRecover.html](https://bioconductor.org/packages/release/bioc/html/scRecover.html))
3. **~~enImpute~~** ([https://github.com/Zhangxf-ccnu/EnImpute](https://github.com/Zhangxf-ccnu/EnImpute)) (combines the results obtained from multiple imputation methods - including ALRA, scImpute, SAVER, and MAGIC - to (allegedly) generate a more accurate result)

# Imputation Vignette Study.

Vignette link : [Single-cell RNA-seq Workshop: Imputation (and other resources)](https://rnabioco.github.io/cellar/previous/2019/docs/8_imputation.html)

<p align="center">
 <img width="500" alt="Screen Shot 2023-01-18 at 11 28 38 PM" src="https://user-images.githubusercontent.com/47490862/213204128-0eb7906c-30b6-438c-8478-86c792af367d.png">
 <p/>

- Note that while the alpha and beta cell markers are robustly detected, the **delta and gamma cell markers are more sparse**.
- 아래 덩어리들이 delta, gamma cell인데 이들의 marker는 sparse. cell type specificity가 떨어진다 (완전 CoghelpDC 상황이잖아?!)

## ****ALRA****

Paper link : [Zero-preserving imputation of single-cell RNA-seq data - Nature Communications](https://www.nature.com/articles/s41467-021-27729-z)
<p align="center">
 <img width="800" alt="Screen Shot 2023-01-18 at 11 29 43 PM" src="https://user-images.githubusercontent.com/47490862/213203865-3e3f6ed1-9b83-41a6-a571-20d5c8b3226e.png">
 <p/>

- ALRA performs “zero-preserving” imputation by (1) computing the rank-k approximation for the expression matrix using randomized SVD (Singular Value Decomposition), (2) thresholding each row (gene) by the magnitude of the most negative value of that gene, and (3) rescaling the matrix.
- ALRA reports some very interesting metrics during the run, most notably the proportion of non-zero counts in the matrix before and after imputation. ALRA creates **a new assay slot that contains the imputed data**.

```r
# by default, ALRA is set as the default assay (poor form)
so <- RunALRA(so, setDefaultAssay = FALSE)

# a new assay called 'alra' now appears in the object
so@assays$alra
```

<p align = "center">
 <img width="647" alt="Screen Shot 2023-01-18 at 11 40 58 PM" src="https://user-images.githubusercontent.com/47490862/213204651-82aa0313-e8c2-4100-87f5-12020789b997.png">
 <p/>

- We can now access the alra imputed matrix from any Seurat plotting function using the “alra_” prefix.
- The expression of the the delta and gamma cell markers is now uniformly high in the relevant clusters
- Ccr7 division 뿐 아니라, CoghelpDC marker gene 찾는데도 도움 될 듯!!!
