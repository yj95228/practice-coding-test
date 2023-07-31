# https://www.acmicpc.net/problem/1018
import sys

sys.stdin=open("input.txt", "rt")
input = sys.stdin.readline
N = int(input())
stack = []
for _ in range(N):
    x = int(input())
    if x:
        stack.append(x)
    else:
        stack.pop()
print(sum(stack))