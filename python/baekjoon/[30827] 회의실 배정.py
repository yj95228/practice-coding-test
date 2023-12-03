import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[1], x[0]))
answer, time = 0, [0]*K
for start, end in arr:
    idx, mx = -1, -1
    for i, t in enumerate(time):
        if t < start and mx < t:
            idx, mx = i, t
    if idx != -1:
        answer += 1
        time[idx] = end
print(answer)