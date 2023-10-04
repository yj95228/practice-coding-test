# 6번째 성공 / 풀이시간: 약 4시간 (실패 횟수 5회)
# FIXME: 말의 위치를 확인할때 같은 숫자가 윷놀이 지도에 여러 군데 있는 것을 간과함
# 첫번째 실수: 다른 말이 있는지 확인을 같은 숫자인지로만 확인해서 10/20/25/30/35/40가 빠짐
# 두번째 실수: 30의 경우 지도 두군데에 있어서 해당 조건을 따로 처리함
# https://www.acmicpc.net/problem/17825
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 말이 이동을 마치는 칸에 다른 말이 있으면 True, 없으면 False
def check(x, y, h1, h2, h3, h4):
    # x: 체크할 타입, y: 체크할 idx, h1: 1번말, h2: 2번말, h3: 3번말, h4: 4번말
    if x is not None:
        if game[x][y] in (10,20,25,35,40):
            # 같은 숫자면 True
            if h1[0] is not None and game[x][y] == game[h1[0]][h1[1]]: return True
            if h2[0] is not None and game[x][y] == game[h2[0]][h2[1]]: return True
            if h3[0] is not None and game[x][y] == game[h3[0]][h3[1]]: return True
            if h4[0] is not None and game[x][y] == game[h4[0]][h4[1]]: return True
        elif game[x][y] == 30:
            if h1[0] is not None and\
            ((x,y) == (h1[0],h1[1]) or (x,y,h1[0],h1[1]) in ((3,0,0,15),(0,15,3,0),(1,5,2,4),(1,5,3,5),(2,4,1,5),(2,4,3,5),(3,5,1,5),(3,5,2,4))): return True
            if h2[0] is not None and\
            ((x,y) == (h2[0],h2[1]) or (x,y,h2[0],h2[1]) in ((3,0,0,15),(0,15,3,0),(1,5,2,4),(1,5,3,5),(2,4,1,5),(2,4,3,5),(3,5,1,5),(3,5,2,4))): return True
            if h3[0] is not None and\
            ((x,y) == (h3[0],h3[1]) or (x,y,h3[0],h3[1]) in ((3,0,0,15),(0,15,3,0),(1,5,2,4),(1,5,3,5),(2,4,1,5),(2,4,3,5),(3,5,1,5),(3,5,2,4))): return True
            if h4[0] is not None and\
            ((x,y) == (h4[0],h4[1]) or (x,y,h4[0],h4[1]) in ((3,0,0,15),(0,15,3,0),(1,5,2,4),(1,5,3,5),(2,4,1,5),(2,4,3,5),(3,5,1,5),(3,5,2,4))): return True
        else:
            # 같은 위치면 True
            if h1[0] is not None and (x, y) == (h1[0], h1[1]): return True
            if h2[0] is not None and (x, y) == (h2[0], h2[1]): return True
            if h3[0] is not None and (x, y) == (h3[0], h3[1]): return True
            if h4[0] is not None and (x, y) == (h4[0], h4[1]): return True
    return False

def dfs(n, result, h1, h2, h3, h4):
    global answer
    if n == 10:
        answer = max(result, answer)
        return
    x = arr[n]
    if h1[0] is not None:
        type1, idx1 = h1
        # 파란 화살표
        if type1 == 0 and idx1+x in (5, 10, 15):
            new_type = (idx1+x)//5
            if new_type < 4 and not check(new_type, 0, h1, h2, h3, h4):
                dfs(n+1, result+game[new_type][0], [new_type, 0], h2, h3, h4)
        else:
            # 도착
            if len(game[type1]) <= idx1+x:
                dfs(n+1, result, [None, None], h2, h3, h4)
            else:
                # 빨간 화살표
                if not check(type1, idx1+x, h1, h2, h3, h4):
                    dfs(n+1, result+game[type1][idx1+x], [type1, idx1+x], h2, h3, h4)
    if h2[0] is not None:
        type2, idx2 = h2
        # 파란 화살표
        if type2 == 0 and idx2+x in (5, 10, 15):
            new_type = (idx2+x)//5
            if new_type < 4 and not check(new_type, 0, h1, h2, h3, h4):
                dfs(n+1, result+game[new_type][0], h1, [new_type, 0], h3, h4)
        else:
            # 도착
            if len(game[type2]) <= idx2+x:
                dfs(n+1, result, h1, [None, None], h3, h4)
            else:
                # 빨간 화살표
                if not check(type2, idx2+x, h1, h2, h3, h4):
                    dfs(n+1, result+game[type2][idx2+x], h1, [type2, idx2+x], h3, h4)
    if h3[0] is not None:
        type3, idx3 = h3
        # 파란 화살표
        if type3 == 0 and idx3+x in (5, 10, 15):
            new_type = (idx3+x)//5
            if new_type < 4 and not check(new_type, 0, h1, h2, h3, h4):
                dfs(n+1, result+game[new_type][0], h1, h2, [new_type, 0], h4)
        else:
            # 도착
            if len(game[type3]) <= idx3+x:
                dfs(n+1, result, h1, h2, [None, None], h4)
            else:
                # 빨간 화살표
                if not check(type3, idx3+x, h1, h2, h3, h4):
                    dfs(n+1, result+game[type3][idx3+x], h1, h2, [type3, idx3+x], h4)
    if h4[0] is not None:
        type4, idx4 = h4
        # 파란 화살표
        if type4 == 0 and idx4+x in (5, 10, 15):
            new_type = (idx4+x)//5
            if new_type < 4 and not check(new_type, 0, h1, h2, h3, h4):
                dfs(n+1, result+game[new_type][0], h1, h2, h3, [new_type, 0])
        else:
            # 도착
            if len(game[type4]) <= idx4+x:
                dfs(n+1, result, h1, h2, h3, [None, None])
            else:
                # 빨간 화살표
                if not check(type4, idx4+x, h1, h2, h3, h4):
                    dfs(n+1, result+game[type4][idx4+x], h1, h2, h3, [type4, idx4+x])


