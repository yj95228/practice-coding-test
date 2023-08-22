# https://www.acmicpc.net/problem/1975
import sys, heapq
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())
queue = []
for _ in range(N):
    x = int(input())
    if x: heapq.heappush(queue, x)
    elif queue: print(heapq.heappop(queue))
    else: print(0)