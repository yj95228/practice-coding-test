# https://www.acmicpc.net/problem/8979
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N, K = map(int, input().split())
olympic = []
for _ in range(N):
    idx, gold, silver, bronze = map(int, input().split())
    olympic.append((idx, gold, silver, bronze))
olympic.sort(key=lambda x: (x[1],x[2],x[3]), reverse=True)
if olympic[0][0] == K: print(1)
else:
    rank = [1]
    for i in range(1,N):
        if (olympic[i][1], olympic[i][2], olympic[i][3])\
        == (olympic[i-1][1], olympic[i-1][2], olympic[i-1][3]):
            rank.append(rank[-1])
        else:
            rank.append(i+1)
        if olympic[i][0] == K:
            print(rank[-1])
            break