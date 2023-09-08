# https://www.acmicpc.net/problem/14891
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 톱니바퀴 A를 회전할 때, 그 옆에 있는 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면, B는 A가 회전한 방향과 반대방향으로 회전하게 된다.
def rotate(num, dir, left_right = None):
    # 오른쪽
    if num <= 3 and left_right != 'left':
        if wheels[num-1][2] != wheels[num][6]:
            # 오른쪽 톱니바퀴 dir과 반대방향 회전
            rotate(num+1, -dir, 'right')
    # 왼쪽
    if num >= 2 and left_right != 'right':
        if wheels[num-1][6] != wheels[num-2][2]:
            # 왼쪽 톱니바퀴 dir과 반대방향 회전
            rotate(num-1, -dir, 'left')
    # 자기 자신
    # 시계방향
    if dir == 1:
        wheels[num-1] = [wheels[num-1].pop()] + wheels[num-1]
    # 반시계방향
    else:
        wheels[num-1] = wheels[num-1][1:] + [wheels[num-1][0]]

wheels = [list(input().rstrip()) for _ in range(4)]
# 총 K번 회전
K = int(input())
for _ in range(K):
    # 1이 시계방향, -1이 반시계방향
    num, dir = map(int, input().split())
    rotate(num, dir)

answer = 0
for a, b in zip([int(wheel[0]) for wheel in wheels],[1,2,4,8]):
    answer += a*b
print(answer)