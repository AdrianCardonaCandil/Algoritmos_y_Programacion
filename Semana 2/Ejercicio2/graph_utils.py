import networkx as nx

def build_graph():
    """ 
    Read data from the standard input and build the corresponding
    nondirected graph without weights. Nodes numbering starts with
    number 1 (that is, nodes are 1,2,3,...)
    """
    
    print("Introduce el número de nodos y el número de aristas del grafo:")
    
    first_line = input().split()
    num_nodes  = int(first_line[0])
    num_edges  = int(first_line[1])

    # Paso 1: Crear el grafo no-dirigido con sus vértices
    
    # Declaro el correspondiente grafo no dirigido
    graph = nx.Graph()
    
    # Añado los vértices
    for i in range(1, num_nodes):
        graph.add_node(i)
    
    # Paso 2: Añadirle las aristas
    
    # Para añadir las aristas tengo que leer antes todos los vertices
    print("Introduce los vertices que forman el grafo deseado: ")
    
    for i in range(num_edges):
        vertice = input().split()
        graph.add_edge(int(vertice[0]), int(vertice[1]))
        
    return graph