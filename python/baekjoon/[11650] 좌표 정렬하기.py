# https://www.acmicpc.net/problem/11650
import sys

sys.stdin = open('input.txt','rt')
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    X, Y = map(int, input().split())
    arr.append((X,Y))
for a, b in sorted(arr, key=lambda x: (x[0], x[1])):
    print(a,b)