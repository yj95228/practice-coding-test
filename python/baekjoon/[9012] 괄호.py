# https://www.acmicpc.net/problem/9012
import sys

sys.stdin=open("input.txt", "rt")
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    stack = []
    for x in input().strip():
        if x == '(':
            stack.append(x)
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        print('NO' if stack else 'YES')