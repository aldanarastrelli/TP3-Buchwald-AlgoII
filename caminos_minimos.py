from queue import Queue
from heapq import heappush
from heapq import heappop
from grafo import Grafo


def bfs(grafo, origen, destino=None):
    visitados = set()
    padre = {}
    orden = {}
    q = Queue()

    visitados.add(origen)
    padre[origen] = None
    orden[origen] = 0

    q.put(origen)

    while not q.empty():
        if destino and destino in visitados:
            break
        v = q.get()
        for w in grafo.obtener_adyacentes(v):
            if w not in visitados:
                visitados.add(w)
                q.put(w)
                padre[w] = v
                orden[w] = orden[v] + 1
    return padre, orden


def recorrido_dfs(grafo):
    visitados = set()
    padre = {}
    orden = {}

    for v in grafo.obtener_vertices():
        if v not in visitados:
            orden[v] = 0
            padre[v] = None
            dfs(grafo, v, visitados, padre, orden)

    return padre, orden


def dfs(grafo, v, visitados, padre, orden):
    visitados.add(v)
    for w in grafo.obtener_adyacentes(v):
        if w not in visitados:
            padre[w] = v
            orden[w] = orden[v] + 1
            dfs(grafo, w, visitados, orden, padre)


def dijkstra(grafo, origen, destino=None, funcion=None):    # .Camino mínimo
    distancia = {}
    padre = {}
    for v in grafo.obtener_vertices():
        distancia[v] = float('inf')

    distancia[origen] = 0
    padre[origen] = None
    q = []
    heappush(q, (distancia[origen], origen))

    while len(q) > 0:
        v = heappop(q)[1]
        if destino and v == destino:
            break
        for w in grafo.obtener_adyacentes(v):
            peso = grafo.obtener_peso(v, w)
            if funcion:
                peso = funcion(peso)
            if distancia[v] + peso < distancia[w]:
                distancia[w] = distancia[v] + peso
                padre[w] = v
                heappush(q, (distancia[w], w))

    return padre, distancia
