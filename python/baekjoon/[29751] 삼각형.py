import sys
input = sys.stdin.readline

W, H = map(int, input().split())
print(f'{W*H/2:.1f}')