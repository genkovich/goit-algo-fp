from graph_generator import generate_fb_friends
import heapq
import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(graph, start):
    # Ініціалізація відстаней до всіх вершин як "нескінченність"
    shortest_paths = {vertex: float('infinity') for vertex in graph.nodes}
    shortest_paths[start] = 0

    # Ініціалізація черги з пріоритетом (бінарна купа)
    priority_queue = [(0, start)]
    heapq.heapify(priority_queue)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо відстань в черзі більша, ніж вже відома - пропускаємо
        if current_distance > shortest_paths[current_vertex]:
            continue

        # Огляд сусідів поточної вершини
        for neighbor, attributes in graph[current_vertex].items():
            weight = attributes['weight']
            distance = current_distance + weight

            # Якщо знайдений коротший шлях до сусіда - оновлюємо і додаємо в чергу
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths


def main():
    main_account = "Your Account"
    fb_graph, friend_for_search = generate_fb_friends(main_account)

    print(f"Випадковий друг для пошуку: {friend_for_search}")

    # Застосовуємо алгоритм Дейкстри для пошуку найкоротших шляхів від головного акаунта
    shortest_paths = dijkstra(fb_graph, main_account)

    # Виводимо найкоротший шлях до вибраного друга
    print(f"Найкоротший шлях від '{main_account}' до '{friend_for_search}': {shortest_paths[friend_for_search]}")

    # Візуалізація графа
    pos = nx.spring_layout(fb_graph)
    nx.draw(fb_graph, pos, with_labels=True, node_size=1200, font_size=6)
    edge_labels = nx.get_edge_attributes(fb_graph, 'weight')
    nx.draw_networkx_edge_labels(fb_graph, pos, edge_labels=edge_labels)
    plt.show()


if __name__ == "__main__":
    main()
