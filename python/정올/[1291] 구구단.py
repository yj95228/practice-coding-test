# https://www.jungol.co.kr/problem/1291

s, e = map(int, input().split())
while not (1 < s < 10 and 1 < e < 10):
    print('INPUT ERROR!')
    s, e = map(int, input().split())
else:
    list = [i for i in range(s,e+1,1)] if s < e else [i for i in range(s,e-1,-1)]
    for i in range(9):
        for j in list:
            print(f'{j} * {i+1} = {j*(i+1):2d}', end='   ')
        print()