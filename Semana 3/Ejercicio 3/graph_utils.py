import networkx as nx

def build_digraph_with_weights():
    """ 
    Read data from the standard input and build the corresponding
    directed graph with weights. Nodes numbering starts with number
    1 (that is, nodes are 1,2,3,...)
    """

    print("Introduce el número de nodos y el número de aristas del grafo:")

    first_line = input().split()
    num_nodes  = int(first_line[0])
    num_edges  = int(first_line[1])

    # Paso 1: Crear grafo direcional con num_nodes

    graph = nx.DiGraph()
    
    # Añado los vértices añ digrafo dirigido

    for vertice in range(1, num_nodes + 1):
        graph.add_node(vertice)

    # Paso 2: Añadir los vértices del grafo
    
    print("Introduce los vertices que forman el grafo deseado: ")

    for i in range(num_edges):
        arista = input().split()
        graph.add_edge(int(arista[0]), int(arista[1]), weight = int(arista[2])) # 0 = Inicio, 1 = Final, 2 = Peso

    return graph