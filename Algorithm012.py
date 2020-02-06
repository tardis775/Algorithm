'''
문제
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 
합을 나타낼 때는 수를 1개 이상 사용해야 한다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 
각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. 
n은 양수이며 11보다 작다.

출력
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.
'''
#input값 예외처리
def input_num():
    global num
    num = input("11미만의 정수를 입력하시오 : ")
    num = int(num)
    if 0 < num < 11:
        return num
    else:
        print("범위에 맞는 값을 입력해 주세요")
        input_num()
#정수받아오기
input_num()

SumKinds = []

#region m3(num) 3씩 빼기
def m3(num):
    if (num - 3) >= 0:
        num -= 3
    return num
#endregion
#region m2(num) 2씩 빼기
def m2(num):
    if (num - 2) >= 0:
        num -= 2
    return num
#endregion
#region m1(num) 1씩 빼기
def m1(num):
    if (num - 1) >= 0:
        num -= 1
    return num
#endregion

while True:
    if num>3:
        m3(num)
        SumKinds[0] = 3

    if num == 0:
        break


