## Basic Concepts
![image](https://user-images.githubusercontent.com/47490862/182034107-17a90d64-2356-4b8e-896d-b653baab94a0.png)

1. Introduction to RNA-Seq
2. FASTQ Files -> aligning RNA-seq read
3. Normalization of read counts (counting RNA-seq reads or fragments in genes)
4. Differential expression (count-based differential expression)

## 1. Introduction to RNA-Seq
- 기본 technology : RNA transcript -> cDNA로 convert -> fragment -> sequence it! Read가 만들어지면 genome에 mapping.
- 우리가 알고 싶은 것 : sample 내에 gene이 얼마나 있는가. Read가 얼마나 해당 gene에 mapping되었는가를 바탕으로 확인 가능. 즉, count를 다루는 것이다 (Poisson, negative bionomal.. DESeq, EdgeR)

<p align="center"><img width="389" alt="image" src="https://user-images.githubusercontent.com/47490862/182033868-58f6b74c-2450-4945-9a8d-1dbb7410ee69.png">

- *RNA-Seq Complication 1* :  RNA에는 intron이 spliced out되어서 exon만 존재하는 상태이다. 문제는 **junction**. Exon1과 exon2가 붙어있는 구간, 즉 mRNA spliced site 부근에 존재하는 read인 junction은 genome상에는 가운데에 intron이 들어가는 구간이기 때문에, 이 junction 파트의 sequence는 genome 상에는 존재하지 않는다. 따라서 genome에서는 junction sequence가 없어서 mapping이 될 수 없다.

<p align="center"><img width="397" alt="image" src="https://user-images.githubusercontent.com/47490862/182034235-e2adbcc2-bad6-4657-a672-bbb185183356.png">

- *RNA-Seq Complication 2* : A gene can have different **transcripts**. RNA splicing 과정에 따라 Exon 구성이 다양하게 만들어지기 때문. 따라서 RNA-seq 데이터를 볼 때는 different transcript를 measure, quantify transcript levels for different transcripts in same gene.
