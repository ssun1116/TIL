# Today I Learned

## git - 간편 안내서
- `git clone 사용자명@호스트:/원격/저장소/경로` : 원격 서버의 저장소를 Local에 복제.
- 로컬 저장소는 git이 관리하는 세 그루의 나무로 구성 -> 첫번째 나무인 작업 디렉토리(Working directory)는 실제 파일들로 이루어져있고, 두번째 나무인 인덱스(Index)는 준비 영역(staging area)의 역할을 하며, 마지막 나무인 HEAD는 최종 확정본(commit)을 나타낸다.
- working directory -> `git add <파일>` -> 변경된 파일이 index에 추가됨 ->`git commit -m "이번 확정본에 대한 설명"` -> 변경 내용이 확정되어 로컬 저장소의 HEAD에 반영됨 -> `git push origin master` -> 변경 내용을 원격 서버에 올림. remote git update! 원격 저장소에 변경 내용이 반영됨.

## 3분에 익히는 머신러닝의 기본 원리

## GSEA - Points of Normalized Enrichment Score (NES)
So, to run GSEA you have your list of genes (L) and two conditions (or more), i.e. a microarray with normal and tumor samples. the first thing that GSEA does is to rank the genes in L based on "how well they divide the conditions" using the probe intensity values. at this point you have a list L ranked from 1...n.
Now you want to see whether the genes present in a gene set (S) are at the top or at the bottom of your list...or if they are just spread around randomly. to do that GSEA calculates the famous enrichment score, that becomes normalized enrichment score (NES) when correcting for multiple testing (FDR).
- A positive NES will indicate that genes in set S will be mostly represented at the top of the provided gene list L.
- A negative NES will indicate that the genes in the set S will be mostly at the bottom of the provided gene list L.

서버와 데스크탑의 차이점 : https://m.post.naver.com/viewer/postView.naver?volumeNo=10335098&memberNo=2521903
