## Loading

```
options(stringsAsFactors = F)
library(DESeq2)
library(ggplot2)
library(WGCNA)
library(cowplot)
library(igraph)
library(gProfileR)
library(ggnetwork)
library(tidyverse)
source('~/Dropbox/NGR_SNU_2019/wgcna_t_cell_201912/function_wgcna.R')

## Load datasets
load('data_express_20191205.RData')

## WGCNA
e = td3$e
g = td3$g
s = td3$s
```
- `td1$e` : 메인이 되는 data frame.
- `td1$s` : `sample` 에 대한 정보들.
- `td1$g` : `gene` 에 대한 정보들 (`March`: 3월 아님. gene 이름)

## goodSamplesGenes
 
```
gsg = goodSamplesGenes(t(e), verbose = 5)
gsg$allOK
table(gsg$goodGenes)
table(gsg$goodSamples)
```
- `goodSampleGenes()` : flagging genes, samples with too many missing values를 탐색해서 제거. 사용에 적절하지 않은 데이터 제거하기.
 - `t()` : 행, 열 전환
 - `verbose` : 장황한 레벨. 0이면 silent, 클수록 verbose.

```
e1 = e[gsg$goodGenes==TRUE, gsg$goodSamples == TRUE]
g1 = g[g$gene_name %in% rownames(e1), , drop=F]
```
- 실행 결과가 TRUE인 Genes, Samples만 추출해 새로운 dataframe 생성

## Determine soft power threshold

```
## Set the outtag
date = 20191205
outtag = paste('norm', date, 'All', 'sft_0.8_meank_50', sep = '_')
```
- outtag : scale free topology model fit은 0.8, mean connectivity 는 50을 충족시키는 **lowest power**를 `determineSoftPower()`로 choose하는 기준 설정.

```
## Determine soft power cutoff for WGCNA
e1$D0_Naive_1 <- NULL
e1$D0_Naive_2 <- NULL
```
- T cell은 differentiation 과정에 따라 **naive, effector, memory T cell**이 존재하며, 공격성을 띄기 전인 initial state가 naive T cell이다. 
 - 자극 받으면 effector, memory T cell로 분화

```
s = s[s$id %in% colnames(e1), ]
e2 = e1
```
- s에 있던 Naive row가 제거됨 : e1의 naive가 NULL로 변경되면서 삭제되었기 때문!
- 이후 dataframe 이름을 `e2`로 변경 (사실상 `e1`과 `e2`는 같은 데이터이다)

```
type <- 'signed hybrid'
sft0 <- determineSoftPowerWGCNA(
   data1 = e2,
   outtag = outtag,
   sft1 = 1, sft2 = 20, sft_by = 2
)
sft <- sft0$fitIndices
```
- type으로 signed hybrid를 사용한 것이 기존 코드와의 차이점!
 - signed hybrid : signed와 크게 차이는 없으나, weighted와 unweighted network의 hybrid! correlation >= 0이면 similarity equals the correlation.
- 1부터 20까지 2 간격의 sequence를 power로 사용.

```
mean.k = 50
sft_cut = min(sft[sft.R.sq >= 0.75 & sft$mean.k. <= mean.k,]$Power)
print(paste('The sft cutoff for this analysis is', sft_cut, sep = ' ')
```
- 기준에 맞는 `min` 값을 `sft_cut`에 저장. soft thresholding power beta.

## *Q. What is a determineSoftPowerWGCNA function?*

Constructing a weighted gene network entails the choice of the **soft thresholding power** to which co-expression similarity is raised to calculate adjacency.

We should choose the soft thresholding power based on the criterion of approximate scale-free topology.

We choose a set of candidate powers(the function provides suitable default values), and the function returns a set of **network indices** that should be inspected.

```
determineSoftPowerWGCNA <- function(data1, outtag, sft1=2, sft2=20, sft_by=1){
  options(stringsAsFactors = FALSE)
  require(cowplot)
  require(ggplot2)
```

``` 
  # plot powers to work out soft-power 
  # Choose a set of soft-thresholding powers
  powers <- seq(from = sft1, to= sft2, by=sft_by)
```
- `sft1`부터 `sft2`까지, `sft_by`를 기준으로 sequence를 `power`에 저장

