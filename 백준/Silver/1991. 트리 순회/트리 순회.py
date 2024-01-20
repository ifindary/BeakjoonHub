import sys
input = sys.stdin.readline

def preorder(node): # 전위 순회
    if node != '.':
        print(node, end='')
        preorder(tree[node][0])
        preorder(tree[node][1])
    
def inorder(node): # 중위 순회
    if node != '.':
        inorder(tree[node][0])
        print(node, end='')
        inorder(tree[node][1])

def postorder(node): # 후위 순회
    if node != '.':
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end='')


n = int(input())
tree = {} # 딕셔너리 이용

for _ in range(n):
    data, left, right = input().split()
    tree[data] = [left, right]

# 항상 A가 루트 노드
preorder('A')
print()
inorder('A')
print()
postorder('A')