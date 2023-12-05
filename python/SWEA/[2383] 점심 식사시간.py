# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5-BEE6AK0DFAVl
from sys import stdin
stdin = open('input.txt')
input = stdin.readline

def recur(n, wq1, wq2):
    global answer
    if n == length:
        wq1.sort()
        wq2.sort()
        result = 0
        for i, x in enumerate(wq1):
            if 0 <= i-3 and x <= wq1[i-3]+s1:
                result = max(result, wq1[i-3]+2*s1+1)
            else:
                result = max(result, x+s1+1)
        for i, x in enumerate(wq2):
            if 0 <= i-3 and x <= wq2[i-3]+s2:
                result = max(result, wq2[i-3]+2*s2+1)
            else:
                result = max(result, x+s2+1)
        answer = min(answer, result)
        return
    r, c = people[n]
    recur(n+1, wq1+[abs(sr1-r)+abs(sc1-c)], wq2)
    recur(n+1, wq1, wq2+[abs(sr2-r)+abs(sc2-c)])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    INF = N*N+10
    matrix = [list(map(int, input().split())) for _ in range(N)]
    people = []
    sr1, sc1, s1, sr2, sc2, s2 = None, None, None, None, None, None
    for r in range(N):
        for c in range(N):
            if not matrix[r][c]: continue
            elif matrix[r][c] == 1:
                people.append((r,c))
            else:
                if sr1 is None:
                    sr1, sc1, s1 = r, c, matrix[r][c]
                else:
                    sr2, sc2, s2 = r, c, matrix[r][c]

    length = len(people)
    answer = 987654321
    recur(0, [], [])
    print(f'#{tc} {answer}')

# 2차 풀이
from collections import deque
from itertools import product

def solve(p):
    stairs = [[] for _ in range(2)]
    for i in range(len(people)):
        r, c = people[i]
        idx = p[i]
        length, rr, cc = stair[idx]
        stairs[idx].append(abs(rr-r)+abs(cc-c))

    mx = 0
    for i, st in enumerate(stairs):
        queue = deque()
        time = stair[i][0]
        for s in sorted(st):
            if len(queue) >= 3:
                out = queue.popleft()
                mx = max(mx, out+time)
                queue.append(max(s+1, out+time))
            else:
                queue.append(s+1)
        while queue:
            mx = max(mx, queue.popleft()+time)
    return mx

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    people, stair = [], []
    for r in range(N):
        for c in range(N):
            if A[r][c] == 1:
                people.append((r, c))
            elif A[r][c] > 1:
                stair.append((A[r][c], r, c))

    answer = 987654321
    for p in product(range(2), repeat=len(people)):
        answer = min(answer, solve(p))
    print(f'#{tc} {answer}')