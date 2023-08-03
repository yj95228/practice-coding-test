# https://www.acmicpc.net/problem/1547
import sys

sys.stdin = open('input.txt','rt')
input = sys.stdin.readline

M = int(input())
balls = [False, True, False, False]
for _ in range(M):
    A, B = map(int, input().split())
    balls[A], balls[B] = balls[B], balls[A]
print(balls.index(True))