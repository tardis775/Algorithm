# ICPC Bangkok Regional에 참가하기 위해 수완나품 국제공항에 막 도착한 팀 레드시프트 일행은 눈을 믿을 수 없었다. 
# 공항의 대형 스크린에 올해가 2562년이라고 적혀 있던 것이었다.

# 불교 국가인 태국은 불멸기원(佛滅紀元), 즉 석가모니가 열반한 해를 기준으로 연도를 세는 불기를 사용한다. 
# 반면, 우리나라는 서기 연도를 사용하고 있다. 
# 불기 연도가 주어질 때 이를 서기 연도로 바꿔 주는 프로그램을 작성하시오.

while True:

    print("서기 : 0, 불기 : 1")

    year_type = input("연도 타입을 입력해 주세요")
    year_type = int(year_type)

    year = input("연도를 입력해 주세요")
    year = int(year)

    if year_type == 0 :
        year -= 543
        print("불기 ", year, "입니다.")
        
    else : 
        year += 543 
        print("서기 ", year, "입니다.")