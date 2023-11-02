# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AWXRFInKex8DFAUo&probBoxId=AYpJUI9690oDFAQI+&type=PROBLEM&problemBoxTitle=28_230831%3A+%EC%8B%A4%EC%A0%84%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC&problemBoxCnt=++4+
# 상하끼리, 좌우끼리만 부딪히는 경우만 생각해서 2000 -> 4000으로 수정
# TODO: 리스트말고 딕셔너리로 하는게 더 나은 듯 함
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    answer = 0
    obj = {}
    for _ in range(N):
        x, y, d, K = map(int, input().split())
        obj[(2*x,2*y)] = [(d,K)]
    dx, dy = [0,0,-1,1], [1,-1,0,0]
    for _ in range(4000):
        new = {}
        crush = set()
        for x,y in obj.keys():
            for d, K in obj[(x,y)]:
                nx, ny = x+dx[d], y+dy[d]
                if (nx,ny) in new:
                    new[(nx,ny)] = [*new[(nx,ny)], (d,K)]
                    crush.add((nx,ny))
                else:
                    new[(nx,ny)] = [(d,K)]
        for x,y in crush:
            answer += sum(k for _, k in new[(x,y)])
            del new[(x,y)]
        if not len(new.keys()): break
        obj = new
    print(f'#{tc} {answer}')

# 2차 풀이
T = int(input())
dt = ((0,1),(0,-1),(-1,0),(1,0))
for tc in range(1, T+1):
    N = int(input())
    obj = dict()
    for _ in range(N):
        x, y, d, k = map(int, input().split())
        obj[(2*x, 2*y)] = [(d, k)]

    answer = 0
    for _ in range(4000):
        nobj = dict()
        crash = set()
        for (r, c), value in obj.items():
            for d, k in value:
                dx, dy = dt[d]
                nx, ny = r+dx, c+dy
                if nobj.get((nx, ny)):
                    crash.add((nx, ny))
                    nobj[(nx, ny)].append((d, k))
                else:
                    nobj[(nx, ny)] = [(d, k)]

        if crash:
            for r, c in crash:
                for _, k in nobj[(r, c)]:
                    answer += k
                del nobj[(r, c)]

        if not nobj: break
        obj = nobj

    print(f'#{tc} {answer}')