from sys import stdin
input = stdin.readline

def recur(A):
    NN = len(A)//2
    if NN:
        B = [[0]*NN for _ in range(NN)]
        for r in range(NN):
            for c in range(NN):
                B[r][c] = sorted([A[2*r][2*c], A[2*r+1][2*c], A[2*r][2*c+1], A[2*r+1][2*c+1]])[-2]
        return recur(B)
    else:
        return A[0][0]

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
print(recur(A))