# https://www.acmicpc.net/problem/1110

import sys

sys.stdin=open("python\백준\input.txt","rt")
num = int(sys.stdin.readline())
answer = 1
new_num = num
while True:
    if new_num < 10:
        new_num = f'0{new_num}'
    A,B = list(str(new_num))
    new_num = int(f'{B}{(int(A)+int(B))%10}')
    if num == new_num:
        print(answer)
        break
    answer += 1
