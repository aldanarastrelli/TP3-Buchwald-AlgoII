from random import sample
from collections import defaultdict


class Grafo:
    def __init__(self, dirigido=False, lista_vertices=[]):
        self.vertices = defaultdict(dict)
        self.grados = defaultdict(dict) # grado de entrada + salida, si es dirigido
        self.dirigido = dirigido
        for v in lista_vertices:
            self.agregar_vertice(v)

    def agregar_vertice(self, v):
        if v in self.vertices:
            return None
        else:
            self.vertices[v] = {}
            self.grados[v] = 0

    def agregar_arista(self, v1, v2, peso=0):
        if not self.dirigido:
            self.vertices[v2][v1] = peso

        self.grado[v1] += peso
        self.grado[v2] += peso
        if self.dirigido:
            self.vertices[v1][v2] = -peso

    def obtener_vertices(self):
        return list(self.vertices)

    def obtener_adyacentes(self, v):
        if v not in self.vertices:
            return []
        else:
            return list(self.vertices[v])

    def obtener_peso(self, v1, v2):
        if (v1 not in self.vertices) or (v2 not in self.vertices):
            return None
        if (v2 not in self.obtener_adyacentes(v1)):
            return None
        if (not self.dirigido) and (v1 not in self.obtener_adyacentes(v2)):
            return None
        else:
            return self.vertices[v1][v2]
    def obtener_grado(self,v):
        if v not in self.vertices:
            return None
        return grafo.grados[v]

    def vertice_aleatorio(self):
        return sample(self.obtener_vertices(),1)[0]

    def __contains__(self, v):
        return v in self.vertices

    def __str__(self):
        return str(self.vertices)

    def __iter__(self):
        return iter(self.vertices)

    def __len__(self):
        return len(self.vertices)
