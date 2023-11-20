(x1, y1), (x2, y2), (x3, y3) = [list(map(int, input().split())) for _ in range(3)]
Z = (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)
print(0 if not Z else 1 if Z > 0 else -1)