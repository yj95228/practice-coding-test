# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX8a0ZU6TlIDFARO&probBoxId=AYmlcXZqFWsDFAUe&type=USER&problemBoxTitle=06_230731%3A+Stack%281%29&problemBoxCnt=4
import sys

sys.stdin = open("input.txt", "rt")
for tc in range(1,11):
    N, password = input().split()
    stack = []
    for txt in password:
        if stack and stack[-1] == txt:
            stack.pop()
        else:
            stack.append(txt)
    print(f'#{tc} {"".join(stack)}')
