# Running cellranger count

- **cellranger** **count** : align sequencin greads in FASTQ file to a reference transcriptome and generate `.cloupe` file for analysis in Loupe Browser. Quantifies single cell gene expression.

1) Make a directory to run the anlaysis in.

2) download FASTQ files -> `.fastq.gz` type.

- **Chromium033_S5_L002_I1_001.fastq.gz**
 - Chromium033 : sample name, library Lane : L00X.

3) Need a reference transcriptome.
 -> 설치중 (mouse reference dataset) - 용량 너무 커서 서버에!
 -> 동시에 cellranger software도 함께 설치 중!

4) FASTQ file과 reference 준비되었으면 `cellranger count` 실행
 
```
cellranger count --id=ID \
                 --fastqs=PATH \
                 --sample=PREFIX \
                 --transcriptome=DIR \
                 ...
```

- `--id` : any string. 이름을 내가 설정해서 넣으면 Ok. output 하위 디렉토리의 이름으로 사용됨.
- `--fastqs` : path to the directory containing FASTQ file.
- `--sample` : path 내에 한개 이상의 sample 있을 때 분석할 sample을 specify.
- `--transcriptome` : transcriptome reference로의 경로.
- `--expect-cells` : Expected number of recovered cells.
- `--force-cells` : Force pipeline to use this number of cells, bypassing the cell detection algorithm. 
- `--localcores` : specify a different number of cores to use
- `--localmem` : restrict the amount of memory (in GB) used by cellranger.
