# https://www.acmicpc.net/problem/2559
import sys
sys.stdin=open("input.txt", "rt")
input = sys.stdin.readline
N, K = map(int, input().split())
arr = list(map(int, input().split()))
answer = sm = sum(arr[:K])
for i in range(N-K):
    sm = sm - arr[i] + arr[i+K]
    answer = max(answer, sm)
print(answer)