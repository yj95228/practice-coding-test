# https://school.programmers.co.kr/learn/courses/30/lessons/84512?language=python3
import itertools

def solution(word):
    character = ['','A','E','I','O','U']
    dictionary = set()
    for i in range(5):
        dictionary.update(
            map(
                lambda x: ''.join(x),
                itertools.product(character, repeat=i+1)
           )
        )
    return sorted(dictionary).index(word)
