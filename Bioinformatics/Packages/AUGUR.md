**AUGUR : tool for prioritizing cell types most responsive to an experimental perturbation.** 

- Machine-learning based classifier training → rank cell types based on their separability.
    - Cell types that repond strongly to perturbation : become more separable in MDS space.
- 내가 기존에 perturbation을 평가해온 방식 : **based on the number of differentially expressed genes (DEGs) within each cell types**
    - Conduct DE test comparing preturbed / unpreturbed cells, tally the number o genes that pass a threshold for statistical significance → more DE genes, more responsive.
- Limitations 1: their bias toward cell types that are found with a higher relative abundance in the dataset. Larger number of cells → greater statistical power for identifying differences.
- Limitations 2: sparsity in single-cell dataset -> most highly expressed genes만 평가되고 나머지 80%에서 오는 signal은 사용되지 않는다.

AUGUR employs a repeated subsampling procedure that elminates bias toward more abundanct cell types, and incorporates information from the entire transcriptome.
- RNA velocity calculation에도 활용 가능하다고 한다! 
