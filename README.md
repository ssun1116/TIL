# Today I Learned

## git - 간편 안내서
- `git clone 사용자명@호스트:/원격/저장소/경로` : 원격 서버의 저장소를 Local에 복제.
- 로컬 저장소는 git이 관리하는 세 그루의 나무로 구성 -> 첫번째 나무인 작업 디렉토리(Working directory)는 실제 파일들로 이루어져있고, 두번째 나무인 인덱스(Index)는 준비 영역(staging area)의 역할을 하며, 마지막 나무인 HEAD는 최종 확정본(commit)을 나타낸다.
- working directory -> `git add <파일>` -> 변경된 파일이 index에 추가됨 ->`git commit -m "이번 확정본에 대한 설명"` -> 변경 내용이 확정되어 로컬 저장소의 HEAD에 반영됨 -> `git push origin master` -> 변경 내용을 원격 서버에 올림. remote git update! 원격 저장소에 변경 내용이 반영됨.

## GSEA - Points of Normalized Enrichment Score (NES)
So, to run GSEA you have your list of genes (L) and two conditions (or more), i.e. a microarray with normal and tumor samples. the first thing that GSEA does is to rank the genes in L based on "how well they divide the conditions" using the probe intensity values. at this point you have a list L ranked from 1...n.
Now you want to see whether the genes present in a gene set (S) are at the top or at the bottom of your list...or if they are just spread around randomly. to do that GSEA calculates the famous enrichment score, that becomes normalized enrichment score (NES) when correcting for multiple testing (FDR).
- Positive NES will indicate that genes in set S will be mostly represented at the top of the provided gene list L.
- Negative NES will indicate that the genes in the set S will be mostly at the bottom of the provided gene list L.

## IT Basic Information
서버와 데스크탑의 차이점 - https://m.post.naver.com/viewer/postView.naver?volumeNo=10335098&memberNo=2521903
서버 : 네트워크를 통해 클라이언트에게 정보를 제공하는 컴퓨터 시스템. CPU, Memory, Disk 등을 고려하게 된다.
 - CPU : 클럭 속도 (CPU가 초당 실행하는 cycle 수, 연산속도에 비례.) & Core 개수 (CPU의 뇌, 많을수록 multitasking이 가능) 를 고려
 - Memory : CPU가 처리해야 할, 혹은 처리한 데이터를 저장하는 공간. 많으면 많을수록, 용량이 클수록 좋음.
LAN : 근거리 통신망. Local Area Network. 네트워크 매체를 이용하여 가까운 지역을 묶는 컴퓨터 네트워크.
WAN : 광역 통신망. Wide Area Network. 서로 멀리 떨어진 지역의 네트워크를 연결. 네이버, 구글 등에 접속할 때 사용하는 네트워크.
IP와 MAC 주소 : 장비 간 데이터를 전송하기 위해 서로 통신하기 위한 주소
 - MAC 주소 : 전세계에서 유일한 하드웨어 물리적 주소. 제조업체에서 장비를 제작할 때 할당되며, 불가변적. 주민등록번호 같은 것.
 - IP 주소 : 네트워크 연결을 위해 제공되는 논리적 주소. 외부통신을 위해 사용, 집주소와 같은 것. 가변주소로, Wifi 다른거 쓰면 IP도 바뀐다.
 - Public IP는 전세계쩍으로 고유의 주소, 외부와 통신할 때 사용하는 internet. Private IP는 한정된 공간 내에서 통신하기 위한 특정 구역 내의 고유의 주소.
NAT (Network Address Translation) : Private IP <-> Public IP 통신할 때 각 구역에서 사용하는 IP로 변환하는 기술. 주소 변환 서비스.
Subnetting : 하나의 네트워크를 여러 대역으로 분할하는 것. IP 낭비를 줄일 수 있고, 보안 및 관리 측면에서 이점.
Routing : 네트워크 안에서 데이터를 보낼 때 최적의 경로를 선택하는 과정. 

## AWS
EC2 (AWS Elastic Compute Cloud) : AWS 클라우드에서 확장 가능 컴퓨팅 용량을 제공. 쉽게 확장, 축소 등의 재구성이 가능.
VPC (Virtual Private Cloud) : 사용자가 정의한 가상 네트워크 -> VPC를 사용하여 AWS 리소스를 시작할 수 있ㅇㅁ. 
Subnet : VPC의 IP 주소 범위. 지정된 서브넷으로 AWS 리소스를 시작할 수 있음. 
Routing table : 서브넷 또는 게이트웨이의 네트워크 트래픽이 전송되는 위치를 결정.
Internet gateway : VPC와 인터넷 간에 통신할 수 있게 해줌. 
