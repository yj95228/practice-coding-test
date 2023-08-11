# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX9DJAbqIewDFAQe&probBoxId=AYnhsQg60D4DFARi&type=USER&problemBoxTitle=15_230811%3A+greedy_Test_03&problemBoxCnt=2
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    container = sorted(list(map(int, input().split())), reverse=True)
    truck = sorted(list(map(int, input().split())), reverse=True)
    answer = 0
    while container and truck:
        print(container, truck)
        if container[0] <= truck[0]:
            answer += container[0]
            container.pop(0)
            truck.pop(0)
        else:
            container.pop(0)
    print(f'#{tc} {answer}')