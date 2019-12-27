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
z = 0
num = random.randint(1,9)

for r in range(3):
    while num in score:
        num = random.randint(1,9)
    score.append(num)

print("3자리의 정수를 생성했습니다.")
print(score)

while True:
    num2 = input("숫자를 입력해 주세요. : ").split()
    for i in score:
        if score[z] == num2[z]:
            s += 1 
        else : b += 1
        z += 1

    print(s,"스트라이크 ",b,"볼 입니다.",z)
    
    s = 0
    b = 0
    z = 0
    num2 = []
