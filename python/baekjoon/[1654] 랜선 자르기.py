import sys
input = sys.stdin.readline

def solve(length):
    cnt = 0
    for x in arr:
        cnt += x//length
    return cnt >= N

K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]
left, right = 1, max(arr)
answer = 0
while left <= right:
    mid = (left+right)//2
    if solve(mid):
        answer = max(answer, mid)
        left = mid+1
    else:
        right = mid-1
print(answer)