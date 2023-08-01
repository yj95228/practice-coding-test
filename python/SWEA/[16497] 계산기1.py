# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AYZNUQEq1AEDFARc&probBoxId=AYmuRN-KAGwDFARi&type=USER&problemBoxTitle=07_230801%3A+Stack%282%29&problemBoxCnt=7
import sys

sys.stdin = open("input.txt", "rt")
for tc in range(1,11):
    _ = input()
    txt = list(input())
    answer, stack = [], []
    priority = {'*': 1, '+': 0}
    for x in txt:
        if x.isdigit():
            if stack and answer:
                stack.pop()
                answer.append(answer.pop() + int(x))
            else:
                answer.append(int(x))
        else:
            stack.append(x)
    print(f'#{tc} {answer[0]}')

# 날로 먹는 풀이
for tc in range(10):
    _ = input()
    print(f'#{tc} {sum(map(int, input().split("+")))}')

# 강사님 코드
for tc in range(1,11):
    _ = input()
    txt = list(input())
    answer, stack = '', []
    # (1) 중위표기식 => 후위표기식
    for x in txt:
        if x.isdigit():
            answer += x
        else:
            while stack and priority[x] <= priority[stack[-1]]:
                answer += stack.pop()
            stack.append(x)
    while stack:
        answer += stack.pop()

    # (2) 후위표기식 계산 : 숫자 append, 연산자 pop해서 계산
    for x in answer:
        if x.isdigit():
            stack.append(int(x))
        elif x == '+':
            B, A = stack.pop(), stack.pop()
            stack.append(A+B)

    print(f'#{tc} {stack.pop()}')