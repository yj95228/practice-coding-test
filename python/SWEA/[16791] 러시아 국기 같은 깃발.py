# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AYaWYmdafowDFARM&probBoxId=AYmCPbwako0DFAUe&type=USER&problemBoxTitle=01_230724&problemBoxCnt=6
from itertools import product
from math import inf
import sys

sys.stdin = open("input.txt", "r")
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