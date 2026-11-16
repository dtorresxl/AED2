# Aulas 15 e 16 - Labirinto como grafo + BFS e DFS
# ATENÇÃO: os slides mostram só o dicionário parcial (linhas 0 e 1) e o resultado
# [(0,2),(0,3),(1,3),(2,3),(2,4),(3,4),(4,4),(4,3),(4,2)]. Os algoritmos BFS/DFS abaixo
# são a implementação padrão (complemento meu, não está nos slides), e as arestas
# foram lidas do desenho dos slides 14-16.
from collections import deque

graph = {
    # Linha 0 (topo)
    (0, 0): [(1, 0)],
    (0, 1): [(0, 2), (1, 1)],
    (0, 2): [(0, 1), (0, 3)],
    (0, 3): [(0, 2), (0, 4), (1, 3)],
    (0, 4): [(0, 3), (1, 4)],
    # Linha 1
    (1, 0): [(0, 0), (1, 1)],
    (1, 1): [(0, 1), (1, 0), (2, 1)],
    (1, 2): [(2, 2), (1, 1)],
    (1, 3): [(0, 3), (2, 3)],
    (1, 4): [(0, 4)],
    # Linhas 2 a 4 (lidas do desenho)
    (2, 0): [(2, 1), (3, 0)],
    (2, 1): [(2, 0), (1, 1), (3, 1)],
    (2, 2): [(1, 2), (3, 2)],
    (2, 3): [(1, 3), (2, 4)],
    (2, 4): [(2, 3), (3, 4)],
    (3, 0): [(2, 0), (4, 0)],
    (3, 1): [(2, 1), (3, 2)],
    (3, 2): [(3, 1), (2, 2), (3, 3)],
    (3, 3): [(3, 2)],
    (3, 4): [(2, 4), (4, 4)],
    (4, 0): [(3, 0), (4, 1)],
    (4, 1): [(4, 0)],
    (4, 2): [(4, 3)],
    (4, 3): [(4, 2), (4, 4)],
    (4, 4): [(4, 3), (3, 4)],
}

def bfs(grafo, inicio, fim):
    """Busca em Largura (fila). Garante o caminho com menos arestas."""
    fila = deque([[inicio]])
    visitados = {inicio}
    while fila:
        caminho = fila.popleft()
        no = caminho[-1]
        if no == fim:
            return caminho
        for viz in grafo[no]:
            if viz not in visitados:
                visitados.add(viz)
                fila.append(caminho + [viz])
    return None

def dfs(grafo, inicio, fim):
    """Busca em Profundidade (pilha)."""
    pilha = [[inicio]]
    visitados = set()
    while pilha:
        caminho = pilha.pop()
        no = caminho[-1]
        if no == fim:
            return caminho
        if no in visitados:
            continue
        visitados.add(no)
        for viz in reversed(grafo[no]):
            if viz not in visitados:
                pilha.append(caminho + [viz])
    return None

if __name__ == "__main__":
    print("BFS:", bfs(graph, (0, 2), (4, 2)))
    print("DFS:", dfs(graph, (0, 2), (4, 2)))
