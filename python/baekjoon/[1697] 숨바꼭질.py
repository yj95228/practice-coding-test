# https://www.acmicpc.net/problem/1697
import sys

sys.stdin = open('input.txt','rt')
input = sys.stdin.readline

N, K = map(int, input().split())
queue = [N]
distance = {N:0}
while queue:
    current = queue.pop(0)
    if current == K: break
    for x in (-1,1,current):
        if current+x not in distance and 0 <= current+x <= 100000:
            distance[current+x] = distance[current]+1
            queue.append(current+x)
print(distance[K])