# https://www.acmicpc.net/problem/11050
import sys

sys.stdin = open('input.txt','rt')
input = sys.stdin.readline

N, K = map(int, input().split())
K = min(K, N-K)
if K == 0:
    print(1)
else:
    answer = N
    for x in range(1,K):
        answer *= (N-x)/(x+1)
    print(int(answer))