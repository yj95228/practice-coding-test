# https://www.acmicpc.net/problem/11399

import sys
from functools import reduce

sys.stdin=open("python\백준\input.txt","rt")
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = 0
for i in range(len(arr)):
    answer += reduce(lambda x,y: x+y, arr[:i+1])
print(answer)