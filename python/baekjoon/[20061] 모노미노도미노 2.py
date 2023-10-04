# 각각 5분씩 읽고 1:11에 풀기 시작
# 1차 제출: 코드가 개판이지만 일단 제출 (2:24)
# 2차 제출: pycharm으로 다행히 type error 잡음 (blue[i][c] 해줘야 하는데 blue[c]로 함)
# 3차 제출: blue를 뒤집어서 코드 새로 짜기
# 4차 제출: 행과 열이 헷갈려서 X,Y 등등 실수 수정
# 5차 제출: i+1이 안되어있었음 (121512kb, 348ms)
# https://www.acmicpc.net/problem/19236
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

red = [[0]*4 for _ in range(4)]
blue = [[0]*4 for _ in range(6)]
green = [[0]*4 for _ in range(6)]
N = int(input())
answer = 0
for _ in range(N):
    T, X, Y = map(int, input().split())

    if T == 1:
        i = 0
        while i+1 <= 5 and blue[i+1][X] == 0:
            i += 1
        blue[i][X] = 1
        if all(blue[i]):
            answer += 1
            blue.pop(i)
            blue.insert(0, [0]*4)
        i = 0

        while i+1 <= 5 and green[i+1][Y] == 0:
            i += 1
        green[i][Y] = 1
        if all(green[i]):
            answer += 1
            green.pop(i)
            green.insert(0, [0]*4)

    elif T == 2:
        i = 0
        while i+2 <= 5 and blue[i+1][X] == 0 and blue[i+2][X] == 0:
            i += 1
        blue[i][X], blue[i+1][X] = 1, 1
        if all(blue[i]):
            answer += 1
            blue.pop(i)
            blue.insert(0, [0]*4)
        if all(blue[i+1]):
            answer += 1
            blue.pop(i+1)
            blue.insert(0, [0]*4)

        i = 0
        while i+1 <= 5 and green[i+1][Y] == 0 and green[i+1][Y+1] == 0:
            i += 1
        green[i][Y], green[i][Y+1] = 1, 1
        if all(green[i]):
            answer += 1
            green.pop(i)
            green.insert(0, [0]*4)

    elif T == 3:
        i = 0
        while i+1 <= 5 and blue[i+1][X] == 0 and blue[i+1][X+1] == 0:
            i += 1
        blue[i][X], blue[i][X+1] = 1, 1
        if all(blue[i]):
            answer += 1
            blue.pop(i)
            blue.insert(0, [0]*4)

        i = 0
        while i+2 <= 5 and green[i+1][Y] == 0 and green[i+2][Y] == 0:
            i += 1
        green[i][Y], green[i+1][Y] = 1, 1
        if all(green[i]):
            answer += 1
            green.pop(i)
            green.insert(0, [0]*4)
        if all(green[i+1]):
            answer += 1
            green.pop(i+1)
            green.insert(0, [0]*4)

    if any(blue[0]) and any(blue[1]):
        blue.pop()
        blue.pop()
        blue.insert(0, [0]*4)
        blue.insert(1, [0]*4)
    elif any(blue[1]):
        blue.pop()
        blue.insert(1, [0]*4)

    if any(green[0]) and any(green[1]):
        green.pop()
        green.pop()
        green.insert(0, [0]*4)
        green.insert(1, [0]*4)
    elif any(green[1]):
        green.pop()
        green.insert(1, [0]*4)

print(answer)
print(sum(sum(blue,[]))+sum(sum(green,[])))

# 2차 풀이
'''
- 폭발시킬 때 한번에 처리 (idx 바뀌므로)
- 1차. 19:00 ~ 19:50 틀렸습니다 1%
- 2차. 폭발시킬 때 idx 앞에서부터 처리
'''
def put(t,x,y,arr,green=True):
    global answer
    where = 5
    explode = []
    if green:
        for rr, cc in green_block[t]:
            lst = [row[y+cc] for row in arr]
            where = min(where, lst.index(1)-1 if any(lst) else 5)
        for rr, cc in green_block[t]:
            arr[where+rr][y+cc] = 1
            if all(arr[where+rr]):
                explode.append(where+rr)

    else:
        for rr, cc in blue_block[t]:
            lst = [row[3-x+cc] for row in arr]
            where = min(where, lst.index(1)-1 if any(lst) else 5)
        for rr, cc in blue_block[t]:
            arr[where+rr][3-x+cc] = 1
            if all(arr[where+rr]):
                explode.append(where+rr)

    for r in sorted(explode):
        answer += 1
        arr.pop(r)
        arr.insert(0,[0]*4)

N = int(input())
green = [[0]*4 for _ in range(6)]
blue = [[0]*4 for _ in range(6)]
green_block = [[(0,0)],[(0,0),(0,1)],[(0,0),(-1,0)]]
blue_block = [[(0,0)],[(0,0),(-1,0)],[(0,0),(0,-1)]]
answer = 0
for _ in range(N):
    t, x, y = map(int, input().split())
    put(t-1,x,y,green)
    if any(green[0]):
        green.pop()
        green.insert(0,[0]*4)
    if any(green[1]):
        green.pop()
        green.insert(0,[0]*4)

    put(t-1,x,y,blue,False)
    if any(blue[0]):
        blue.pop()
        blue.insert(0,[0]*4)
    if any(blue[1]):
        blue.pop()
        blue.insert(0,[0]*4)

print(answer)
print(sum(map(sum,green))+sum(map(sum,blue)))