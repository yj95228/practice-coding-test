import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    answer = 987654321
    # 3층으로 쌓는 경우
    for i in range(2):
        for j in range(2):
            for k in range(2):
                answer = min(answer, (A[i] + B[j] + C[k]) * max(A[1-i], B[1-j], C[1-k]))
    # 2층으로 쌓는 경우
    for i in range(2):
        for j in range(2):
            for k in range(2):
                answer = min(answer, max(A[i]+B[j], C[k]) * (max(A[1-i],B[1-j]) + C[1-k]))
                answer = min(answer, max(B[i]+C[j], A[k]) * (max(B[1-i],C[1-j]) + A[1-k]))
                answer = min(answer, max(C[i]+A[j], B[k]) * (max(C[1-i],A[1-j]) + B[1-k]))
    print(answer)