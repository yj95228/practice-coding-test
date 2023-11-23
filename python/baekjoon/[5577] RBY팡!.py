import sys
input = sys.stdin.readline

def play(C):
    while True:
        stack = []
        for x in C:
            if not stack or stack[-1] == x:
                stack.append(x)
            else:
                if len(stack) >= 4 and stack[-1] == stack[-2] == stack[-3] == stack[-4]:
                    color = stack[-1]
                    while stack and stack[-1] == color:
                        stack.pop()
                stack.append(x)

        if len(stack) >= 4 and stack[-1] == stack[-2] == stack[-3] == stack[-4]:
            color = stack[-1]
            while stack and stack[-1] == color:
                stack.pop()

        return len(stack)

N = int(input())
A = [int(input()) for _ in range(N)]
answer = N
for i in range(N):
    B = A[:]
    if B[i] == 1:
        if B[i-3:i].count(2) + B[i+1:i+4].count(2) >= 3:
            B[i] = 2
            answer = min(answer, play(B))
        if B[i-3:i].count(3) + B[i+1:i+4].count(3) >= 3:
            B[i] = 3
            answer = min(answer, play(B))
    elif B[i] == 2:
        if B[i-3:i].count(1) + B[i+1:i+4].count(1) >= 3:
            B[i] = 1
            answer = min(answer, play(B))
        if B[i-3:i].count(3) + B[i+1:i+4].count(3) >= 3:
            B[i] = 3
            answer = min(answer, play(B))
    elif B[i] == 3:
        if B[i-3:i].count(1) + B[i+1:i+4].count(1) >= 3:
            B[i] = 1
            answer = min(answer, play(B))
        if B[i-3:i].count(2) + B[i+1:i+4].count(2) >= 3:
            B[i] = 2
            answer = min(answer, play(B))
print(answer)