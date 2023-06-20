# https://www.acmicpc.net/problem/1764

import sys

sys.stdin=open("python\백준\input.txt","rt")
input = sys.stdin.readline
N,M = map(int, input().split())
not_listen = set([])
not_see = set([])
for i in range(N):
    not_listen.add(input().strip())
for i in range(M):
    not_see.add(input().strip())
intersect = sorted(not_listen & not_see)
print(len(intersect))
for i in intersect:
    print(i)