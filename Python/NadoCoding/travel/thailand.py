class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")

if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행할 때만 출력되는 문장입니다.")
    trip_to = ThailandPackage()
    trip_to.detail()

else:
    print("Thailand 외부에서 모듈이 호출되었습니다.")