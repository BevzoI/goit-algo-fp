import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color

def heap_to_tree(heap):
    if not heap:
        return None

    # Автозабарвлення вузлів на основі значень (мінімальне — зелене, максимальне — червоне)
    min_val, max_val = min(heap), max(heap)
    def get_color(val):
        if max_val == min_val:
            return "skyblue"
        ratio = (val - min_val) / (max_val - min_val)
        return f"#{int(255 * ratio):02x}{int(255 * (1 - ratio)):02x}80"  # градієнт від зелено-червоного

    nodes = [Node(val, get_color(val)) for val in heap]

    for i in range(len(heap)):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(heap):
            nodes[i].left = nodes[left]
        if right < len(heap):
            nodes[i].right = nodes[right]
    
    return nodes[0]

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        pos[node.val] = (x, y)
        graph.add_node(node.val, pos=(x, y), layer=layer, color=node.color)
        if node.left is not None:
            dx = 1 / layer
            graph.add_edge(node.val, node.left.val)
            add_edges(graph, node.left, pos, x - dx, y - 1, layer + 1)
        if node.right is not None:
            dx = 1 / layer
            graph.add_edge(node.val, node.right.val)
            add_edges(graph, node.right, pos, x + dx, y - 1, layer + 1)
    return graph

def draw_tree(tree_root):
    graph = nx.DiGraph()
    pos = {}
    tree = add_edges(graph, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]

    plt.figure(figsize=(12, 8))
    nx.draw(tree, pos=nx.get_node_attributes(tree, 'pos'),
            with_labels=True, arrows=False,
            node_size=2500, node_color=colors, font_weight='bold')
    plt.show()

# 🟦 Приклад купи (мін-купа)
heap_array = [1, 3, 5, 7, 9, 11, 13]

# Побудова дерева та візуалізація
heap_tree_root = heap_to_tree(heap_array)
draw_tree(heap_tree_root)
