import sys
input = sys.stdin.readline

N, X = input().split()
grade = {'A+':450, 'A0':400, 'B+':350, 'B0':300, 'C+':250, 'C0':200, 'D+':150, 'D0':100, 'F':0}
score, num = 0, 0
for _ in range(int(N)-1):
    c, g = input().split()
    C = int(c)
    num += C
    score += C*grade[g]

L = int(input())
num += L
A, B = map(int, X.split('.'))
X = A*100+B

if score//num > X:
    print('F')
elif (score+L*100)//num > X:
    print('D0')
elif (score+L*150)//num > X:
    print('D+')
elif (score+L*200)//num > X:
    print('C0')
elif (score+L*250)//num > X:
    print('C+')
elif (score+L*300)//num > X:
    print('B0')
elif (score+L*350)//num > X:
    print('B+')
elif (score+L*400)//num > X:
    print('A0')
elif (score+L*450)//num > X:
    print('A+')
else: print('impossible')