```
  # Call the network topology analysis function
  # enableWGCNAThreads(nThreads = 2)
  sft <- pickSoftThreshold(t(data1), powerVector=powers, networkType="signed", verbose=5)
  # disableWGCNAThreads()
```
- `pickSoftThreshold` : calculate weighted networks by interpreting data. The weighted networks are obtained by raising the similarity to the powers given in powerVector. 

``` 
  # Plot the results:
  p1 <- ggplot(sft$fitIndices, aes(Power, SFT.R.sq)) + 
    geom_point() + theme_minimal(base_size = 7) + 
    labs(title = 'Scale independence',
         x='Soft Threshold (power)', 
         y='Scale Free Topology Model Fit,signed R^2')
  p2 <- ggplot(sft$fitIndices, aes(Power, mean.k.)) + 
    geom_point() + theme_minimal(base_size = 7) +
    labs(title = 'Mean connectivity',
         x='Soft Threshold (power)', 
         y='Mean Connectivity')
  p <- plot_grid(p1, p2, labels = c('A', 'B'), ncol=2)
  save_plot(paste("Figures/plot.determineSoftPowerWGCNA", outtag,"pdf", sep='.'), 
            p,
            base_height = 2.5*1, 
            base_width = 5*1)
  
  # return
  return(sft)
}
```
- `determineSoftPowerWGCNA`는 `function_wgcna.R` 파일에서 정의된 함수
 - data1, outtag, sft1, sft2, sft_by 값을 argument로 받아서 sft 변수에 soft-threshold 값을 저장하고 return.
 - `softPowerThreshold()` 함수를 통해 scale-free topology fit index, mean connectivity가 기준을 충족시키는 lowest power를 알 수 있다.

## WGCNA parameter setting

```
## Set a run parameter for WGCNA
minModuleSize <- 150
deepSplit <- 4

outtag = paste('norm', date, 'All',
              sft_0.8_meank', mean.k, 
              'ModSize', minModuleSize,
              'ds', deepSplit,
              sep = '_')
```
- `minModuleSize`, `deepSplit`을 추가하여 WGCNA outtag 설정
- We prefer **large modules**, so we set the minimum module size relatively high.

## Generating adjacency and TOM similarity matrices

```
## adj matrix
adjacencyA1 <- WGCNA::adjacency(t(e2),
            power = sft_cut, type = type)
```
- calculate adjacency matrix. 
- **double colon** : WGCNA 패키지의 `adjacency` 함수 사용 specify.

```
TOMsim <- TOMsimilarity(adjacencyA1, TOMType="signed")
dissTOMA1 <- 1 - TOMsim
```
- **TOM** : Topological Overlap Matrix
 - transform the adjacency into TOM to **minimize noise and spurious associations**
 - calculate the corresponding dissimilarity
- dissTOMA1 : calculate the corresponding dissimilarity

```
geneTree = hclust(as.dist(dissTOMA1), method="average")

tree = cutreeHybrid(dendro = geneTree,
                    minClusterSize= minModuleSize,
                    pamStage=FALSE,
                    cutHeight = 0.999,
                    deepSplit= deepSplit,
                    distM= dissTOMA1 )

merged = mergeCloseModules(exprData= t(e2),
                           colors = tree$labels,
                           cutHeight=0.1,
                           verbose = 3)
```
- **hierarchical clustering of the genes based on TOM dissimilarity measure**
 - each leaf(short vertical line) corresponds to a **gene**, branches of densely interconnected : **highly co-expressed genes**
- 이렇게 하여 clustering 완료된 module 관련 데이터들이 만들어진다.

```
## Merge information into the data frame
res = setNames(as.data.frame(cbind(tree$labels, merged$colors)), c('Raw', 'Merged'))
rownames(res) <- rownames(e2)
res$gene_id <- rownames(res)
res = res[rownames(e2), ]
res$Merged_color = labels2colors(res$Merged)
sort(table(res$Merged_color))
length(unique(res$Merged_color))
```
- clustering 결과 만들어진 module number를 `res` 라는 dataframe에 새롭게 저장.
 - `tree`의 데이터, `merged`의 데이터, 기존 `e2` dataframe에 저장되어있던 gene id 등을 가져와서 하나의 dataframe안에 뭉쳐주기.
- 이후 label(숫자)로 저장된 데이터를 해당되는 color에 매칭! 이후 color 분포를 확인
- `unique`: 겹치지 않고 총 몇 가지의 색상이 나타나는지를 알 수 있다.

