"""
Task 3
Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі,
 використовуючи бінарну купу.
  Завдання включає створення графа, використання піраміди для оптимізації вибору вершин
  та обчислення найкоротших шляхів від початкової вершини до всіх інших.
"""
import networkx as nx
import matplotlib.pyplot as plt
import heapq


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # Бінарна купа (піраміда)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)  # Отримання вершини з найменшою відстанню

        if current_distance > distances[current_vertex]:
            continue  # Пропускаємо вершини, які мають більшу відстань

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))  # Додаємо сусідню вершину у бінарну купу

    return distances


def print_table(distances, visited):
    # Верхній рядок таблиці
    print("{:<10} {:<10} {:<10}".format("Вершина", "Відстань", "Перевірено"))
    print("-" * 30)

    # Вивід даних для кожної вершини
    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(distance)

        status = "Так" if vertex in visited else "Ні"
        print("{:<10} {:<10} {:<10}".format(vertex, distance, status))
    print("\n")

G = nx.Graph()
G.add_edge('A', 'B', weight=1)
G.add_edge('A', 'С', weight=4)
G.add_edge('B', 'A', weight=1)
G.add_edge('B', 'C', weight=2)
G.add_edge('B', 'D', weight=5)
G.add_edge('C', 'A', weight=4)
G.add_edge('C', 'B', weight=2)
G.add_edge('C', 'D', weight=1)
G.add_edge('D', 'B', weight=5)
G.add_edge('D', 'C', weight=1)

pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=15, width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
shortest_distances = dijkstra(graph, start_vertex)
print_table(shortest_distances, list(graph.keys()))

plt.show()
