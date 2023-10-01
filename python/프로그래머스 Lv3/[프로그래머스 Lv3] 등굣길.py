# https://school.programmers.co.kr/learn/courses/30/lessons/42898?language=python3
def solution(m, n, puddles):
    answer = 0
    dp = [[0]*(m+1)] + [[0]+[0]*m for _ in range(n)]
    dp[1][1] = 1
    for r in range(1,n+1):
        for c in range(1,m+1):
            if [c,r] not in puddles:
                dp[r][c] += (dp[r][c-1] + dp[r-1][c])%1_000_000_007
    return dp[-1][-1]%1_000_000_007