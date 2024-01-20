import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
    
def preorder(node): # 전위 순회
    print(node.data, end='')
    if node.left != '.': preorder(tree[node.left])
    if node.right != '.': preorder(tree[node.right])
    
def inorder(node): # 중위 순회
    if node.left != '.': inorder(tree[node.left])
    print(node.data, end='')
    if node.right != '.': inorder(tree[node.right])

def postorder(node): # 후위 순회
    if node.left != '.': postorder(tree[node.left])
    if node.right != '.': postorder(tree[node.right])
    print(node.data, end='')


n = int(input())
tree = {} # 딕셔너리 이용

for _ in range(n):
    data, left, right = input().split()
    tree[data] = Node(data, left, right)

# 항상 A가 루트 노드
preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])