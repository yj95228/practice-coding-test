# https://www.acmicpc.net/problem/14470

import sys

sys.stdin=open("python\백준\input.txt","rt")
input = sys.stdin.readline
N = int(input())
score = list(map(int, input().split()))
print(sum(score)/N/max(score)*100)