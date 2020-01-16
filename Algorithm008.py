#문제
# JOI는 물리, 화학, 생물, 지구과학, 역사, 지리 총 6 과목의 시험을 봤다. 각 시험의 만점은 100점이다.
# JOI는 물리, 화학, 생물, 지구과학 4과목 중에서 3 과목을 선택하고 역사, 지리 2 과목 중에서 한 과목을 선택한다.
# 시험 점수의 합이 가장 높게 나오도록 과목을 선택할 때, JOI가 선택한 과목의 시험 점수의 합을 구하시오.

#입력
# 입력은 6행으로 되어있으며, 각 행에 1개의 정수가 주어진다.
# 1행에는 JOI의 물리 시험의 점수 A가 주어진다.
# 2행에는 JOI의 화학 시험의 점수 B가 주어진다.
# 3행에는 JOI의 생물 시험의 점수 C가 주어진다.
# 4행에는 JOI의 지구과학의 시험 점수 D가 주어진다.
# 5행에는 JOI의 역사 시험의 점수 E가 주어진다
# 6행에는 JOI의 지리 시험의 점수 F가 주어진다.
# 입력한 정수 A, B, C, D, E, F는 모두 0이상 100이하이다.

#출력
# JOI가 선택한 과목의 총 점수를 1행에 출력하시오.

Physics = input("물리점수를 입력하시오.     : ")
Chemistry = input("화학점수를 입력하시오.     : ")
Biology = input("생물점수를 입력하시오.     : ")
EarthScience = input("지구과학점수를 입력하시오. : ")
History = input("역사점수를 입력하시오.     : ")
Geography = input("지리점수를 입력하시오.     : ")

Science = [Physics, Chemistry, Biology, EarthScience]
Society = [History, Geography]

Science = list(map(int, Science))
Society = list(map(int, Society))

#선택정력 값을 직접 비교
sum = 0
count1 = 0
count2 = 0
Science_temp = Science[count1]
for i in Science:
    for j in Science:
        if len(Science) == count2:
            break
        if Science[count1] < Science[count2]:
            Science_temp = Science[count2]
            Science[count2] = Science[count1]
            Science[count1] = Science_temp
        count2 += 1    
    count1 += 1
    count2 = count1
    
count1 = 0
count2 = 0
Society_temp = Society[count1]
for i in Society:
    for j in Society:
        if len(Society) == count2:
            break
        if Society[count1] < Society[count2]:
            Society_temp = Society[count2]
            Society[count2] = Society[count1]
            Society[count1] = Society_temp
        count2 += 1    
    count1 += 1
    count2 = count1

del Science[len(Science)-1]
del Society[len(Society)-1]

count = 0
for i in Science:
    sum += Science[count]
    count += 1
count = 0
for i in Society:
    sum += Society[count]
    count += 1

print(sum)