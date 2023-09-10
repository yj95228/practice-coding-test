# FIXME: 날짜 변경될때 반올림되는 경우와 0이 되는 경우 고려해야 함
# https://www.acmicpc.net/problem/29722
import sys
input = sys.stdin.readline

yyyy, mm, dd = map(int, input().split('-'))
N = int(input())
year, days = divmod(N,360)
month, day = divmod(days,30)
if dd+day > 30:
    day -= 30
    month += 1
if mm+month > 12:
    month -= 12
    year += 1
year += yyyy
month += mm
day += dd
print(f'{year}-{(12 if month == 0 else "0"+str(month)) if month < 10 else month}-{(30 if day == 0 else "0"+str(day)) if day < 10 else day}')