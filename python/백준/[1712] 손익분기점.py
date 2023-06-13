# https://www.acmicpc.net/problem/1712

import sys

sys.stdin=open("python\백준\input.txt","rt")
input = sys.stdin.readline
A, B, C = (map(int,input().split()))
if B == C or A/(C-B) < 0:
    print(-1)
else:
    print(int(A/(C-B))+1)