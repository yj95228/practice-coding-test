# https://www.acmicpc.net/problem/2588

import sys

sys.stdin=open("python\백준\input.txt","rt")
input = sys.stdin.readline
A = int(input())
B = input()
print(A*int(B[2]))
print(A*int(B[1]))
print(A*int(B[0]))
print(A*int(B))