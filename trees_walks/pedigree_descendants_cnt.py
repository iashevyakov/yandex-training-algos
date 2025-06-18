import sys
from collections import defaultdict

sys.setrecursionlimit(100000)

n = int(input())
parents_dict = {}
nodes = set()
childs_cnt_dict = {}
childs_dict = defaultdict(list)

for _ in range(n - 1):
    child, parent = input().split()
    childs_dict[parent].append(child)
    nodes.add(child)
    nodes.add(parent)


def get_childs_cnt(node: str):
    childs_cnt = 0
    childs = childs_dict.get(node, [])
    childs_cnt += len(childs)
    for child in childs:
        child_cnt = childs_cnt_dict.get(child)
        if child_cnt is None:
            child_cnt = get_childs_cnt(child)
            childs_cnt_dict[child] = child_cnt
        childs_cnt += child_cnt
    childs_cnt_dict[node] = childs_cnt
    return childs_cnt


for node in sorted(nodes):
    cnt = childs_cnt_dict.get(node, get_childs_cnt(node))
    print(node, cnt)