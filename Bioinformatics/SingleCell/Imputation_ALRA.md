# Imputation of CoghelpDC

From Braun et al. (2020), Immunity, 

![Untitled](Imputation%20of%20CoghelpDC%2083352a48a7f8475ba11a14722fd05fbe/Untitled.png)

Cells were then split into Cd226 high, dim, and neg populations based on Cd226 protein expression level. **Cd226hi and Cd226neg cells represent the top and bottom 25% of expression whereas Cd226dim population consists of the middle 50%**. For heatmap generation, the dataset was first down sampled to 300 cells per group, where **indicated imputed gene expression values were used for data visualization**. Imputation was performed on all genes in the dataset using the RunALRA function in Seurat.

- Dividing CoghelpDC into Ccr7 high / low groups → imputation이 필요할 것으로 생각됨.
- Imputation → Processed seurat object에 바로 적용해도 되는 것인지??
    - **As a general rule, imputation should be restricted to visualization and expression filtering and *not* used for differential expression or dimensionality reduction/clustering.**
    - Imputation → Ccr7에 대해서… coghelpDC를 나누는 기준으로만 사용. 전처리 완료된 데이터에 적용해야 함 (전처리에 imputated value를 사용하면 안됨
- Imputation에 사용되는 툴은 크게 세 가지가 존재.
1. **ALRA** ([https://github.com/KlugerLab/ALRA](https://github.com/KlugerLab/ALRA))
2. **scRecover** ([https://bioconductor.org/packages/release/bioc/html/scRecover.html](https://bioconductor.org/packages/release/bioc/html/scRecover.html))
3. **~~enImpute~~** ([https://github.com/Zhangxf-ccnu/EnImpute](https://github.com/Zhangxf-ccnu/EnImpute)) (combines the results obtained from multiple imputation methods - including ALRA, scImpute, SAVER, and MAGIC - to (allegedly) generate a more accurate result)
- 아래 vignette를 따라가면서 imputation method - **ALRA와 scRecover (scImpute로 대체) 를 공부**

[Single-cell RNA-seq Workshop: Imputation (and other resources)](https://rnabioco.github.io/cellar/previous/2019/docs/8_imputation.html)

# Imputation Vignette Study.

![Untitled](Imputation%20of%20CoghelpDC%2083352a48a7f8475ba11a14722fd05fbe/Untitled%201.png)

- 예제 데이터에서… Note that while the alpha and beta cell markers are robustly detected, the **delta and gamma cell markers are more sparse**.
- 아래 덩어리들이 delta, gamma cell인데 이들의 marker는 sparse. cell type specificity가 떨어진다 (완전 CoghelpDC 상황이잖아?!)

## ****ALRA****

---

[Zero-preserving imputation of single-cell RNA-seq data - Nature Communications](https://www.nature.com/articles/s41467-021-27729-z)

![Untitled](Imputation%20of%20CoghelpDC%2083352a48a7f8475ba11a14722fd05fbe/Untitled%202.png)

- ALRA performs “zero-preserving” imputation by (1) computing the rank-k approximation for the expression matrix using randomized SVD (Singular Value Decomposition), (2) thresholding each row (gene) by the magnitude of the most negative value of that gene, and (3) rescaling the matrix.
- ALRA reports some very interesting metrics during the run, most notably the proportion of non-zero counts in the matrix before and after imputation. ALRA creates **a new assay slot that contains the imputed data**.

```r
# by default, ALRA is set as the default assay (poor form)
so <- RunALRA(so, setDefaultAssay = FALSE)

# a new assay called 'alra' now appears in the object
so@assays$alra
```

![Untitled](Imputation%20of%20CoghelpDC%2083352a48a7f8475ba11a14722fd05fbe/Untitled%203.png)

- We can now access the alra imputed matrix from any Seurat plotting function using the “alra_” prefix.
- The expression of the the delta and gamma cell markers is now uniformly high in the relevant clusters
- Ccr7 division 뿐 아니라, CoghelpDC marker gene 찾는데도 도움 될 듯!!!

## ****scImpute****

---

[An accurate and robust imputation method scImpute for single-cell RNA-seq data - Nature Communications](https://www.nature.com/articles/s41467-018-03405-7)

- scRecover is not an imputation method per se, but rather a method for **identifying dropouts (technical zeros) using a zero-inflated negative binomial model**.
- 예전에 나온 패키지이고, issue tracking이 잘 되지 않는 것 같음. ALRA method로 결과 만들고 분석하기!

# Imputation analysis using ALRA