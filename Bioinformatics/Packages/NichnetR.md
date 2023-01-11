- Paper link : https://www.nature.com/articles/s41592-019-0667-5
- Github link : https://github.com/saeyslab/nichenetr

![Untitled](https://user-images.githubusercontent.com/47490862/211726842-0e076e15-d1d2-43ca-86a9-0fd40add9301.png)

- The goal of NicheNet is to study intercellular communication from a computational perspective. NicheNet uses human or mouse gene expression data of interacting cells as input and combines this with a prior model that integrates existing knowledge on ligand-to-target signaling paths. This allows to predict ligand-receptor interactions that might drive gene expression changes in cells of interest.
- functional understanding of a cellular communication process also requires knowing how these inferred ligand-receptor interactions result in changes in the expression of downstream target genes within the receiver cells → **단순히 interaction 유추에서 끝나는 것이 아니라, downstream gene들의 expression change까지 고려해서 봐야 한다.**
    - Nichnet goes beyond ligand-receptor interactions and incorporates intracellular signaling and transcriptional regulation as well → predict which ligands influence the expression in another cell, which target genes are affected by each ligand and which signaling mediators may be involved.

![Untitled](https://user-images.githubusercontent.com/47490862/211726928-6cf75b7e-c9cd-49e4-962f-b07cf8fde0a2.png)
- 위의 그림이 existing CCC tool
- 아래 그림이 Nichenet. 차별화가 된다고 하는데, 과연 유의미한 결과가 얻어질지?
    - assessing how well ligands expressed by a sender cell can predict changes in gene expression in the receiver cell
        - Nichenetr의 가장 큰 특징은 receiver cell의 gene expression까지 고려한다는 점이다.
    - prioritizing ligands based on their effect on gene expression

- Nichnet requires **Defining the gene set of interest and a background of genes. As gene set of interest, we consider the genes of which the expression is possibly affected due to communication with other cells. The definition of this gene set depends on your research question and is a crucial step in the use of NicheNet.**
    - 이 부분을 어떻게 해야할지 고민이 되었는데…. 생각해보니 이렇게 하면 될것같다. 지금 내가 관심있는 건 Coghelp 샘플 내에서 CoghelpDC의 영향으로 인한 나머지 cell들의 변화 → 그러면 나머지 cell들의 변화는 Coghelp vs Helpess or Naive sample DEG를 살펴보면 되는 것!! Expression possibily affected due to communication → 상대적으로 Naive에 비해 Coghelp에서 up-regulate되어있는 gene들이겠지..!
- **Update**. 일단 어느정도 분석이 되는 걸 확인했고, target / sender 관계만 확실하면 흥미롭게 스토리 이어갈 수 있을지도 모름. 근데 일단 선행되어야하는 것은 coghelpDC의 lineage → GMCSF lineage와 FLT3 lineage 나누는걸 확실히 해야 sender receiver도 정리가 될 것 같음.

## Ligand Receptor Analysis using LIANA

- predict 1) which ligands from one or more cell population(s) (“sender/niche”) are most likely to affect target gene expression in an interacting cell population (“receiver/target”) and 2) which specific target genes are affected by which of these predicted ligands.
