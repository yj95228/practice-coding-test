import sys

sys.stdin=open("python\백준\input.txt","rt")
input = sys.stdin.readline
N = int(input())
lst = []
for _ in range(N):
    txt = input().split()
    if len(txt) == 2:
        if txt[0] == 'push':
            lst.append(txt[1])
    else:
        if txt[0] == 'pop':
            if len(lst):
                a = lst.pop()
                print(a)
            else:
                print(-1)
        elif txt[0] == 'size':
            print(len(lst))
        elif txt[0] == 'empty':
            print(0 if len(lst) else 1)
        elif txt[0] == 'top':
            print(lst[len(lst)-1] if len(lst) else -1)