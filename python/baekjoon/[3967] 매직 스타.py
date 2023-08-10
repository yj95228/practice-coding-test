# https://www.acmicpc.net/problem/3967
# 순서가 유의미하므로 순열 O(N!)
# 나왔던게 다시 못 나오므로 중복순열 X
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def check(arr):
    if 26 == arr[0]+arr[2]+arr[5]+arr[7]\
    == arr[7]+arr[8]+arr[9]+arr[10]\
    == arr[0]+arr[3]+arr[6]+arr[10]\
    == arr[1]+arr[2]+arr[3]+arr[4]\
    == arr[1]+arr[5]+arr[8]+arr[11]\
    == arr[4]+arr[6]+arr[9]+arr[11]: return True
    else: return False

def dfs(arr):
    if 0 not in arr:
        if check(arr):
            return arr
    else:
        idx = arr.index(0)
        for x in range(1,13):
            if x not in arr:
                arr[idx] = x
                if dfs(arr): return arr
                arr[idx] = 0

star = [list(filter(lambda x: x != '', input().strip().split('.'))) for _ in range(5)]
star = [x for row in star for x in row]
star = list(map(lambda x: 0 if ord(x) == 120 else ord(x)-64, star))
x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12 = list(map(lambda x: chr(x+64), dfs(star)))
print(f'....{x1}....')
print(f'.{x2}.{x3}.{x4}.{x5}.')
print(f'..{x6}...{x7}..')
print(f'.{x8}.{x9}.{x10}.{x11}.')
print(f'....{x12}....')

# 강사님 코드
s_map = [list(input().rstrip()) for _ in range(5)]
pos_list = []
check_pos_list = [(1,1),(3,1),(0,4),(1,7),(1,1),(0,4)]
dr = (0,0,1,1,1,1)
dc = (2,2,-1,-1,1,1)

def solve():
    input_set = set()
    for r in range(5):
        for c in range(9):
            if s_map[r][c] == 'x':
                pos_list.append((r,c))
            elif s_map != '.':
                input_set.add(s_map[r][c])

    target_list = list(set(['A','B','C','D','E','F','G','H','I','J','K','L'])-input_set)
    target_list.sort()

    permutation(target_list, [0]*len(target_list),0)

def permutation(target_list, is_selected, cnt):
    if not is_success(): return False
    if cnt == len(target_list):
        for r in range(5):
            print(''.join(s_map[r]))
        return True

    r,c = pos_list[cnt]
    for i in range(len(target_list)):
        if is_selected[i]: continue
        is_selected[i] = 1
        s_map[r][c] = target_list[i]
        if permutation(target_list, is_selected, cnt+1): return True
        is_selected[i] = 0
        s_map[r][c] = 'x'
    return False

def is_success():
    for d in range(6):
        r, c = check_pos_list[d]
        total, cnt = 0, 0
        for i in range(4):
            nr = r+i*dr[d]
            nc = c+i*dc[d]
            if s_map[nr][nc] == 'x': continue
            total += ord(s_map[nr][nc])-ord('A')+1
            cnt += 1
        if cnt == 4 and total != 26: return False
    return True