```
res$isTopHub <- ifelse(res$gene_id %in% chooseTopHubInEachModule(datExpr = t(e2), colorh = res$Merged_color, power = sft_cut), 1, 0)
```
- gene이 tophub gene인지 판별하여 맞으면 1, 아니면 0을 `isTopHub` column에 저장.
 - `chooseTopHubinEachModule` : returns the gene in each module with the highest connectivity

```
f_oriMat = paste('Tables/table.wgcna_original_module_genes', outtag, 'txt', sep='.')
write.table(res, f_oriMat, sep='\t', quote=F, col.names = NA, row.names = T)

f_me = paste('Tables/table.ME', outtag, 'txt', sep='.')
moddat = merged$newMEs
rownames(moddat) <- colnames(e2)
write.table(moddat, f_me, sep='\t', quote=F, col.names = NA, row.names = T)
```
- ME : **module eigengene**
- 만들어진 res data를 txt 형식으로 저장. merged의 `newMEs` column도 저장.

## kMEs
```
## Get KMEs for genes
kMEs <- signedKME(dataExpr = t(e2), datME = merged$newMEs)
c = as.data.frame(table(res$Merged, res$Merged_color))
c = c[c$Freq!=0, ]
rownames(c) <- paste('kME', as.character(c$Var1), sep = '')
colnames(kMEs) <- paste('kME', as.character(c[colnames(kMEs),]$Var2), sep = '')

kMEs$gene_id <- rownames(kMEs)
kMEs = merge(kMEs, res, by = 'gene_id')
write.table(kMEs, paste('Tables/table.kME', outtag, 'txt', sep='.'), 
            sep='\t', quote=F, col.names = NA, row.names = T)
```
- To correlating gene expression profile with module eigengene of given module. How gene is correlated to the specific module eigengene.
 - close to 0 : not part of the specific module
 - close to 1 or -1 : highly connected to specific module genes.
- `signedKME` : 각 gene data들을 module 별 20개의 kME와의 correlation을 계산한다. `dataExpr`은 expression data. e2에 저장된 데이터이고, `datME`는 module 별 eigengene. 
- dataframe `c`는 module number와 color를 저장해둔 참고용 데이터 느낌이고, 이후 `c`로부터 number matching color 데이터를 가져와서 `kMEs` dataframe의 column 이름을 color representing name으로 수정한다.
- 이후 `kMEs`의 rownames(gene id로 되어있음)를 column에 추가해주고 이 column을 연결점으로 `kMEs` dataframe과 `res` dataframe을 `merge`. 그리고 데이터를 txt 파일로 저장.

```
## Sample traits
## Update the colnames
res = read.delim(paste('Tables/table.wgcna_original_module_genes', outtag, 'txt', sep = '.'), row.names = 1)

## Run MDS on MEs
## Euclidean distance between the rows (transpose data first so that this runs correctly)
...
```
- MDS : multi dimensional scailing. cluster dendogram visualizing step.


### Further insights...

To identify highly connected genes or hub genes, the WGCNA package was used for calculating Eigengene-based module connectivity or module membership (kME) measures for a particular gene within a given non-preserved module. The module membership can be determined by the correlation between the expression profile of a gene and the module eigengene (or first principal component) of a module. This measure quantifies how close a gene is to a given module. Therefore, it can be applied to detect module hub genes, as genes with high module membership are labeled as intramodular hub genes. Hub genes are representative of the module’s overall function and have a high likelihood to be critical components within the module. This measure was used to identify hub genes of non-preserved modules associated with different states (NEM, MMES, and MSES), as genes whose |kME| was ≥0.7 were considered as hub genes to the respective module

kME = high modular membership.

First things first: grey is not really a module, it is a label for unassigned genes, and the eigengene and kME for the grey "module" are more or less meaningless. In other words, ignore the eigengene and kME values for the grey "module".

WGCNA assigns module labels using dynamic tree cut (look up dynmaicTreeCut) of hierarchical clustering tree that is based on the Toplogical Overlap Measure (TOM). TOM results in similar but not quite the same similarity as correlation, hence for some genes the assigned module may differ from the module with highest kME. Module merging can also play a part here.

Practically speaking, genes will have a high kME to their assigned module. When assigned module and module of highest kME differ, the gene probably has high kME to both and can be considered intermediate between the two modules.

https://support.bioconductor.org/p/84835/

