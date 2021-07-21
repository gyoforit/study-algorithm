# 재귀 깊이 제한 설정
import sys
sys.setrecursionlimit(10**6)

def preorder(ans, x, tree):
    if x:
        ans.append(x)
        preorder(ans, tree[x][0], tree)
        preorder(ans, tree[x][1], tree)
    return ans

def postorder(ans, x, tree):
    if x:
        postorder(ans, tree[x][0], tree)
        postorder(ans, tree[x][1], tree)
        ans.append(x)
    return ans

# 이진 트리 구현해서 전위/후위 순회
def solution(nodeinfo):
    new_nodeinfo = [(0, 0, 0)]+[(i + 1, nodeinfo[i][0], nodeinfo[i][1]) for i in range(len(nodeinfo))]
    # 위에서부터 연결해나가기 위해 y좌표가 큰 순서대로 정렬
    nodes = sorted([(i + 1, nodeinfo[i][0], nodeinfo[i][1]) for i in range(len(nodeinfo))], key=lambda x: -x[2])
    # 인덱스가 부모, 해당하는 값은 양쪽자식들
    binarytree = [[0, 0] for _ in range(len(nodeinfo) + 1)]
    for i in range(1, len(nodeinfo)):
        target = nodes[i]
        first = nodes[0]
        # x 값이 모두 다르다는 점을 활용
        while True:
            if target[1] < first[1]:
                tmp = binarytree[first[0]][0]
                if not tmp:
                    binarytree[first[0]][0] = target[0]
                    break
                first = new_nodeinfo[tmp]
            else:
                tmp = binarytree[first[0]][1]
                if not tmp:
                    binarytree[first[0]][1] = target[0]
                    break
                first = new_nodeinfo[tmp]
    pre = preorder([], nodes[0][0], binarytree)
    post = postorder([], nodes[0][0], binarytree)
    return [pre, post]

print(solution([[5,3]]))