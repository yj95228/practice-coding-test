# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX9DMaOqIg8DFAQe&probBoxId=AYnhsQg60D4DFARi&type=USER&problemBoxTitle=15_230811%3A+greedy_Test_03&problemBoxCnt=2
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (-x[1], -x[0]))
    answer, time = 0, 0
    while arr:
        s, e = arr.pop()
        if time <= s:
            answer += 1
            time = e
    print(f'#{tc} {answer}')