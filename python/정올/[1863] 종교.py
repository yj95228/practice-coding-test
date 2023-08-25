# https://jungol.co.kr/problem/1863
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def union(a,b):
    arr[find(b)] = find(a)

def find(x):
    while x != arr[x]:
        x = arr[x]
    return x

N, M = map(int, input().split())
arr = [x for x in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    union(i,j)
answer = 0
for i in range(1,N+1):
    if i == arr[i]:
        answer += 1
print(answer)
