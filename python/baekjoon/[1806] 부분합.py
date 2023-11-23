import sys

input = sys.stdin.readline

N, S = map(int, input().split())
arr = [0] + list(map(int, input().split()))
for i in range(N):
    arr[i + 1] += arr[i]

answer = N + 1
left, right = 0, 1
while left < right:
    sm = arr[right] - arr[left]
    if sm < S:
        if right == N: break
        right += 1
    else:
        answer = min(answer, right - left)
        left += 1
print(0 if answer == N + 1 else answer)