# https://www.acmicpc.net/problem/15661
from sys import stdin
input = stdin.readline

def recur(n, A, B, a_score, b_score):
    global answer
    if n == N:
        if A and B:
            answer = min(answer, abs(a_score-b_score))
        return
    for a in A:
        a_score += S[a][n] + S[n][a]
    recur(n+1, A+[n], B, a_score, b_score)
    for a in A:
        a_score -= S[a][n] + S[n][a]
    for b in B:
        b_score += S[b][n] + S[n][b]
    recur(n+1, A, B+[n], a_score, b_score)
    for b in B:
        b_score -= S[b][n] + S[n][b]

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
answer = 987654321
recur(0, [], [], 0, 0)
print(answer)