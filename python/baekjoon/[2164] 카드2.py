# https://www.acmicpc.net/problem/2164
import sys
from collections import deque
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())
queue = deque([x for x in range(1,N+1)])
while len(queue) >= 2:
    queue.popleft()
    queue.append(queue.popleft())
print(queue[0])