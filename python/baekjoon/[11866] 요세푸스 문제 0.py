# https://www.acmicpc.net/problem/11866
import sys
sys.stdin=open("input.txt", "rt")
input = sys.stdin.readline
N, K = map(int, input().split())
arr = [i+1 for i in range(N)]
i = -1
answer = []
for _ in range(N):
    for _ in range(K):
        i += 1
        if i >= len(arr):
            i -= len(arr)
    answer.append(arr.pop(i))
    i -= 1
print(f'<{", ".join(map(str,answer))}>')