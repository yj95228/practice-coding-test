# https://www.acmicpc.net/problem/10040
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N, M = map(int, input().split())
money = [int(input()) for _ in range(N)]
limit = [int(input()) for _ in range(M)]
vote = [0]*N
for x in limit:
    for i in range(N):
        if money[i] <= x:
            vote[i] += 1
            break
print(vote.index(max(vote))+1)