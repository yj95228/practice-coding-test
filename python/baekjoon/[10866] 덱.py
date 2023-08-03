# https://www.acmicpc.net/problem/10866
import sys

sys.stdin = open('input.txt','rt')
input = sys.stdin.readline

N = int(input())
deque = []
for _ in range(N):
    command = input().split()
    if len(command) > 1:
        if command[0] == 'push_back':
            deque.append(int(command[1]))
        elif command[0] == 'push_front':
            deque.insert(0, int(command[1]))
    else:
        if command[0] == 'pop_front':
            print(deque.pop(0) if deque else -1)
        elif command[0] == 'pop_back':
            print(deque.pop() if deque else -1)
        elif command[0] == 'size':
            print(len(deque))
        elif command[0] == 'empty':
            print(0 if deque else 1)
        elif command[0] == 'front':
            print(deque[0] if deque else -1)
        elif command[0] == 'back':
            print(deque[-1] if deque else -1)