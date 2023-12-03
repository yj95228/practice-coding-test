import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
answer = 0
now = arr[0]
for i in range(1, N):
    if arr[i][0] <= now[1]:
        answer += 1
        now = min(now, arr[i], key=lambda x: x[1])
    else:
        now = arr[i]
print(answer)