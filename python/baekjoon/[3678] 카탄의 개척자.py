import sys
input = sys.stdin.readline

def play(nx, ny, nd):
    global r, c, d
    s = [1,2,3,4,5]
    for ddx, ddy in ((1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1)):
        nnx, nny = nx+ddx, ny+ddy
        if obj.get((nnx, nny)):
            num = obj.get((nnx, nny))
            if num in s: s.remove(obj.get((nnx, nny)))
    mn, num = 987654321, 0
    for x in s:
        if cnt[x] < mn:
            mn, num = cnt[x], x
    obj[(nx, ny)] = num
    cnt[num] += 1
    snail.append(num)
    r, c, d = nx, ny, nd

T = int(input())
arr = [int(input()) for _ in range(T)]
mx = max(arr)
snail = [1,2]
obj = {(0,0):1,(-1,0):2}
cnt = [0,1,1,0,0,0,0]
dt = ((0,-1),(1,0),(1,1),(0,1),(-1,0),(-1,-1))
r, c, d, = -1, 0, -1
for _ in range(mx-2):
    dx, dy = dt[(d+1)%6]
    nx, ny = r+dx, c+dy
    if not obj.get((nx, ny)):
        play(nx, ny, (d+1)%6)
    else:
        dx, dy = dt[d]
        nx, ny = r+dx, c+dy
        play(nx, ny, d)
for x in arr:
    print(snail[x-1])