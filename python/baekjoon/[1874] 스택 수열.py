# TODO: 다시 풀어보기
# https://www.acmicpc.net/problem/1874
import sys

sys.stdin=open("input.txt", "rt")
input = sys.stdin.readline
N = int(input())
i, stack, answer = 1, [], []
for _ in range(N):
    x = int(input())
    while i <= N+1:   # 여기서 답 못 만들면 'NO'
        # 스택에서 꺼내서 숫자 만들기
        if stack and stack[-1] == x:
            stack.pop()
            answer.append('-')
            break   # 다음 입력을 받음
        stack.append(i)
        i += 1
        answer.append('+')
    # 수열을 표현할 수 없는 경우 'NO' 출력
    if i > N+1:
        answer = ['NO']
        break
print('\n'.join(answer))

# 다른 코드
# lst = [int(input())) for _ in range(N)]
# stack, answer, j = [], [], 0
# for i in range(1, N+1):
#     stack.append(i)
#     answer.append('+')
#     while stack and stack[-1] == lst[j]:
#         stack.pop()
#         answer.append('-')
#         j += 1
#
# if stack:
#     print('NO')
# else:
#     print(*answer, sep = '\n')