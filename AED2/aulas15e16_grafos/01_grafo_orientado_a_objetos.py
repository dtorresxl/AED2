# Aulas 15 e 16 - Grafos: classes Vertice, Adjacente e Grafo (mapa de cidades)

# Classe Vertice ou Nó
class Vertice:
    def __init__(self, rotulo):
        self.rotulo = rotulo
        self.visitado = False
        self.adjacentes = []

    def adiciona_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)

    def mostra_adjacentes(self):
        for i in self.adjacentes:
            print(i.vertice.rotulo, i.custo)

# Classe Adjacente ou Aresta
class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo

# Classe Grafo (definindo suas relações)
class Grafo:
    sorocaba = Vertice('Sorocaba')
    saopaulo = Vertice('São Paulo')
    campinas = Vertice('Campinas')
    botucatu = Vertice('Botucatu')
    limeira = Vertice('Limeira')
    ribeiraopreto = Vertice('Ribeirão Preto')
    jau = Vertice('Jaú')
    saocarlos = Vertice('São Carlos')
    sjriopreto = Vertice('S. J. Rio Preto')
    barretos = Vertice('Barretos')

    sorocaba.adiciona_adjacente(Adjacente(saopaulo, 87))
    sorocaba.adiciona_adjacente(Adjacente(campinas, 85))
    sorocaba.adiciona_adjacente(Adjacente(botucatu, 152))

    # Obs.: no slide o código usa 95 km (São Paulo-Campinas) e o desenho mostra 96 km.
    # Mantido 95 como no código do slide.
    saopaulo.adiciona_adjacente(Adjacente(sorocaba, 87))
    saopaulo.adiciona_adjacente(Adjacente(campinas, 95))

    campinas.adiciona_adjacente(Adjacente(saopaulo, 95))
    campinas.adiciona_adjacente(Adjacente(sorocaba, 85))
    campinas.adiciona_adjacente(Adjacente(limeira, 54))
    campinas.adiciona_adjacente(Adjacente(ribeiraopreto, 238))

    botucatu.adiciona_adjacente(Adjacente(sorocaba, 152))
    botucatu.adiciona_adjacente(Adjacente(jau, 76))

    limeira.adiciona_adjacente(Adjacente(campinas, 54))
    limeira.adiciona_adjacente(Adjacente(saocarlos, 98))

    ribeiraopreto.adiciona_adjacente(Adjacente(campinas, 238))
    ribeiraopreto.adiciona_adjacente(Adjacente(barretos, 127))

    jau.adiciona_adjacente(Adjacente(botucatu, 76))
    jau.adiciona_adjacente(Adjacente(saocarlos, 99))

    saocarlos.adiciona_adjacente(Adjacente(jau, 99))
    saocarlos.adiciona_adjacente(Adjacente(limeira, 98))
    saocarlos.adiciona_adjacente(Adjacente(barretos, 226))
    saocarlos.adiciona_adjacente(Adjacente(sjriopreto, 216))

    sjriopreto.adiciona_adjacente(Adjacente(saocarlos, 216))
    sjriopreto.adiciona_adjacente(Adjacente(barretos, 95))

    barretos.adiciona_adjacente(Adjacente(saocarlos, 226))
    barretos.adiciona_adjacente(Adjacente(ribeiraopreto, 127))
    barretos.adiciona_adjacente(Adjacente(sjriopreto, 95))

if __name__ == "__main__":
    grafo = Grafo()
    print("Adjacentes de São Paulo:")
    grafo.saopaulo.mostra_adjacentes()
    print("\nAdjacentes de Sorocaba:")
    grafo.sorocaba.mostra_adjacentes()
