import matplotlib
matplotlib.use('Agg')  # 👈 Вимикає tkinter

import os
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "#cccccc"  # початковий колір

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        pos[node.val] = (x, y)
        graph.add_node(node.val, pos=(x, y), color=node.color)
        if node.left:
            dx = 1 / layer
            graph.add_edge(node.val, node.left.val)
            add_edges(graph, node.left, pos, x - dx, y - 1, layer + 1)
        if node.right:
            dx = 1 / layer
            graph.add_edge(node.val, node.right.val)
            add_edges(graph, node.right, pos, x + dx, y - 1, layer + 1)
    return graph

def draw_tree_step(tree_root, visited_nodes_colors, step_num, mode):
    os.makedirs("output", exist_ok=True)

    graph = nx.DiGraph()
    pos = {}
    graph = add_edges(graph, tree_root, pos)

    for node_val, color in visited_nodes_colors.items():
        graph.nodes[node_val]['color'] = color

    colors = [data['color'] for _, data in graph.nodes(data=True)]

    plt.figure(figsize=(10, 6))
    nx.draw(graph, pos=nx.get_node_attributes(graph, 'pos'),
            with_labels=True, arrows=False, node_color=colors,
            node_size=2500, font_weight='bold')
    
    plt.title(f"{mode} Step {step_num}")
    filename = f"output/{mode.lower()}_step_{step_num:02d}.png"
    plt.savefig(filename)
    plt.close()

def generate_color_gradient(n, base_color="#1296F0"):
    base_r = int(base_color[1:3], 16)
    base_g = int(base_color[3:5], 16)
    base_b = int(base_color[5:7], 16)

    gradient = []
    for i in range(n):
        factor = 0.4 + 0.6 * (i / max(1, n - 1))
        r = int(base_r * factor)
        g = int(base_g * factor)
        b = int(base_b * factor)
        color = f"#{r:02x}{g:02x}{b:02x}"
        gradient.append(color)
    return gradient

def bfs(root):
    print("Обхід у ширину (BFS):")
    queue = deque([root])
    visited = set()
    visited_colors = {}
    color_list = generate_color_gradient(20, "#1296F0")
    i = 0

    while queue:
        node = queue.popleft()
        if node.val not in visited:
            visited.add(node.val)
            visited_colors[node.val] = color_list[i % len(color_list)]
            draw_tree_step(root, visited_colors, i + 1, "BFS")
            i += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

def dfs(root):
    print("Обхід у глибину (DFS):")
    stack = [root]
    visited = set()
    visited_colors = {}
    color_list = generate_color_gradient(20, "#F012BE")
    i = 0

    while stack:
        node = stack.pop()
        if node.val not in visited:
            visited.add(node.val)
            visited_colors[node.val] = color_list[i % len(color_list)]
            draw_tree_step(root, visited_colors, i + 1, "DFS")
            i += 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

# Створення дерева
root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)

# Запуск обходів
bfs(root)
dfs(root)
