import sys

sys.stdin=open("python\백준\input.txt","rt")
input = sys.stdin.readline
N = int(input())
stack = []
for _ in range(N):
    command = input().split()
    if len(command) > 1:
        if command[0] == 'push':
            stack.append(command[1])
    else:
        if command[0] == 'pop':
            print(stack.pop() if stack else -1)
        elif command[0] == 'size':
            print(len(stack))
        elif command[0] == 'empty':
            print(0 if stack else 1)
        elif command[0] == 'top':
            print(stack[-1] if stack else -1)