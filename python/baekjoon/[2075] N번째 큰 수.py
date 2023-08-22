# https://www.acmicpc.net/problem/2075
import sys
import heapq
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())
queue = []
for _ in range(N):
    for x in map(int, input().split()):
        heapq.heappush(queue, x)
        while len(queue) > N:
            heapq.heappop(queue)
print(queue[0])