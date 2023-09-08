# https://www.acmicpc.net/problem/23971
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

H, W, N, M = map(int, input().split())
a = H//(N+1)+1 if H%(N+1) else H//(N+1)
b = W//(M+1)+1 if W%(M+1) else W//(M+1)
print(a*b)