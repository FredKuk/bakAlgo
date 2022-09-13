def preOrder(tree:list,now:int):
    if now>26 or chr(now+ord('A')-1)=='.': return
    tree[0].append(chr(ord('A')+now-1))
    preOrder(tree,ord(tree[now][0])-ord('A')+1)
    preOrder(tree,ord(tree[now][1])-ord('A')+1)

def inOrder(tree:list,now:int):
    if now>26 or chr(now+ord('A')-1)=='.': return
    inOrder(tree,ord(tree[now][0])-ord('A')+1)
    tree[0].append(chr(ord('A')+now-1))
    inOrder(tree,ord(tree[now][1])-ord('A')+1)

def postOrder(tree:list,now:int):
    if now>26 or chr(now+ord('A')-1)=='.': return
    postOrder(tree,ord(tree[now][0])-ord('A')+1)
    postOrder(tree,ord(tree[now][1])-ord('A')+1)
    tree[0].append(chr(ord('A')+now-1))

def main():

    n=int(input())
    tree=[ [] for _ in range(27)]
    std = ord('A')
    for _ in range(n):
        node, child1, child2=map(str,input().split(" "))
        tree[ord(node)-std+1].append(child1)
        tree[ord(node)-std+1].append(child2)
    preOrder(tree,1)
    print("".join(tree[0]))
    tree[0]=[]
    inOrder(tree,1)
    print("".join(tree[0]))
    tree[0]=[]
    postOrder(tree,1)
    print("".join(tree[0]))
if __name__ =="__main__":
    main()

# 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
# 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
# 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
#
# 입력
# 첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다.
# 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다.
# 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.
#
# 출력
# 첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.
#
# 7
# A B C
# B D .
# C E F
# E . .
# F . G
# D . .
# G . .
#
# ABDCEFG
# DBAECFG
# DBEGFCA