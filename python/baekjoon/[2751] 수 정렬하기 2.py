# https://www.acmicpc.net/problem/1920
import sys

sys.stdin = open('input.txt','rt')
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
for x in sorted(arr):
    print(x)