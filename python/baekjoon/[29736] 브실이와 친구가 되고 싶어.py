# https://www.acmicpc.net/problem/29736
import sys
input = sys.stdin.readline

A, B = map(int, input().split())
K, X = map(int, input().split())
answer = min(B, K+X)-max(A, K-X)+1
print('IMPOSSIBLE' if answer <= 0 else answer)