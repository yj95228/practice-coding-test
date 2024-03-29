# https://www.acmicpc.net/problem/10709
import sys

sys.stdin=open("input.txt", "rt")
input = sys.stdin.readline
N = int(input())
matrix = [[0 for _ in range(1001)] for _ in range(1001)]
for n in range(1,N+1):
    a,b,x,y = map(int, input().split())
    for i in range(x):
        for j in range(y):
            matrix[a+i][b+j] = n
for n in range(1,N+1):
    print(sum([x == n for row in matrix for x in row]))

# 두번째 풀이
cnt = [0]*N
for n in range(1,N+1):
    a,b,x,y = map(int, input().split())
    for i in range(x):
        for j in range(y):
            if matrix[a+i][b+j] > 0:
                cnt[matrix[a+i][b+j]-1] -= 1
            matrix[a+i][b+j] = n
            cnt[n-1] += 1
print(*cnt, sep='\n')