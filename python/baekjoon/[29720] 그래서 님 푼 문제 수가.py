# https://www.acmicpc.net/problem/29720
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
print(max(0,N-M*K), N-M*K+M-1)