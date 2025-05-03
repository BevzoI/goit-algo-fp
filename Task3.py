import heapq

def dijkstra(graph, start):
    # Ініціалізація відстаней: нескінченність для всіх вершин, крім стартової
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # Мінімальна купа: (відстань, вершина)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Пропускаємо, якщо вже знайшли коротший шлях
        if current_distance > distances[current_vertex]:
            continue

        # Перевірка сусідів
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Якщо знайдено коротший шлях до сусіда — оновлюємо
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6}
}

start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)

for vertex in sorted(shortest_paths):
    print(f"Найкоротший шлях від {start_vertex} до {vertex}: {shortest_paths[vertex]}")
