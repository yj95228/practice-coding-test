import sys
input = sys.stdin.readline

Q = int(input())
comm, N, M, *arr = map(int, input().split())
belt, gift = dict(), dict()
for b_num in range(1, N+1):
    belt[b_num] = [None, None, 0]   # [맨 앞 선물, 맨 뒤 선물, cnt]
for idx in range(1, M+1):
    b_num = arr[idx-1]
    belt[b_num][2] += 1
    if belt[b_num][0] is None: belt[b_num][0] = idx
    if belt[b_num][1] is None:
        belt[b_num][1] = idx
        gift[idx] = [None, None]
    else:
        prev_id = belt[b_num][1]
        belt[b_num][1] = idx
        gift[prev_id][1] = idx
        gift[idx] = [prev_id, None]

for _ in range(Q-1):
    comm, *arr = map(int, input().split())
    if comm == 200:
        src, dst = arr
        front, back, cnt = belt[src]
        front2, back2, cnt2 = belt[dst]
        belt[src] = [None, None, 0]
        if cnt:
            if cnt2:
                gift[front2][0] = back
            else:
                belt[dst][1] = back
            belt[dst][0], belt[dst][2] = front, cnt2+cnt
            gift[back][1] = front2
        print(cnt2+cnt)

    elif comm == 300:
        src, dst = arr
        front1, front2 = belt[src][0], belt[dst][0] # 3, None
        next1, next2 = None, None   # 2, None
        if front1 is not None: next1 = gift[front1][1]
        if front2 is not None: next2 = gift[front2][1]
        if front1 is not None: gift[front1][1] = next2
        if front2 is not None: gift[front2][1] = next1
        if next1 is not None: gift[next1][0] = front2
        if next2 is not None: gift[next2][0] = front1
        if front1 is None and front2 is not None:
            belt[src] = [front2, front2, 1]
            belt[dst][0] = next2
            belt[dst][2] -= 1
            if not belt[dst][2]: belt[dst][1] = None
        elif front1 is not None and front2 is None:
            belt[src][0] = next1
            belt[src][2] -= 1
            if not belt[src][2]: belt[src][1] = None
            belt[dst] = [front1, front1, 1]
        else:
            belt[src][0], belt[dst][0] = front2, front1
            if belt[src][2] == 1: belt[src][1] = belt[src][0]
            if belt[dst][2] == 1: belt[dst][1] = belt[dst][0]
        print(belt[dst][2])

    elif comm == 400:
        src, dst = arr
        n = belt[src][2]
        if n//2:
            start = belt[src][0]    # 5
            now = start
            for i in range(n//2):
                next = gift[now][1]   # 6
                now = next
            prev = gift[now][0]     # 5
            gift[now][0] = None
            front = belt[dst][0]    # 2
            if front is not None: gift[front][0] = prev
            gift[prev][1] = front
            belt[src][0] = now
            belt[dst][0] = start
            if belt[dst][1] is None: belt[dst][1] = prev
            belt[src][2] -= n//2
            belt[dst][2] += n//2
        print(belt[dst][2])

    elif comm == 500:
        p_num = arr[0]
        a, b = gift[p_num]
        if a is None: a = -1
        if b is None: b = -1
        print(a+2*b)

    elif comm == 600:
        b_num = arr[0]
        a, b, c = belt[b_num]
        if a is None: a = -1
        if b is None: b = -1
        print(a+2*b+3*c)