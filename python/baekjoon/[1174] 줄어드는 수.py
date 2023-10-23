from sys import stdin
stdin = open('input.txt','r')
input = stdin.readline

def recur(n, txt):
    if txt: s.add(int(txt))
    if len(txt) == n:
        return
    for x in range(10):
        if not txt or int(txt[-1]) > x:
            recur(n, txt+str(x))

N = int(input())
s = set()
for n in range(1, 12):
    recur(n, '')
    if len(s) >= N:
        print(sorted(list(s))[N-1])
        break
else: print(-1)