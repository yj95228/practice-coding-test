# TODO: 처음에 조합으로 접근했다가 powerset으로 풀었던 문제
# https://www.acmicpc.net/problem/9375
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    M = int(input())
    obj = {}
    for _ in range(M):
        name, kind = input().split()
        if kind in obj:
            obj[kind] += 1
        else:
            obj[kind] = 1
    answer = 1
    for x in list(obj.values()):
        answer *= x+1
    print(answer-1)