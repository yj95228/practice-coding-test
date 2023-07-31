# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX8azz-KThgDFARO&probBoxId=AYmlcXZqFWsDFAUe+&type=USER&problemBoxTitle=06_230731%3A+Stack&problemBoxCnt=++4+
import sys

sys.stdin = open("input.txt", "rt")
T = int(input())
for tc in range(1,T+1):
    stack = []
    for t in input():
        if stack and stack[-1] == t:
            stack.pop()
        else:
            stack.append(t)
    print(f'#{tc} {len(stack)}')