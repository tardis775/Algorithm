"각자 서로 다른 1~9까지 3자리 임의의 숫자를 정한 뒤 서로에게 3자리의 숫자를 불러서 결과를 확인합니다. "
"그리고 그 결과를 토대로 상대가 정한 숫자를 예상한 뒤 맞힙니다."

# 숫자는 맞지만, 위치가 틀렸을 때는 볼
# 숫자와 위치가 모두 맞을 때는 스트라이크
# 숫자와 위치가 모두 틀렸을 때는 아웃


import random

num2 = []
score = []
s = 0
b = 0
x = 0
num = random.randint(1,9)

for r in range(3):
    while num in score:
        num = random.randint(1,9)
    score.append(num)

print("3자리의 정수를 생성했습니다.")
print(score)

while True:
    num2 = input("숫자를 입력해 주세요. : ").split()
    num2 = list(map(int, num2))   # 문자열 리스트 int형태로 변환

    for i in score: # 스트라이크 카운트 업 
        if score[x] == num2[x]: 
            s += 1 
        else :
            y = 0
            for i in score:  # 볼 카운트 업
                if score[x] == num2[y]: 
                    b += 1  
                y += 1
        x += 1

    if s == 3:
        print(s,"스트라이크 정답입니다.")
        break
    elif s == 0 and b == 0:
        print("OUT 입니다.")
    else :
        print(s,"스트라이크 ",b,"볼 입니다.",x,y)
    
    s = 0
    b = 0
    x = 0
    num2 = []
