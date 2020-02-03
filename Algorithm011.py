# 삽입 정렬

#region 랜덤함수 사용
#랜덤함수 호출
import random
score = []
num = random.randint(1,99)
#배열에 랜덤으로 숫자 채움
for r in range(5):
    while num in score:
        num = random.randint(1,99)  #랜덤 숫자 범위 설정
    score.append(num)
#endregion

#선택정렬 함수정의
def Selection(score):
    for i in range(1, len(score)):
        while 0 < i and score[i] < score[i - 1]: 
            score[i], score[
                i - 1] = score[i - 1], score[i]
            i -= 1
    return score

print(Selection(score))