# https://www.acmicpc.net/problem/1991
from sys import stdin
stdin = open('input.txt','r')
input = stdin.readline

def preorder(root):
    if root != '.':
        print(root, end='')
        left, right = tree[root]
        preorder(left)
        preorder(right)

def inorder(root):
    if root != '.':
        left, right = tree[root]
        inorder(left)
        print(root, end='')
        inorder(right)

def postorder(root):
    if root != '.':
        left, right = tree[root]
        postorder(left)
        postorder(right)
        print(root, end='')

N = int(input())
tree = dict()
for _ in range(N):
    A, B, C = input().split()
    tree[A] = [B, C]
preorder('A')
print()
inorder('A')
print()
postorder('A')