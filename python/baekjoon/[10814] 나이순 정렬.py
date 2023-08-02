# https://www.acmicpc.net/problem/1181
import sys

sys.stdin = open('input.txt','rt')
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(input().split())
for age, name in sorted(arr, key=lambda x: int(x[0])):
    print(age, name)