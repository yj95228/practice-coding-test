# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AX8rj3iKV5gDFAQe&solveclubId=AYmCPbwakowDFAUe&problemBoxTitle=09_230803%3A+Queue_BFS&problemBoxCnt=5&probBoxId=AYm4kJEa4c4DFARi
import sys

sys.stdin = open("input.txt", "rt")
for _ in range(1, 11):
    TC = int(input())
    arr = list(map(int, input().split()))
    i = 1
    while arr[-1] > 0:
        last = arr.pop(0)
        arr.append(0 if last-i < 0 else last-i)
        i = 1 if i >= 5 else i+1    # i = i%5 + 1
    print(f'#{TC}',*arr)