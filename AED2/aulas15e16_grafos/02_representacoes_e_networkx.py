# Aulas 15 e 16 - Representações de grafo e NetworkX

# ---- Matriz de adjacência (grafo dos slides: A=0, B=1, C=2, D=3) ----
# Direcionado: B->A, B->D, B->C, D->C
matriz_dirigido = [
    [0, 0, 0, 0],   # A
    [1, 0, 1, 1],   # B
    [0, 0, 0, 0],   # C
    [0, 0, 1, 0],   # D
]
# Não direcionado: A-B, B-D, B-C, D-C
matriz_nao_dirigido = [
    [0, 1, 0, 0],
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
]

# ---- Lista de adjacências (dicionário) ----
lista_nao_dirigido = {
    'A': ['B'],
    'B': ['A', 'D', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'B'],
}

if __name__ == "__main__":
    print("Matriz (dirigido):")
    for linha in matriz_dirigido:
        print(linha)
    print("Lista de adjacências (não dirigido):", lista_nao_dirigido)

    # ---- NetworkX (slide 47) ----
    # pip install networkx
    try:
        import networkx as nx
        G = nx.Graph()
        G.add_edge('A', 'B')
        G.add_weighted_edges_from([('A', 'C', 2)])
        print("\nNetworkX -> nós:", list(G.nodes), "| arestas:", list(G.edges(data=True)))
    except ImportError:
        print("\n(NetworkX não instalado: pip install networkx)")
