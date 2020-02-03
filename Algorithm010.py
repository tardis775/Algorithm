# 버블 정렬
# 버블 정렬은 오른쪽에서 왼쪽으로 정렬을 한다.

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

#region 오른쪽에서 왼쪽
# for i in range(0, len(score)):
#     for j in range(len(score)-1, i, -1):
#         if score[j-1] > score[j]:
#             score[j-1], score[j] = score[j], score[j-1] #자리바꿈
#         print(score)   #변환과정 출력
#endregion

#region 왼쪽에서 오른쪽
# for i in range(len(score)-1, 0, -1):
#     for j in range(0, i):
#         if score[j] > score[j+1]:
#             score[j], score[j+1] = score[j+1], score[j]
#         print(score)   #변환과정 출력
#endregion

#오른쪽부터 함수정의
def right(score):
    for i in range(0, len(score)):
        for j in range(len(score)-1, i, -1):
            if score[j-1] > score[j]:
                score[j-1], score[j] = score[j], score[j-1]
    return score

#왼쪽부터 함수정의
def left(score):
    for i in range(len(score)-1, 0, -1):
        for j in range(0, i):
            if score[j] > score[j+1]:
                score[j], score[j+1] = score[j+1], score[j]
    return score

print(right(score))
#print(left(score))