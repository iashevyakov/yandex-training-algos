n = int(input())
parents_dict = {}
nodes = set()

for _ in range(n - 1):
    child, parent = input().split()
    parents_dict[child] = parent
    nodes.add(child)
    nodes.add(parent)

heights = {}
for node in nodes:
    height = 0
    child = node
    while child in parents_dict:
        height += 1
        child = parents_dict[child]
    heights[node] = height

for node, height in sorted(heights.items()):
    print(node, height)