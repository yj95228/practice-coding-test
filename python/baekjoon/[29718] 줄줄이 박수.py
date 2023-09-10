# https://www.acmicpc.net/problem/29718
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
A = int(input())
arr = list(map(lambda x: sum(x), zip(*matrix)))
result = sum(arr[:A])
answer = result
for x in range(M-A):
    result += arr[x+A] - arr[x]
    answer = max(answer, result)
print(answer)