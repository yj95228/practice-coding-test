# https://www.acmicpc.net/problem/4153
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

while True:
    A, B, C = map(int, input().split())
    if (A, B, C) == (0, 0, 0): break
    print('right' if A**2 + B**2 == C**2 or B**2 + C**2 == A**2 or C**2 + A**2 == B**2 else 'wrong')