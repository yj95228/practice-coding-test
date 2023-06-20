# https://www.acmicpc.net/problem/14470

import sys

sys.stdin=open("python\백준\input.txt","rt")
input = sys.stdin.readline
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
if A < 0:
    print(-A*C+D+B*E)
else:
    print((B-A)*E)