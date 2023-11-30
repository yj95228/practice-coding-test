import sys
from itertools import permutations
input = sys.stdin.readline

def solve(gbb):

    def play(i, j):
        i, j = min(i, j), max(i, j)
        x = gbb[turn[0]] if i == 0 else B[turn[1]] if i == 1 else C[turn[2]]
        y = gbb[turn[0]] if j == 0 else B[turn[1]] if j == 1 else C[turn[2]]
        turn[i] += 1
        turn[j] += 1
        if A[x][y] == 2:
            score[i] += 1
            return i, [v for v in [0,1,2] if v != i and v != j][0]
        else:
            score[j] += 1
            return j, [v for v in [0,1,2] if v != i and v != j][0]

    score = [0]*3
    i, j = 0, 1
    turn = [0]*3
    for _ in range(3*(K-1)+1):
        if turn[0] >= N: return False
        i, j = play(i, j)
        if max(score) >= K:
            return score[0] >= K
    return False

N, K = map(int, input().split()) # N: 손동작 수, K: 필요 승수
A = [list(map(int, input().split())) for _ in range(N)]
B = list(map(lambda x: int(x)-1, input().split()))
C = list(map(lambda x: int(x)-1, input().split()))

for gawibawibo in permutations(range(N), N):
    if solve(gawibawibo):
        print(1)
        break
else: print(0)