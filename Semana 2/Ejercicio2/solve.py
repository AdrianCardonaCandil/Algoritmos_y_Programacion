import networkx   as nx
from sys          import maxsize as infinite
from simple_queue import *

def bfs_path_length(graph, first_node):
    """
    Compute the shortest path length of the non-directed graph G
    starting from node first_node. Return a dictionary with the
    distance (in number of steps) from first_node to all the nodes.
    """

    distance = {}                 # Diccionario con la distancia desde 
                                  # firstNode al resto de los nodos.
    # Para cada nodo, distancia al nodo inicial igual a infinito.
    for node in graph.nodes():
        distance[node] = infinite
    
    # Distancia al nodo inicial = 0
    distance[first_node] = 0

    # Elaboración del algoritmo de recorrido de grafos por niveles (BFS)
    
    # Iniciamos una cola para poder realizar el algoritmo
    cola = Queue()
    
    # Iniciamos un array de nodos visitados
    nodos_visitado = [0]*graph.number_of_nodes()
    
    # Añado el nodo inicial a la cola y lo marco como visitado
    cola.enqueue(first_node)
    nodos_visitado[first_node - 1] = 1
    
    # Mientras que haya elementos en la cola pendientes de procesar
    while not cola.isEmpty():
        # Saco un elemento de la cola
        actual = cola.dequeue()
        # Para todos sus vecinos, si no estan marcados como visitados
        for vecino in list(graph.neighbors(actual)):
            if nodos_visitado[vecino - 1] == 0:
                # Lo marco como visitado y lo añado a la cola
                nodos_visitado[vecino - 1] = 1
                cola.enqueue(vecino)
                # Y por último, actualizo la distancia
                distance[vecino] = distance[actual] + 1
                
    return distance