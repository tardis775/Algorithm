# 별찍기
'''
입력 : 2
** **
 ***
** **

입력 : 5
*****       *****   = x + x-1 + x-2 + x
 *   *     *   *    = 
  *   *   *   *
   *   * *   *
    *   *   *
   *   * *   *
  *   *   *   *
 *   *     *   *
*****       *****
'''

print("N(2 ≤ N ≤ 100)")

star = input("숫자 N을 입력해 주세요 : ")
star = int(star)

for i in range(star):
    for j in range(star):
        if i == 0:
            print('*', end = '')
        elif i == j:
            print('*', end = '')
        else: print(' ', end = '')
    for j in range(star):
        if i == j:
            print('*', end = '')
        else: print(' ', end = '')
        
    for j in range(star-2, -1, -1):
        if i == j:
            print('*', end = '')
        else: print(' ', end = '')
    for j in range(star-1, -1, -1):
        if i == 0:
            print('*', end = '')
        elif i == j:
            print('*', end = '')
        else: print(' ', end = '')
    print('')
    

for i in range(star-1):
    for j in range(star-2, -1, -1):
        if i == 3:
            print('*', end = '')
        elif i == j:
            print('*', end = '')
        else: print(' ', end = '')
    for j in range(star, -1, -1):
        if i == j-1:
            print('*', end = '')
        else: print(' ', end = '')
    for j in range(star):
        if i == j:
            print('*', end = '')
        else: print(' ', end = '')
    for j in range(star-1):
        if i == 3:
            print('*', end = '')
        elif i == j:
            print('*', end = '')
        else: print(' ', end = '')
    print('')