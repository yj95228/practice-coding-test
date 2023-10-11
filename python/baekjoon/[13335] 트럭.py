# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5-BEE6AK0DFAVl
from sys import stdin
from collections import deque
stdin = open('input.txt')
input = stdin.readline

N, W, L = map(int, input().split()) # N: 트럭 수, W: 다리 길이, L: 다리 최대 하중
queue = deque(list(map(int, input().split())))
dari = deque([0]*W)
time = 0
while True:
    time += 1
    dari.popleft()
    if queue:
        x = queue.popleft()
        if sum(dari)+x <= L and len(dari) < W:
            dari.append(x)
        else:
            queue.appendleft(x)
            dari.append(0)
    else:
        dari.append(0)
    if not any(dari): break
    print(time)
    print('큐',queue)
    print('다리',dari)
print(time)