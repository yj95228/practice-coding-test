A, B, D = map(int, input().split())
flag = True
answer = 0
dist = D
while True:
    if flag:
        if dist > A:
            dist -= A
            answer += (A+B)
        else:
            answer += dist
            dist = D
            flag = False
    else:
        if dist > B:
            dist -= B
            answer += (A+B)
        else:
            answer += dist
            break
print(answer)