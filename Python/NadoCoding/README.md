## 내장함수 : import 없이 바로 사용가능한 함수.

### input : 사용자 입력을 받는 함수
```
langauge = input("무슨 언어를 좋아하세요?")
```

### dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
```
import random
print(dir(random)) # 랜덤 모듈 내에서 쓸 수 있는 함수들.
```

## 외장함수 : import를 통해서 사용 가능한 함수.
### glob : 경로 내의 폴더 / 파일 목록을 조회. 
```
import glob
print(glob.glob("*.py")) # 확장자가 py인 모든 파일
```

### os : 운영체제에서 제공하는 기본 기능
```
import os
print(os.getcwd()) # 현재 디렉토리 출력
print(os.listdir()) # 현 디렉토리의 파일 출력
```

### time : 시간 관련 함수
```
import time
print(time.localtime())
print(time.strftime("%y-%m-%d %H:%M:%S"))
```
