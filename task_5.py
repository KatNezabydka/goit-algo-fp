"""
Завдання 5. Візуалізація обходу бінарного дерева

Використовуючи код із завдання 4 для побудови бінарного дерева, необхідно створити програму на Python,
 яка візуалізує обходи дерева: у глибину та в ширину.

Вона повинна відображати кожен крок у вузлах з різними кольорами, використовуючи 16-систему RGB (приклад #1296F0).
 Кольори вузлів мають змінюватися від темних до світлих відтінків, залежно від послідовності обходу.
 Кожен вузол при його відвідуванні має отримувати унікальний колір, який візуально відображає порядок обходу.
"""
import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def dfs_traversal(node, visited, colors):
    if node is None:
        return

    visited.add(node.id)
    colors[node.id] = len(visited) / 10

    dfs_traversal(node.left, visited, colors)
    dfs_traversal(node.right, visited, colors)

def bfs_traversal(node, visited, colors):
    if node is None:
        return

    queue = [node]
    while queue:
        current_node = queue.pop(0)
        visited.add(current_node.id)
        colors[current_node.id] = len(visited) / 10

        if current_node.left and current_node.left.id not in visited:
            queue.append(current_node.left)
        if current_node.right and current_node.right.id not in visited:
            queue.append(current_node.right)

def draw_tree(root, traversal_type):
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    tree = add_edges(tree, root, pos)

    visited = set()
    colors = {}

    if traversal_type == 'DFS':
        dfs_traversal(root, visited, colors)
    elif traversal_type == 'BFS':
        bfs_traversal(root, visited, colors)

    node_colors = [colors[node_id] for node_id in tree.nodes()]

    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors, cmap='plasma')
    plt.title(f'{traversal_type} Traversal')
    plt.show()

root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)

draw_tree(root, 'DFS')

draw_tree(root, 'BFS')
