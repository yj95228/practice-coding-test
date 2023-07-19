# https://www.acmicpc.net/problem/10810

import sys

sys.stdin=open("python\백준\input.txt","rt")
input = sys.stdin.readline

N, M = map(int, input().split())
answer = [i+1 for i in range(N)]
for _ in range(M):
    i, j = map(int, input().split())
    answer = answer[:i-1] + answer[i-1:j][::-1] + answer[j:]
print(' '.join(map(str,answer)))
