# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX8jykL6xDADFARO&probBoxId=AYmuRN-KAGwDFARi&type=USER&problemBoxTitle=07_230801%3A+Stack%282%29&problemBoxCnt=7
import sys

def solution(txt):
    answer = []
    for x in txt:
        if x.isdigit():
            answer.append(int(x))
        elif x == '.':
            return int(answer[0]) if len(answer) == 1 else 'error'
        elif len(answer) < 2:
            return 'error'
        else:
            B, A = answer.pop(), answer.pop()
            if x == '+': answer.append(A+B)
            elif x == '-': answer.append(A-B)
            elif x == '*': answer.append(A*B)
            elif x == '/': answer.append(int(A/B))

sys.stdin = open("input.txt", "rt")
T = int(input())
for tc in range(1,T+1):
    txt = list(input().split())
    print(f'#{tc} {solution(txt)}')