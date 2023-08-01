# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX8gn30KB90DFARO&probBoxId=AYmuRN-KAGwDFARi+&type=USER&problemBoxTitle=07_230801%3A+Stack%282%29&problemBoxCnt=++7+
import sys

sys.stdin = open("input.txt", "rt")
for tc in range(1, 11):
    _ = input()
    txt = list(input())
    answer, stack = [], []
    priority = {'*': 1, '+': 0}
    for x in txt:
        if x.isdigit():
            answer.append(int(x))
            if stack and stack[-1] == '*':
                stack.pop()
                answer.append(answer.pop() * answer.pop())
            elif len(stack) > 1:
                answer.insert(0, answer.pop(0) + answer.pop(0))
        else:
            stack.append(x)
    print(f'#{tc} {answer.pop(0)+answer.pop(0)}')

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
        else:
            B, A = stack.pop(), stack.pop()
            if x == '+': stack.append(A+B)
            elif x == '*': stack.append(A*B)

    print(f'#{tc} {stack.pop()}')
