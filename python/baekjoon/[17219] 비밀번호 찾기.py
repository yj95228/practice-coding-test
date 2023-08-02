# https://www.acmicpc.net/problem/17219
import sys

sys.stdin=open("input.txt", "rt")
input = sys.stdin.readline
N, M = map(int, input().split())
obj = {}
for _ in range(N):
    site, pw = input().split()
    obj[site] = pw
for _ in range(M):
    print(obj[input().strip()])