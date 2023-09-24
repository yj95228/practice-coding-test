# 121604kb 1536ms
import sys
input = sys.stdin.readline

N = int(input())
test = []
for _ in range(N):
    P, L = map(int, input().split())
    test.append((L,P))

M = int(input())
for _ in range(M):
    command, *arr = input().split()
    if command == 'recommend':
        if arr[0] == '1':
            print(max(test)[1])
        else:
            print(min(test)[1])
    elif command == 'add':
        P, L = map(int, arr)
        test.append((L,P))
    elif command == 'solved':
        P = int(arr[0])
        for i in range(len(test)):
            if test[i][1] == P:
                test.pop(i)
                break