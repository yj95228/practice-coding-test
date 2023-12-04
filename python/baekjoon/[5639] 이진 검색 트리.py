import sys

input = sys.stdin.readline


def pre_to_post(left, right):
    if left > right: return
    root = pre[left]
    idx = None
    for i, v in enumerate(pre[left + 1:], start=left + 1):
        if v > root:
            idx = i
            break
    if idx is None: idx = right + 1
    pre_to_post(left + 1, idx - 1)
    pre_to_post(idx, right)
    print(root)


pre = []
while True:
    try:
        pre.append(int(input()))
    except:
        break
sys.setrecursionlimit(2 * 10 ** 5)
pre_to_post(0, len(pre) - 1)