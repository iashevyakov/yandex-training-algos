parents_dict = {}
requests = []


def get_all_parents(node: str):
    parents = set()
    parents.add(node)
    child = node
    while child in parents_dict:
        child = parents_dict[child]
        parents.add(child)
    return parents


with open('input.txt') as f:
    n = int(f.readline())
    for i, line in enumerate(f.readlines()):
        node_1, node_2 = line.split()
        if i < n - 1:
            parents_dict[node_1] = node_2
        else:
            requests.append((node_1, node_2))

with open('output.txt', 'a') as f:
    for child_1, child_2 in requests:
        parents_1 = get_all_parents(child_1)
        if child_2 in parents_1:
            f.write(f"{child_2}\n")
        else:
            child = child_2
            while child in parents_dict:
                child = parents_dict[child]
                if child in parents_1:
                    f.write(f"{child}\n")
                    break