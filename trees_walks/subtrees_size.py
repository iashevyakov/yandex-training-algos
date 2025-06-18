import sys
from collections import defaultdict

sys.setrecursionlimit(100000)

v = int(input())

matrix = defaultdict(list)
for _ in range(v - 1):
    v1, v2 = tuple(map(int, input().split()))
    matrix[v1].append(v2)
    matrix[v2].append(v1)

subtrees_sizes = {}
visited = set()


def visit_vertices(root: int):
    visited.add(root)
    v_subtree_members_cnt = 1
    for cur_v in matrix[root]:
        if cur_v not in visited:
            cnt = visit_vertices(cur_v)
            v_subtree_members_cnt += cnt
        elif cur_v in subtrees_sizes:
            cnt = subtrees_sizes[cur_v]
            v_subtree_members_cnt += cnt

    subtrees_sizes[root] = v_subtree_members_cnt
    return v_subtree_members_cnt


for i in range(1, v + 1):
    if i not in visited:
        visit_vertices(i)
    print(subtrees_sizes[i], end=' ')