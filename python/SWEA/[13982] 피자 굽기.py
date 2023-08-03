# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX805F_613wDFAQe&probBoxId=AYm4kJEa4c4DFARi&type=USER&problemBoxTitle=09_230803%3A+Queue_BFS&problemBoxCnt=5
import sys

sys.stdin = open("input.txt", "rt")
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    pizza = arr[:N]
    idx = [x for x in range(N)]
    i = 0
    while len(pizza) > 1:
        pizza.append(pizza.pop(0)//2)
        idx.append(idx.pop(0))
        if pizza[-1] == 0:
            pizza.pop()
            idx.pop()
            if N+i < M:
                pizza.append(arr[N+i])
                idx.append(N+i)
                i += 1
    print(f'#{tc} {idx[0]+1}')


# enumerate로 푼 버전
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(enumerate(map(int, input().split())))
    pizza = arr[:N]
    i = 0
    while len(pizza) > 1:
        first = pizza.pop(0)
        pizza.append((first[0], first[1]//2))
        if pizza[-1][1] == 0:
            pizza.pop()
            if N+i < M:
                pizza.append(arr[N+i])
                i += 1
    print(f'#{tc} {pizza[0][0]+1}')