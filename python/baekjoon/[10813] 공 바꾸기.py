# https://www.acmicpc.net/problem/10813

import sys

sys.stdin=open("python\백준\input.txt","rt")
input = sys.stdin.readline

N, M = map(int, input().split())
ls = [i+1 for i in range(N)]
for _ in range(M):
    i, j = map(int, input().split())
    ls[j-1], ls[i-1] = ls[i-1], ls[j-1]
print(' '.join(map(str,ls)))