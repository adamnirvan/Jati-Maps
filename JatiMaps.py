# Import library yang diperlukan
import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations
import heapq
import random

# Mapping nama kota
nama_kota = {
    "Kota_1": "Surabaya",
    "Kota_2": "Jakarta",
    "Kota_3": "Bandung",
    "Kota_4": "Yogyakarta",
    "Kota_5": "Semarang",
    "Kota_6": "Malang",
    "Kota_7": "Medan",
    "Kota_8": "Palembang",
    "Kota_9": "Makassar",
    "Kota_10": "Bali"
}

# Membuat kelas Graph untuk merepresentasikan graf
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, u, v, weight):
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))

    def dijkstra(self, start, end):
        distances = {vertex: float('inf') for vertex in self.adj_list}
        previous = {vertex: None for vertex in self.adj_list}
        distances[start] = 0
        queue = [(0, start)]

        while queue:
            current_distance, current_vertex = heapq.heappop(queue)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in self.adj_list[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(queue, (distance, neighbor))

        path = []
        current = end
        while current is not None:
            path.insert(0, current)
            current = previous[current]

        return path, distances[end]

    def tsp_brute_force(self):
        vertices = list(self.adj_list.keys())
        min_path = None
        min_distance = float('inf')

        for perm in permutations(vertices):
            total_dist = 0
            valid = True
            for i in range(len(perm) - 1):
                found = False
                for neighbor, weight in self.adj_list[perm[i]]:
                    if neighbor == perm[i + 1]:
                        total_dist += weight
                        found = True
                        break
                if not found:
                    valid = False
                    break

            if valid and total_dist < min_distance:
                min_distance = total_dist
                min_path = perm

        return min_path, min_distance

# Membuat graf dengan 10 vertex dan 30 edge
kota = [f"Kota_{i}" for i in range(1, 11)]
graf = Graph()
for k in kota:
    graf.add_vertex(k)

edges_added = set()
while len(edges_added) < 30:
    u, v = random.sample(kota, 2)
    if u != v and (u, v) not in edges_added and (v, u) not in edges_added:
        w = random.randint(10, 100)  # bobot antara 10-100 km
        graf.add_edge(u, v, w)
        edges_added.add((u, v))

# Fungsi untuk memvisualisasikan graf
def visualize_graph(graph, path=None):
    G = nx.Graph()
    for u in graph.adj_list:
        for v, w in graph.adj_list[u]:
            if (v, u) not in G.edges:
                G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    if path:
        edge_path = [(path[i], path[i+1]) for i in range(len(path)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=edge_path, edge_color='red', width=2)

    plt.show()

# Antarmuka Pengguna
print("\n--- Daftar Kota ---")
for k in kota:
    print(f"{k}: {nama_kota[k]}")

asal = input("Masukkan kota asal (misal: Kota_1): ")
tujuan = input("Masukkan kota tujuan (misal: Kota_5): ")

# Menjalankan Dijkstra
path, total = graf.dijkstra(asal, tujuan)
path_nama = [nama_kota[k] for k in path]
print(f"\nJalur tercepat dari {nama_kota[asal]} ke {nama_kota[tujuan]}: {path_nama}")
print(f"Total jarak tempuh: {total} km")

# Visualisasi hasil Dijkstra
visualize_graph(graf, path=path)

# Menjalankan TSP
print("\nMenjalankan TSP (brute-force)... Mohon tunggu beberapa saat...")
tsp_path, tsp_total = graf.tsp_brute_force()
tsp_path_nama = [nama_kota[k] for k in tsp_path]
print(f"Rute TSP terbaik: {tsp_path_nama}")
print(f"Total jarak tempuh TSP: {tsp_total} km")
