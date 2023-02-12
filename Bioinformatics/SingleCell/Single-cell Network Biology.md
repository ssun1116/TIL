
## GENIE3 (GEne Network Inference with Ensemble of trees)
- Statistical approach가 아닌 machine learning approach.
- 여러 tree를 만들고 decision을 모아서 최종 모델을 만드는 것 (Random forest 방법)
- 무엇을 learning? 특정 유전자 variance를 가장 잘 설명하는 유전자 (correlation을 가질 확률이 높음)
- 통계적으로 robust한 correlation은 아니더라도, 하나의 expression variance를 다른 expression variance가 잘 설명한다면, 두 유전자 간의 correlation으로 regulatory 관계성을 규정할 수 있다?
- Feature selection problem과  
- 통계적으로 robust한 correlation은 아니더라도, 하나의 expression variance를 다른 expression variance가 잘 설명한다면, 두 유전자 간의 correlation으로 regulatory 관계성을 규정할 수 있다?동일하다. 
- 통계적으로 robust한 correlation은 아니더라도, 하나의 expression variance를 다른 expression variance가 잘 설명한다면, 두 유전자 간의 correlation으로 regulatory 관계성을 규정할 수 있다? 가장 잘 설명하는 유전자들의 rank를 매기고 종합해서 => interaction ranking. 이것이 곧 network score order가 된다...
- **Ensemble Learning** : weak model을 많이 만들어서 (individual trees) 종합해서 강력한 final model을 (forest) 만드는 것. 크게 두 learning type이 있음 : *Bagging*, *Boosting*
- Random Forest -> Bagging 방법에서 가장 popular하게 사용되는...

## GRNBoost
- gradient-boosting machine. 개념상으로는 GENIE3랑 비슷하게 learning하는 방법이 다름. 
- 마찬가지로 tree를 사용하는데, stump라고 불리는 tree를 base learner로 사용 (그루터기) : depth가 1. 
- GENIE3에 비해 빠르고 scalable. Bagging이랑은 다르다 => boosting은 learning을 한 결과를 본 다음 다시 learning하고 결과를 본 다음 다시 learning하고. 종합하는 것이 아님. **bagging은 parellel, boosting은 sequential.**
- Gradient Boosting Machine : gradient descent algorithm을 사용. Gradient Descent + Boosting.
	- Gradient Descent : 경사하강법. error를 최소화하는 최적의 parameter를 찾기 위해 Mean squared error (MSE) loss function을 사용. Local minimum에 빠지는 것을 방지하기 위해 stochastic gradient descent를 사용.

## Preprocessing
- *Imputation* : Network inference에 imputation이 도움이 되는가? (scRNA-seq data : zero-inflated)
	- Correlation이 좋아지긴 하는데, benchmarking해보면 false-positive가 많다. SAVER라는 imputation 방법이 가장 performance가 좋다고 알려지긴 했는데, **가능한 한 imputation을 하지 않는 것이 좋다. 꼭 필요한 경우에만 사용하는 것이 좋음.**
- *Transformation* : bigScale method. 1차로 preprocess해서 matrix를 만든 뒤 clustering하고 그 안에서 cell들끼리의 pairwise relation 갖고 numerical model을 제작. 그 뒤에 differential expression analysis, z-score로 network inference.
	- Cluster끼리 DE analysis -> 정규분포화해서 z-score 변환. 

## Gene/Protein Networks
1.  Network Connectivity : Hub genes tend to be functionally more important
2.  Netowork propagation : Genes connected in the interactome. Neighboring gene의 정보를 가지고 잘 모르는 gene을 characterize.
3. Subnetwork analysis : Functional module -> tightly connected subnetwork를 이룬다.

## Hypothesis in single-cell network biology
- Dynamic하고, context-specific, cell-type specific한 network를 만들어서 다양한 스토리가 가능하다.
1. Hypoethesis from subnetwork (co-expression module or regulon)
- Co-expression modules (WGCNA)
- Regulon activity of cell states (SCENIC)
2. Hypothesis from network topology analysis
- Changes in Centrality -> 서로 다른 cell type / state에서 같은 유전자가 다른 centrality를 가지는 것. 유전자의 상대적인 중요성이 상황에 따라 바뀌는 것.
- Changes in Neighbors (Targets) -> 상황에 따라 target하는 유전자가 바뀜. 
3. Hypothesis from genotype-network association
- Co-expression QTL

## Hypothesis from subnetwork analysis
1. WGCNA
- 각각의 모듈을 봤을 때 특정 모듈에 대해 module activity가 state별로 다른 경우 -> 이 모듈이 hyper active해지면서 특정 질환이 생겼구나 하는 스토리를 만들 수 있다. 특정 모듈이 disease state에서 activity가 올라가고 내려가는 것을 보고 특정 질환과 특정 cell type이 어떻게 연관성을 갖는지 스토리를 얻을 수 있다. 또한 특정 key regulator를 찾아서 동물 실험 등으로 validation하는 것도 가능하다.
- 모듈로 development state를 설명하는 것도 가능 : 시간이 지나가면서 acitivty가 올라가는 module도 있고, 내려가는 module도 있고.. 등등! module이 발생 과정에서 어떻게 기능하는지를 알아보는 데 분석을 사용할 수도 있겠다.
2. SCENIC 
- Regulon activity analysis. 특정 regulon이 특정 disease state에서 올라가고 내려갔다면 이 regulon이 disease state에서 중요한 기능을 하는 것. 그러면 이 TF가 key가 될 수 있고 이걸로 followup study를 하는 것이 가능하다!
- RcisTarget algorithm을 사용해서 DNA binding data로부터 나온 binding motif를 가지고 filtering을 해서 보다 정확한 regulon을 찾는 데 improvement를 만들었음.
- DNA binding motif 정보를 가지고 보다 정확한 link를 찾아서 regulon을 한번 정리한 다음, 여기서 찾은 regulon을 가지고 regulon gene에 대한 rank를 매겨서 AUCell score를 부여. 

## Hypothesis from Network Topology analysis
- State에 따라 cell을 나눠서 netowork를 만들면 -> topogly가 state에 따라 다를 수 있음.
	- State에 의해 centrality, neighbor, modularity가 바뀔 수 있다.
- Trajectory에서 특정 branch에 있는 cell들끼리 network를 만들어 볼 수도 있을 것. 두 branch 사이에 어떤 차이가 있는지로 story를 만들어볼 수도 있을 것이다.
