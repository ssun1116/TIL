# About GSEA.
Gene Set Enrichment Analysis (or pathway analysis) is to statistically evaluate association of genes with pathways.
GSEA 분석 결과는 pathway에서 clue를 얻고 가설을 세우는 "시작점"이 되어야 한다. 결론이 아닐 수 있으며, 보조도구라는 점을 기억하자!
1. Non-parametric test
2. Rank-based test

## Non-parametric test (Threshold-dependent)
<img width="1019" alt="image" src="https://user-images.githubusercontent.com/47490862/201523873-f0913661-c477-48f2-bd88-f29657726955.png">

- Statistical model : Fisher's exact test. Result : OR, p-value
- Pathway와 overlapped gene이 random sampling에 의해 overlap되는 것보다 유의하게 크게 나타나는지!
 - Fisher test -> 사실 random sampling은 아님, based on theoretical null-hypothesis distribution (hypergeometric distribution)
- p-value depends only on the single gene-set performance, and FDR depends on the performance of all gene-sets.
- Main package : GSVA, gProfileR

> The most naive approach to GSEA is to use a one-sided Fisher’s exact test, also known as hypergeometric test, to determine the significance of over-representation of a gene set in the input list. The drawback of this method is that it requires a clear-cut boundary between included and excluded genes. This distinction may be clear in the case of qualitative experiments such as certain types of proteomics analyses or computational hard clustering analyses. In contrast, other types of analyses, such as most transcriptomics experiments, return a list of p-values associated with each gene. These p-values express the significance that a gene is differentially expressed between different conditions. Defining a boundary between differentially expressed genes (DEGs) and non-DEGs then relies on applying an arbitrary p-value cutoff. Pan et al. have shown that the choice of this cutoff dramatically influences the outcome of a GSEA. As a result, there has been a move away from using hypergeometric methods in favor of other approaches. 


## Rank-based test (Whole-distribution)
<img width="1035" alt="image" src="https://user-images.githubusercontent.com/47490862/201523813-aa47c54d-9fa2-485e-b4df-b2853e0e5d0c.png">

- DE 분석 결과 log fold change 기준으로 정렬해서 input으로 사용
- Pathway gene들이 rank 상에서 무작위로 분포할 것이라는 귀무가설을 적용 -> Pathway gene들이 한 쪽에 몰리면 귀무가설을 reject!
- GSEA tool -> rank-based.
- Whole-distribution methods have been shown to be more stable and stiatistically powerful.
 - No "natural value" for threshold, Different results at different threshodl settings, loss of information due to threshodling.
 - So, **Use whole-distribution whenever possible**
- Main package : FGSEA

> To run GSEA, you have your list of genes (L) and two conditions (or more), i.e. a microarray with normal and tumor samples. the first thing that GSEA does is to rank the genes in L based on "how well they divide the conditions" using the probe intensity values. at this point you have a list L ranked from 1...n. Now you want to see whether the genes present in a gene set (S) are at the top or at the bottom of your list...or if they are just spread around randomly. to do that GSEA calculates the famous enrichment score, that becomes normalized enrichment score (NES) when correcting for multiple testing (FDR).
- Positive NES will indicate that genes in set S will be mostly represented at the top of the provided gene list L.
- Negative NES will indicate that the genes in the set S will be mostly at the bottom of the provided gene list L.

# Gene-Set
1. Gene ontology (GO) databse
- Hierarchically-structured. General for all species.
- Has three independent partitions : Molecular Function, Cellular Component, Biological Process
- Gene ontology 관련 review들 읽어보면 좋음! (Jesse Gillis - Guilt by association..)
- Target predictions may be unreliable, and gene expression-derived sets are often hard to interpret.
2. KEGG
3. PFAM (Protein families / domains)
4. MsigDB
5. Reactome
