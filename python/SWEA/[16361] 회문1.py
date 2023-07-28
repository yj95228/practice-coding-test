# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AYYztTgKYB8DFARc&solveclubId=AYmCPbwakowDFAUe&problemBoxTitle=05_230728%3A+String_Test&problemBoxCnt=3&probBoxId=AYmZq5h69N4DFARi
import sys

sys.stdin = open("input.txt", "rt")

for tc in range(1,11):
    N = int(input())
    arr = [list(input()) for _ in range(8)]
    t_arr = list(zip(*arr))
    answer = 0
    for i in range(8):
        for j in range(8-N+1):
            if arr[i][j:j+N] == arr[i][j:j+N][::-1]:
                answer += 1
            if t_arr[i][j:j+N] == t_arr[i][j:j+N][::-1]:
                answer += 1
    print(f'#{tc} {answer}')