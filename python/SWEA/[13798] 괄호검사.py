# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX8avIIaTPQDFARO&probBoxId=AYmlcXZqFWsDFAUe&type=USER&problemBoxTitle=06_230731%3A+Stack&problemBoxCnt=4
import sys

def solution(txt):
    quote = False
    bracket = []
    for t in txt:
        if quote:
            if t in ["\'", '\"']:
                quote = False
        else:
            if t in ["\'", '\"']:
                quote = True
            elif t in ['(', '{']:
                bracket.append(t)
            elif t in [')', '}']:
                if bracket:
                    if (bracket[-1] == '(' and t == ')')\
                    or (bracket[-1] == '{' and t == '}'):
                        bracket.pop()
                    else:
                        return 0
                else:
                    return 0
    return 0 if bracket else 1

sys.stdin = open("input.txt", "rt")
T = int(input())
for tc in range(1,T+1):
    print(f'#{tc} {solution(input())}')

# 강사님 코드
for tc in range(1,T+1):
    dict = {'{':'}', '(':')'}
    stack = []
    answer = 1
    for t in input():
        if t in dict:
            stack.append(dict[t])
        elif t in dict.values():
            if stack and stack[-1] == t:
                stack.pop()
            else:
                answer = 0
                break