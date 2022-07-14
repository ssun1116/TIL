# Today I Learned 📒

## 집사TV [CITE-seq을 통해 수용체의 세포 표면 발현량을 단일세포 단위에서 대량으로 정량해 봅시다]
- Link : https://www.youtube.com/watch?v=rA7Hqq52-Ug
- Fluorescence-activated cell sorting (FACS) : Surface receptor를 정량하는 전통적인 방법. Antibody 끝부분에 fluorophore를 붙여둠으로써, 특정 wavelength의 빛을 쬐였을 때 emission되는 signal를 정량하여 detect하는 방법, 즉 fluorescent antibody를 사용하는 방법. 
- CD8 / CD4를 target하는 FACS 분석을 통해 T cell이 분화해나갈 때, CD4-/CD8- (Double negative) -> CD4+/CD8+ (Double positive) -> CD4+ 혹은 CD8+ (Single positive)로 분화한다는 것을 발견할 수 있었음.
- 한계 : 수많은 surface marker 중 여러 개를 한번에 분석하고 싶을 때, fluorophore 시그널의 중복 + 다차원 데이터 시각화 문제로 인해 여러 receptor를 detect하기가 어려움.
- Fluorophore마다 emission되는 range가 넓기 때문에, 특정 범위에 속하는 fluorophore가 한 가지가 아님. 여러 개가 detect되어지게 되면서, 정확한 정량이 어렵다.
- 이러한 한계를 극복하기 위해, 항체에 fluorophore를 붙이는 게 아니라 barcode를 붙이는 방식이 바로 **Cite-seq**.
- Droplet level에서 PCR을 할 때 RNA와 barcode를 동시에 정량 (transcriptome 분석 + epitope 분석). 따라서 sscRNA-seq과 Antibody barcode analysis를 parallel하게 분석한다고 이해하면 됨. 세포가 갖고 있는 RNA와 surface protein을 함께 정량 가능하다.
- **Barcode : cell specific. Bead에 고유함, UMI : mRNA specific. mRNA에 고유함.**
- Barcode는 하나하나의 cell을 표시하므로, cell 내에 적정 수의 UMI가 들어가있어야 함. 따라서 Barcode와 UMI를 Compare함으로써 QCfmf gksek.
- Gene expression을 분석하는 최종 목표는 protein의 정량임. RNA-seq은 RNA expression과 Protein 발현간의 correlation이 높다고 가정하고 분석을 하는 것임.
- 그러나 실제로는 RNA, Protein의 correlation은 R^2 = 0.5~0.6 정도. RNA expression이 곧 protein expression을 100% 의미하는 것이 아님. 그러나 protein의 정량은 어렵고 비용이 매우 비싸기 때문에 가성비에 따라 RNA 분석을 하는 것인데, 궁극적으로는 결국 Protein을 보는 걸 목표로 한다. 현재 기술로는 200여개의 surface marker를 관찰 가능!

## git - 간편 안내서
- `git clone 사용자명@호스트:/원격/저장소/경로` : 원격 서버의 저장소를 Local에 복제.
- 로컬 저장소는 git이 관리하는 세 그루의 나무로 구성 -> 첫번째 나무인 작업 디렉토리(Working directory)는 실제 파일들로 이루어져있고, 두번째 나무인 인덱스(Index)는 준비 영역(staging area)의 역할을 하며, 마지막 나무인 HEAD는 최종 확정본(commit)을 나타낸다.
- working directory -> `git add <파일>` -> 변경된 파일이 index에 추가됨 ->`git commit -m "이번 확정본에 대한 설명"` -> 변경 내용이 확정되어 로컬 저장소의 HEAD에 반영됨 -> `git push origin master` -> 변경 내용을 원격 서버에 올림. remote git update! 원격 저장소에 변경 내용이 반영됨.

## edX Statistics and R (Rafael Irizarry)
- Notion에 정리중. Link : https://www.notion.so/Statistics-and-R-df761a6d4626401b8ca0e6a4fbcd9b00
