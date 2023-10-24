from sys import stdin
input = stdin.readline

def solve():
    queue = [(1, 0)]
    V = [set() for _ in range(2*S+1)]
    V[1].add(0)
    time = 0
    while queue:
        temp_q = []
        for cnt, clipboard in queue:
            if cnt == S: return time
            temp_q.append((cnt, cnt))
            if clipboard and cnt+clipboard < 2*S+1 and clipboard not in V[cnt+clipboard]:
                V[cnt+clipboard].add(clipboard)
                temp_q.append((cnt+clipboard, clipboard))
            if 0 <= cnt-1 and clipboard not in V[cnt-1]:
                V[cnt-1].add(clipboard)
                temp_q.append((cnt-1, clipboard))
        queue = temp_q
        time += 1

S = int(input())
print(solve())