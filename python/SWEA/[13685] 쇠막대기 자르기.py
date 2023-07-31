# TODO: 다시 풀어보기
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX7w36oqS-YDFARO&probBoxId=AYmlcXZqFWsDFAUe&type=USER&problemBoxTitle=06_230731%3A+Stack%281%29&problemBoxCnt=4
import sys

sys.stdin = open("input.txt", "rt")
T = int(input())
for tc in range(1,T+1):
    answer = 0
    bracket = []
    txt = input()
    i = 0
    while i < len(txt):
        if txt[i] == '(':
            bracket.append(txt[i])
        else:
            if bracket and txt[i] == ')':
                bracket.pop()
                if txt[i-1] == '(':
                    answer += len(bracket)
                else:
                    answer += 1
        i += 1
    print(f'#{tc} {answer}')