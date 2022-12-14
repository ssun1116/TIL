## clusterProfiler : R Package for Comparing Biological Themes Among Gene Clusters
- Automates the process of biological-term classification and enrichment analysis of gene clusters.
- Gene enrichment를 위한 툴은 많이 개발되어 있고 statistically significant category를 계산하는 것은 어렵지 않지만, enrichment analysis에서 흥미로운 결과를 직접 manually 찾는 과정이 매우 번거롭다는 문제점이 존재함...
- clusterProfiler -> **allows biological theme comparison among gene clusters**
  - `enrichGO` or `enrichKEGG` : calculate enrichment test for GO terms and KEGG pathways based on hypergeometric distiribution.
    -  다른 ontology와의 association 분석도 쉽게 가능함 (ex. DO: Disease Ontology for human -> identification of clinical relavance)
  - `compareCluster` : automatically calculate enriched functional categories of each gene clusters and provide methods for visualization..!

<img width="694" alt="image" src="https://user-images.githubusercontent.com/47490862/207292336-1294f458-846e-422b-b248-a531b87cccdd.png">

### Further Plans for Package Development
1. Use semantic similarity among KEGG / GO terms to aggregate closely related categories. -> *What I Expected!!*
2. Rank gene similarities in each cluster and correlate them to search for enriched categories (more sensibility in finding gene modules)
3. Through acylic graph, compare functional profiles as a whole rather than a set of unrelated categories.

Link for this updates : https://yulab-smu.top/biomedical-knowledge-mining-book/enrichplot.html

-------------------

## Biomedical Knowledge Mining using GOSemSim and clusterProfiler

1. **Over Representation Analysis** : 우리가 기존에 "fisher test"라고 불러왔던 것. Determine whether known biological functions or processes are over-represented (= enriched) in an experimentally-derived gene list, e.g. a list of differentially expressed genes (DEGs). The p-value can be calculated by hypergeometric distribution.
<img width="234" alt="image" src="https://user-images.githubusercontent.com/47490862/207297550-45e79541-afbc-4b3b-8211-08d36029b853.png">

- `N` : total number of genes in the background distribution (all the genes that have annotation)
- `M` : number of genes within that distribution that are annotated (either directly or indirectly) to the gene set of interest
- P-values should be adjusted for multiple comparison.

```
ego <- enrichGO(gene         = gene.df$ENSEMBL,
                OrgDb         = org.Hs.eg.db,
                keyType       = 'ENSEMBL',
                ont           = "CC",
                pAdjustMethod = "BH",
                pvalueCutoff  = 0.01,
                qvalueCutoff  = 0.05)
```

 2. **Gene Set Enrichment Analysis** : 우리가 기존에 "rank-based test"라고 불러왔던 것. All genes can be used in GSEA, aggregating the per gene statistics across genes within a geneset. Genes are ranked based on their phenotypes -> the goal of GSEA is to determine whether the members of priori genes are randomly distributed throughout the ranked gene list or primarily found at the top or bottom.

- Calculation of an Enrichment Score.
  - The enrichment score (ES) represents the degree to which a set S is over-represented at the top or bottom of the ranked list L. The score is calculated by walking down the list L, increasing a running-sum statistic when we encounter a gene in S and decreasing when it is not encountered. The magnitude of the increment depends on the gene statistics (e.g., correlation of the gene with phenotype). The ES is the maximum deviation from zero encountered in the random walk; it corresponds to a weighted Kolmogorov-Smirnov(KS)-like statistic (Subramanian et al. 2005).
- Esimation of Significance Level of ES.
  - The p-value of the ES is calculated using a permutation test. Specifically, we permute the gene labels of the gene list L and recompute the ES of the gene set for the permutated data, which generate a null distribution for the ES. The p-value of the observed ES is then calculated relative to this null distribution.
- Adjustment for Multiple Hypothesis Testing.
  - When the entire gene sets are evaluated, the estimated significance level is adjusted to account for multiple hypothesis testing and also q-values are calculated for FDR control.

```
ego <- gseGO(geneList     = geneList,
              OrgDb        = org.Hs.eg.db,
              ont          = "CC",
              minGSSize    = 100,
              maxGSSize    = 500,
              pvalueCutoff = 0.05,
              verbose      = FALSE)
              
mkk <- gseMKEGG(geneList = geneList,
                 organism = 'hsa',
                 pvalueCutoff = 1)
                 
y <- gsePathway(geneList, 
                pvalueCutoff = 0.2,
                pAdjustMethod = "BH", 
                verbose = FALSE)                 
```

### 여기까지는 보통 FGSEA 결과와 큰 차이가 없음. but... graph visualization 등에서 특화된 툴이다.





