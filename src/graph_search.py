import heapq
from collections import defaultdict

def build_graph(edges):
    """Convierte la lista de edges en un grafo usable."""
    graph = defaultdict(list)
    for u, v, t, line in edges:
        graph[u].append((v, t, line))
        graph[v].append((u, t, line))  # bidireccional
    return graph

def dijkstra_time(graph, start, goal, transfer_penalty=0.0):
    """
    Algoritmo de Dijkstra con penalización por transbordo de línea.
    Devuelve el tiempo y el camino tomado.
    """
    pq = []
    heapq.heappush(pq, (0.0, start, None, []))
    visited = {}

    while pq:
        time_so_far, node, cur_line, path = heapq.heappop(pq)
        if (node, cur_line) in visited and visited[(node, cur_line)] <= time_so_far:
            continue
        visited[(node, cur_line)] = time_so_far

        if node == goal:
            return {
                "time": time_so_far,
                "path": path
            }

        for neighbor, tcost, line in graph.get(node, []):
            extra = 0.0
            if cur_line is not None and line != cur_line:
                extra = transfer_penalty
            new_time = time_so_far + tcost + extra
            new_path = path + [(node, neighbor, tcost, line, extra > 0.0)]
            if (neighbor, line) in visited and visited[(neighbor, line)] <= new_time:
                continue
            heapq.heappush(pq, (new_time, neighbor, line, new_path))
    return None
