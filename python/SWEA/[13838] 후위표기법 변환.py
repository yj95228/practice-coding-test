# TODO: 다시 보기
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX8ggu9KBasDFARO&probBoxId=AYmuRN-KAGwDFARi+&type=USER&problemBoxTitle=07_230801%3A+Stack%282%29&problemBoxCnt=++7+
import sys

sys.stdin = open("input.txt", "rt")
T = int(input())
for tc in range(1,T+1):
    txt = list(input())
    arr = [i for i, x in enumerate(txt) if x == '*']
    for i in arr:
        txt[i], txt[i+1] = txt[i+1], txt[i]
    idx = txt.index('+')
    answer = txt[:idx]+txt[idx+1:] + ['+']
    print(f'#{tc} {"".join(answer)}')

# 강사님 코드
for tc in range(1,T+1):
    txt = input()
    stack, equation = [], ''
    # 연산자의 우선순위 : 높을수록 높은 우선순위
    priority = {'*':1, '+':0}
    for x in txt:
        # 숫자인 경우 equation에 추가
        # 연산자면 우선순위 비교해서 처리
        if x.isdigit():
            equation += x   # 후위표기식에 추가
        else:
            while stack and priority[x] <= priority[stack[-1]]:
                equation += stack.pop()
            stack.append(x)
    while stack:
        equation += stack.pop()
    print(f'#{tc} {equation}')

# 서용님 코드
F = input()
S, A = [], ''
for f in F:
    if f == '+':
        while S:
            A += S.pop()
        S.append(f)
    elif f == '*':
        S.append(f)
    else:
        A += f
        while S and S[-1] == '*':
            A += S.pop()
A += S.pop()