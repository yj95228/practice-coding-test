# FIXME: 가장 먼저 벨트에 올라간 로봇부터 라는 조건을 고려하지 않음
# TODO: count() 함수는 느리다
# https://www.acmicpc.net/problem/20055
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
robot = []
answer = 1

while True:
    # [1] 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    arr = [arr[-1]] + arr[:-1]
    robot = list(map(lambda x: (x+1)%(2*N-1), robot))
    if N-1 in robot: robot.remove(N-1)

    # [2] 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동
    for i in range(len(robot)):
        next = (robot[i]+1)%(2*N-1)
        if next not in robot and arr[next] >= 1:
            arr[next] -= 1
            robot[i] = next
    if N-1 in robot: robot.remove(N-1)

    # [3] 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if arr[0] > 0:
        robot.append(0)
        arr[0] -= 1

    # [4] 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다
    cnt = 0
    for x in arr:
        if x == 0: cnt += 1
    if cnt >= K:
        print(answer)
        break

    answer += 1