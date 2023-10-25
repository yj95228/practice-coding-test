# https://www.acmicpc.net/problem/16434
from sys import stdin
input = stdin.readline

def check(max_hp):
    hp = max_hp
    tmp_attack = attack
    for turn in range(N):
        T, A, H = lst[turn]
        if T == 1:
            if H%tmp_attack:
                time = H//tmp_attack
            else:
                time = H//tmp_attack-1
            damage = A*time
            if hp <= damage:
                return False
            else:
                hp -= damage
        else:
            tmp_attack += A
            hp = min(max_hp, hp+H)
    return True

N, attack = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
answer = 1_000_000*1_000_000*N
left, right = 0, answer
while left <= right:
    mid = (left+right)//2
    if check(mid):
        answer = min(answer, mid)
        right = mid-1
    else:
        left = mid+1
print(answer)