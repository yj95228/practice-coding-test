# https://www.acmicpc.net/problem/29738
import sys
input = sys.stdin.readline

def check(score):
    if score <= 25:
        return 'World Finals'
    elif score <= 1000:
        return 'Round 3'
    elif score <= 4500:
        return 'Round 2'
    else:
        return 'Round 1'

T = int(input())
for tc in range(1,T+1):
    score = int(input())
    print(f'Case #{tc}: {check(score)}')