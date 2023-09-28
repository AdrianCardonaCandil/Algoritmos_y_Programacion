import networkx as nx

def dfs_topological_sort(graph):
    """
    Compute one topological sort of the given graph.
    """
    
    # La solucion que retorna esta función es un diccionario de Python.
    #   * La clave del diccionario es el número del nodo
    #   * El valor es el orden topologico asignado a ese nodo
    # 
    # Por ejemplo, si tenemos el siguiente grafo dirigido con 3 vertices:
    #                    3 ---> 2 ---> 1
    # ... el orden topologico es:
    #                El vértice 3 va en la primera posición
    #                El vértice 2 en la segunda posición
    #                El vértice 1 en la tercera posición
    # Con lo que debemos devolver un diccionario con este contenido:
    #     {1: 3, 2: 2, 3: 1}

    # Número de nodos en el grafo
    N = graph.number_of_nodes()
    
    visibleNodes = set()  # En este ejercicio utilizamos un set
                          # para recordar los nodos visibles
    
    # Declaro el diccionario de orden para el resultado topológico final
    order = {}

    # solve it here! ------------------------------------------------

    def dfs(u):
        nonlocal N
    
        # Marcar el nodo actual como visible
        visibleNodes.add(u)
        
        # Para cada uno de los vecinos del nodo actual
        for vecino in list(graph.neighbors(u)):
            # Si este no es visible
            if vecino not in visibleNodes:
                # Lanzo el recorrido a partir de dicho nodo.
                dfs(vecino)
        
        # A la vuelta de las llamadas recursivas, podemos afirmar que los nodos no tendran vecinos o ya habrán
        # sido visitados. En tal caso, procesamos los nodos.
        order[u] = N
        N = N - 1
        
        return

    # Lanzamos el recorrido para cada uno de los elementos no conectados del grafo.
    for nodo in graph.nodes():
        if nodo not in visibleNodes:
            dfs(nodo)

    return order