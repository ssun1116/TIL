## clusterProfiler : R Package for Comparing Biological Themes Among Gene Clusters
- Automates the process of biological-term classification and enrichment analysis of gene clusters.
- Gene enrichment를 위한 툴은 많이 개발되어 있고 statistically significant category를 계산하는 것은 어렵지 않지만, enrichment analysis에서 흥미로운 결과를 직접 manually 찾는 과정이 매우 번거롭다는 문제점이 존재함...
- clusterProfiler -> **allows biological theme comparison among gene clusters**
- `enrichGO` or `enrichKEGG` : calculate enrichment test for GO terms and KEGG pathways based on hypergeometric distiribution.
 - 다른 ontology와의 association 분석도 쉽게 가능함 (ex. DO: Disease Ontology for human -> identification of clinical relavance)
- `compareCluster` : automatically calculate enriched functional categories of each gene clusters and provide methods for visualization..!

<img width="694" alt="image" src="https://user-images.githubusercontent.com/47490862/207292336-1294f458-846e-422b-b248-a531b87cccdd.png">

### Further Plans for Package Development
1. Use semantic similarity among KEGG / GO terms to aggregate closely related categories. -> *What I Expected!!*
2. Rank gene similarities in each cluster and correlate them to search for enriched categories (more sensibility in finding gene modules)
3. Through acylic graph, compare functional profiles as a whole rather than a set of unrelated categories.

Link for this updates : https://yulab-smu.top/biomedical-knowledge-mining-book/enrichplot.html
