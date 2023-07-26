# https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=python3
def solution(nums):
    return min(int(len(nums)/2), len(set(nums)))