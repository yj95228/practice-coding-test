# https://www.acmicpc.net/problem/18870
import sys

sys.stdin = open('input.txt','r')
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
S = sorted(set(arr))
obj = {}
answer = []
for i, x in enumerate(S):
    obj[x] = i
for x in arr:
    answer.append(obj[x])
print(*answer)