# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX739Ftq3hMDFARO&probBoxId=AYmZq5h69N4DFARi&type=USER&problemBoxTitle=05_230728%3A+String_Test&problemBoxCnt=3
import sys
sys.stdin = open("input.txt", "rt")

T = int(input())
for tc in range(1,T+1):
    A, B = input().split()
    print(f'#{tc} {len(A.replace(B, " "))}')

# 슬라이싱을 사용하는 경우 : 범위(경계)를 벗어나도 문제 발생 X
# i = answer = 0
# while i < N:
#     if A[i:i+M] == B:
#         i += M
#     else:
#         i += 1
#     answer += 1

# 직접 비교하는 경우
# while i < N-M+1:
#     for j in range(M):
#         if A[i+j] != B[j]:
#             i += 1
#             break
#     else:
#         i += M
#     answer += 1