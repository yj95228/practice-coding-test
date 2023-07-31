# https://www.acmicpc.net/problem/17608
import sys

sys.stdin=open("input.txt", "rt")
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)][::-1]
stack = [arr[0]]
for i in range(1,len(arr)):
    if stack and stack[-1] < arr[i]:
        stack.append(arr[i])
print(len(stack))

# 강사님 코드
# while stack and stack[-1] <= x:
#     stack.pop()
# stack.append(x)