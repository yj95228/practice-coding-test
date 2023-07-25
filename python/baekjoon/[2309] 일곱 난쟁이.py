# https://www.acmicpc.net/problem/2309
from itertools import combinations
import sys

sys.stdin=open("input.txt", "rt")
input = sys.stdin.readline
arr = []
for i in range(9):
    arr.append(int(input()))
for x in list(combinations(arr, 7)):
    if sum(x) == 100:
        for a in sorted(x):
            print(a)
        break