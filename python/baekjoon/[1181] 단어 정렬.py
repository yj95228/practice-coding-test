# https://www.acmicpc.net/problem/1181
import sys

sys.stdin = open('input.txt','rt')
input = sys.stdin.readline

N = int(input())
s = set()
for _ in range(N):
    s.add(input().strip())
for x in sorted(s, key=lambda x: (len(x), x)):
    print(x)