arr = list(map(int, input().split()))
game = [[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
        [10, 13, 16, 19, 25, 30, 35, 40],
        [20, 22, 24, 25, 30, 35, 40],
        [30, 28, 27, 26, 25, 30, 35, 40]]
answer = 0
dfs(0, 0, [0, 0], [0, 0], [0, 0], [0, 0])
print(answer)

# 7번째 풀이(새로 짜기) / 풀이시간: 약 1시간 (실패 횟수 5회)
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def cango(i, type, x):
    for idx in range(4):
        if i != idx and horse[idx][0] is not None:
             # 위치가 동일한 경우
            if [type, x] == horse[idx]: return False
            # 10/20/25/35/40에 말이 놓여있는 경우
            elif game[horse[idx][0]][horse[idx][1]] == game[type][x] and game[type][x] in (10,20,25,35,40): return False
            # 30에 말이 놓여있는 경우
            elif (type, x, *horse[idx]) in ((0,15,3,0),(3,0,0,15),(1,5,2,4),(1,5,3,5),(2,4,1,5),(2,4,3,5),(3,5,1,5),(3,5,2,4)):
                return False
    return True

def dfs(n, result):
    global answer
    if n == 10:
        answer = max(answer, result)
        return
    x = arr[n]
    for i in range(4):
        type, idx = horse[i]
        if type is not None:
            # 파란색 화살표(10 / 20 / 30)인 경우
            if type == 0 and idx+x in (5,10,15):
                new_type = type+(idx+x)//5
                # print(new_type)
                if cango(i, new_type, 0):
                    horse[i] = [new_type, 0]
                    dfs(n+1, result+game[new_type][0])
                    horse[i] = [type, idx]
            # 도착인 경우
            elif len(game[type]) <= idx+x:
                horse[i] = [None, None]
                dfs(n+1, result)
                horse[i] = [type, idx]
            else:
                if cango(i, type, idx+x):
                    horse[i] = [type, idx+x]
                    dfs(n+1, result+game[type][idx+x])
                    horse[i] = [type, idx]

game = [[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40],
        [10,13,16,19,25,30,35,40],
        [20,22,24,25,30,35,40],
        [30,28,27,26,25,30,35,40]]
arr = list(map(int, input().split()))
answer = 0
horse = [[0,0],[0,0],[0,0],[0,0]]
dfs(0,0)
print(answer)

# 두번째 풀이
'''
- 1차. 17:00 ~ 18:27 - 틀렸습니다 7%
- 2차. 28,27,26점인데 26,27,28점으로 씀 - 틀렸습니다 9%
- 3차. 도착지점 33 아니고 32임.. - 틀렸습니다 9%
- 4차. 38(idx=19)에서 40(idx=31)로 가야하는데 idx=32로 감.. (120384kb, 372ms)
- 5차. 앞으로 남은 턴에 40을 다 더해도 최대값 갱신을 못하면 가지치기 (372ms -> 196ms)
'''
def recur(n,horse,sm):
    global answer
    if sm+(N-n)*40 < answer:
        return
    elif n == N:
        answer = max(answer, sm)
        return
    for i,h in enumerate(horse):
        if h == 32: continue
        if len(graph[h]) > 1:
            next = graph[h][1]
        else:
            next = graph[h][0]

        for _ in range(int(arr[n])-1):
            next = graph[next][0]

        if next == 32 or next not in horse:
            horse[i] = next
            recur(n+1, horse, sm+score[next])
            horse[i] = h

# idx     0   1   2   3   4   5      6   7   8   9    10      11   12   13   14   15      16   17   18   19   20   21   22   23   24   25   26   27   28   29   30   31   32
score = [ 0,  2,  4,  6,  8,  10,    12, 14, 16, 18,  20,     22,  24,  26,  28,  30,     32,  34,  36,  38,  13,  16,  19,  22,  24,  28,  27,  26,  25,  30,  35,  40,  0]
graph = [[1],[2],[3],[4],[5],[6,20],[7],[8],[9],[10],[11,23],[12],[13],[14],[15],[16,25],[17],[18],[19],[31],[21],[22],[28],[24],[28],[26],[27],[28],[29],[30],[31],[32],[32]]
horse = [0]*4
arr = list(map(int, input().split()))
N = len(arr)
answer = 0
recur(0,horse,0)
print(answer)