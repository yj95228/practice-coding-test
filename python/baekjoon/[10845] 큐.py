# https://www.acmicpc.net/problem/10845
import sys

sys.stdin = open('input.txt','rt')
input = sys.stdin.readline

N = int(input())
queue = []
for _ in range(N):
    command = input().split()
    if len(command) > 1:
        queue.append(int(command[1]))
    else:
        if command[0] == 'pop':
            print(queue.pop(0) if queue else -1)
        elif command[0] == 'size':
            print(len(queue))
        elif command[0] == 'empty':
            print(0 if queue else 1)
        elif command[0] == 'front':
            print(queue[0] if queue else -1)
        elif command[0] == 'back':
            print(queue[-1] if queue else -1)