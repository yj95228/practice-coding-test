# https://www.acmicpc.net/problem/1018
import sys

sys.stdin=open("input.txt", "rt")
input = sys.stdin.readline
N, M = map(int, input().split())
dogam = []
for _ in range(N):
    dogam.append(input().strip())
for _ in range(M):
    pocketmon = input().strip()
    if pocketmon.isdigit():
        print(dogam[int(pocketmon)-1])
    else:
        print(dogam.index(pocketmon)+1)