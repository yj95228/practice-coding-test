from collections import deque

def recur(n, d, dd):
    if dd <= 0 and 0 <= n-1 and arr[n-1][2] != arr[n][6]:
        recur(n-1, -d, -1)
    if dd >= 0 and n+1 < 4 and arr[n][2] != arr[n+1][6]:
        recur(n+1, -d, 1)
    arr[n].rotate(d)

arr = [deque(map(int, input().rstrip())) for _ in range(4)]
K = int(input())
for _ in range(K):
    n, d = map(int, input().split())
    recur(n-1, d, 0)

answer = 0
for i, x in enumerate(arr, start=0):
    answer += 2**i*x[0]
print(answer)