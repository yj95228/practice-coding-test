# https://www.acmicpc.net/problem/27918

import sys

sys.stdin=open("python\백준\input.txt","rt")
input = sys.stdin.readline
N = int(input())
score = {'D':0, 'P':0}
for _ in range(N):
    win = input().strip()
    score[win] += 1
    if score['D'] - score['P'] >= 2 or score['P'] - score['D'] >= 2:
        break
print(f"{score['D']}:{score['P']}")