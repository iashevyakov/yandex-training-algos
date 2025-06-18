from typing import Optional, IO


class Node:
    key: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None

    def __init__(self, key: int, left: Optional["Node"] = None, right: Optional["Node"] = None):
        self.key = key
        self.left = left
        self.right = right


def print_tree(node: Node, level: int, out_f: IO):
    if node is None:
        return

    print_tree(node.left, level + 1, out_f)

    for i in range(0, level):
        out_f.write(".")

    out_f.write(f"{node.key}\n")

    print_tree(node.right, level + 1, out_f)


def add_node(root: Optional[Node], key: int, out_f: IO) -> Node:
    if root is None:
        root = Node(key=key)
        out_f.write("DONE\n")
    else:
        node = root
        while node.key != key:
            if key < node.key:
                if node.left is None:
                    node.left = Node(key=key)
                    out_f.write("DONE\n")
                    break
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = Node(key=key)
                    out_f.write("DONE\n")
                    break
                else:
                    node = node.right
        else:
            out_f.write("ALREADY\n")
    return root


def search_node(root: Node, key: int, out_f: IO):
    if root is None:
        out_f.write("NO\n")
        return
    node = root
    while node.key != key:
        if key < node.key:
            if node.left is None:
                out_f.write("NO\n")
                break
            else:
                node = node.left
        else:
            if node.right is None:
                out_f.write("NO\n")
                break
            else:
                node = node.right
    else:
        out_f.write("YES\n")


with open('input.txt') as f:
    root = None
    reqs = f.readlines()
    with open('output.txt', 'a') as out_f:
        for req in reqs:
            if req.startswith('ADD'):
                key = req.split(' ')[1]
                root = add_node(root, int(key), out_f)
            elif req.startswith('SEARCH'):
                key = req.split(' ')[1]
                search_node(root, int(key), out_f)
            else:
                print_tree(root, 0, out_f)