# https://www.acmicpc.net/problem/11444
from sys import stdin
stdin = open('python/baekjoon/input.txt','r')
input = stdin.readline

W, H = map(int, input().split())
P, Q = map(int, input().split())
T = int(input())
nx, ny = (P+T)%(2*W), (Q+T)%(2*H)
if nx > W: nx = 2*W-nx
if ny > H: ny = 2*H-ny
print(nx, ny)