# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AYaWYmdafowDFARM&probBoxId=AYmCPbwako0DFAUe&type=USER&problemBoxTitle=01_230724&problemBoxCnt=6
from itertools import product
from math import inf
import sys
sys.stdin = open("input.txt", "r")

# itertools에서 product를 활용하여 푼 풀이
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arrW, arrB, arrR = [], [], []
    mn = float(inf)
    for _ in range(N):
        arr = list(input())
        arrW.append(len(list(filter(lambda x: x != 'W', arr))))
        arrB.append(len(list(filter(lambda x: x != 'B', arr))))
        arrR.append(len(list(filter(lambda x: x != 'R', arr))))
    cases = list(filter(lambda x: sum(x) == N, list(product(range(1, N-1), repeat=3))))
    for case in cases:
        sums = [sum(case[:i+1]) for i in range(3)]
        w, b, r = sums
        mn = min(mn, sum(arrW[:w]) + sum(arrB[w:b]) + sum(arrR[b:]))
    print(f'#{tc} {mn}')

# itertools를 활용하지 않은 풀이
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    t_arr = list(zip(*arr))
    txt = [' ']*N
    answer = N*M
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                txt[i:j] = ['W']*(j-i)
                txt[j:k] = ['B']*(k-j)
                txt[k:] = ['R']*(N-k)
                sm = 0
                for r in range(M):
                    for c in range(N):
                        if t_arr[r][c] != txt[c]:
                            sm += 1
                answer = min(answer, sm)
    print(f'#{tc} {answer}')

# itertools를 활용하지 않은 풀이 (2)
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    s_txt = set()
    answer = N*M
    for i in range(1,N-1):
        for j in range(i+1, N):
            txt = 'W'*i
            txt += 'B'*(j-i)
            txt += 'R'*(N-j)
            s_txt.add(txt)
    for t in s_txt:
        cnt = 0
        for r in range(N):
            cnt += M - arr[r].count(t[r])
        answer = min(answer, cnt)
    print(f'#{tc} {answer}')

# 강사님 코드
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    answer = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            cnt = 0
            for k in range(i+1):
                cnt += arr[k].count('W')
            for k in range(i+1, j+1):
                cnt += arr[k].count('B')
            for k in range(j+1, N):
                cnt += arr[k].count('R')
            answer = max(answer, cnt)
    print(f'#{tc} {N*M-answer}')