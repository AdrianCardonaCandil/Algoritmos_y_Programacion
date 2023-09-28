import networkx as nx
from simple_stack import *

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
                          
    # Declaración del diccionario que almacenara el orden topológico
    order = {}
    
    # Declaro una pila para poder realizar el recorrido
    pila = Stack()
    
    def dfs_iterative(u):
        nonlocal N
        
        # Añado al set de nodos visibles y a la pila el nodo inicial
        visibleNodes.add(u)
        pila.push(u)
        
        # Mientras queden elementos en la pila para procesar
        while pila.isEmpty() == False:
            
            # Cual es el nodo actual
            actual = pila.peek()
            
            """
            La idea a continuación es ir descendiendo en el recorrido del grafo e ir comprobando que nodos
            tienen hijos que no han sido procesador para poder procesar dichos hijos antes de que se procesen
            los hijos progenitores. En el momento en el que un nodo no tenga nodos sin visitar o directamente,
            sea un nodo que no tiene hijos, se procesan. Esto da lugar al recorrido topológico.
            En verdad, es un recorrido en postorden de un árbol porque se procesan antes los nodos hijos que
            los padres.
            """
            
            # Si dicho nodo no tiene hijos o todos sus hijos ya han sido visitados
            vecinos = list(graph.neighbors(actual))
            if all(elemento in list(visibleNodes) for elemento in vecinos) or len(vecinos) == 0:
                # Me voy de la pila
                pila.pop()
                # Actualizo mi orden en el diccionario
                order[actual] = N
                N = N - 1
            # En este caso el nodo tiene hijos no visitados
            else:
                for vecino in vecinos:
                    if vecino not in visibleNodes:
                        # Para ellos, los añado a los nodos visitados y los añado a la pila para que sean procesados
                        visibleNodes.add(vecino)
                        pila.push(vecino)
        return
    
    # Como ya se ha definido el numero de nodos para el orden, simplemente vamos a llamar a la función para realizar el recorrido
    for nodo in graph.nodes():
        
        # Para cada nodo en el grafo, si no es visible, llamo a la funcion recorrido.
        if nodo not in visibleNodes:
            dfs_iterative(nodo)
    
    return order