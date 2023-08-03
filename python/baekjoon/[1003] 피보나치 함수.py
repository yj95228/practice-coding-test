# https://www.acmicpc.net/problem/1003
import sys

sys.stdin = open('input.txt','rt')
input = sys.stdin.readline

T = int(input())
arr = [1,1]
for _ in range(T):
    x = int(input())
    if x == 0: print(1, 0)
    elif x == 1: print(0, 1)
    else:
        for i in range(x-1):
            arr.append(arr[-2] + arr[-1])
        print(arr[x-2], arr[x-1])