import sys
input = sys.stdin.readline

N, I, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]
answer = 0
for r, c in A:
    for x in range(1, I//2):
        rr, cc = x, I//2-x
        for i in range(-rr, 1):
            if 1 <= r+i <= N and 1 <= r+i+rr <= N:
                for j in range(-cc, 1):
                    if 1 <= c+j <= N and 1 <= c+j+cc <= N:
                        result = 0
                        for a, b in A:
                            if r+i <= a <= r+i+rr and c+j <= b <= c+j+cc:
                                result += 1
                        answer = max(answer, result)
print(answer)