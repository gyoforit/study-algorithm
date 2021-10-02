import sys
sys.stdin = open('input.txt')
def preorder(x):
    if x >= 0:
        order.append(num_dict[x])
        preorder(binary_tree[x][0])
        preorder(binary_tree[x][1])

def inorder(x):
    if x >= 0:
        inorder(binary_tree[x][0])
        order.append(num_dict[x])
        inorder(binary_tree[x][1])

def postorder(x):
    if x >= 0:
        postorder(binary_tree[x][0])
        postorder(binary_tree[x][1])
        order.append(num_dict[x])

T = int(input())
a_dict = dict()
num_dict = dict()
for i in range(T):
    a_dict[chr(i+65)] = i
    num_dict[i] = chr(i+65)
binary_tree = [list() for _ in range(T)]
for i in range(T):
    node, ch1, ch2 = input().split()
    target1 = ord(ch1)-65 if ch1 != '.' else -1
    binary_tree[a_dict[node]].append(target1)
    target2 = ord(ch2)-65 if ch2 != '.' else -1
    binary_tree[a_dict[node]].append(target2)
order = []

preorder(0)
print(''.join(order))
order.clear()
inorder(0)
print(''.join(order))
order.clear()
postorder(0)
print(''.join(order))