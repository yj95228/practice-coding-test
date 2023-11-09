import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
arr = list(map(int, input().split()))
arr.sort()
left, right = 0, N-1
answer = 0
while left < right:
    if arr[left]+arr[right] < M:
        left += 1
    elif arr[left]+arr[right] > M:
        right -= 1
    else:
        answer += 1
        left += 1
        right -= 1
print(answer)