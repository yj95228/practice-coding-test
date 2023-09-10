# https://www.acmicpc.net/problem/29729
import sys
input = sys.stdin.readline

S, N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N+M)]
answer, result = 0, 0
for x in arr:
    if x == '1':
        result += 1
        answer = max(answer, result)
    else:
        result -= 1
pow_arr = [0] + [S*2**x for x in range(20)]
for x in range(20):
    if pow_arr[x] < answer <= pow_arr[x+1]:
        print(pow_arr[x+1])
        break