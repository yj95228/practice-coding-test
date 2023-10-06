from sys import stdin
stdin = open('input.txt','r')
input = stdin.readline

N, M = map(int, input().split())
J = int(input())
left, right = 1, M
answer = 0
for _ in range(J):
    x = int(input())
    if left <= x <= right:
        continue
    elif x < left:
        answer += left-x
        left, right = x, x+M-1
    else:
        answer += x-right
        left, right = x-M+1, x
print(answer)