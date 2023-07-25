# https://www.acmicpc.net/problem/2670
import sys

sys.stdin=open("input.txt", "rt")
input = sys.stdin.readline
N = int(input())
arr = [float(input()) for _ in range(N)]

# mx = lst[0]
# for i in range(1,len(lst)):
#     mx = max(lst[i-1]*lst[i],lst[i])
#     lst[i] = mx

answer = 0
mx = 1
for a in arr:
    if mx < 1.0:
        mx = a
    else:
        mx *= a
    answer = max(answer, mx)

# for i in range(N):
#     nx = 1
#     for j in range(i,N):
#         mx *= arr[j]
#         answer = max(answer, mx)
print(f'{answer:.3f}')