# TODO: 다시 풀어보기
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX8gn30KB90DFARO&probBoxId=AYmuRN-KAGwDFARi+&type=USER&problemBoxTitle=07_230801%3A+Stack%282%29&problemBoxCnt=++7+
import sys

sys.stdin = open("input.txt", "rt")
for tc in range(1,11):
    _ = input()
    txt = list(input())
    answer, num, stack = '', [], []
    # priority = {'(': -1, '*': 1, '+': 0}
    # incoming priority
    icp = {'(':3,'*':2,'+':1}
    # in stack priority
    isp = {'(':0,'*':2,'+':1}

    # (1) 중위표기식 => 후위표기식
    for x in txt:
        # x가 숫자면 answer에 추가
        if x.isdigit():
            answer += x
        # (이면 무조건 push ('('가 경계선'
        elif x == '(':
            stack.append(x)     # 무조건 push
        # )이면 무조건 pop해서 answer에 추가 (')'는 추가 X)
        elif x == ')':      # 식만들기의 종결이므로 스택에 남길
            while stack:
                v = stack.pop()
                # '(' 처리 (꺼내면 X) : 우선순위 최약체
                # 괄호의 끝이므로 그만 pop
                if v == '(': break
                else: answer+= v
        # else 나보다 우선순위가 높거나 같으면 answer에 추가
        else:
            while stack and icp[x] <= isp[stack[-1]]:
            # while stack and priority[x] <= priority[stack[-1]]:
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
            if x == '+':
                stack.append(A + B)
            elif x == '*':
                stack.append(A * B)
    print(f'#{tc} {stack.pop()}')

# 서용님 코드
priority = {'*': 2, '+': 1, ')': 3, '(': 0}
for tc in range(1, 11):
    N = int(input())
    F = input()
    equation = ''
    stack = []
    for f in F:
        if f.isdigit():
            equation += f
        elif f == '(':
            stack.append(f)
        elif f == ')':
            while stack and stack[-1] != '(':
                equation += stack.pop()
            stack.pop()
        else:
            while stack and priority[f] <= priority[stack[-1]]:
                equation += stack.pop()
            stack.append(f)
    while stack:
        equation += stack.pop()

    for e in equation:
        if e.isdigit():
            stack.append(int(e))
        elif len(stack) > 1:
            A, B = stack.pop(), stack.pop()
            if e == '+':
                stack.append(A + B)
            elif e == '*':
                stack.append(A * B)
    print(f'#{tc} {stack[-1]}')