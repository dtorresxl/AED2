# Aulas 11 e 12 - Algoritmos de ordenação
import numpy as np

# Bubble sort  O(n**2)
def bubble_sort(vetor):
    n = len(vetor)
    for i in range(n):
        for j in range(0, n - i - 1):
            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
    return vetor

# Selection sort  O(n**2)
def selection_sort(vetor):
    n = len(vetor)
    for i in range(n):
        id_minimo = i
        for j in range(i + 1, n):
            if vetor[id_minimo] > vetor[j]:
                id_minimo = j
        temp = vetor[i]
        vetor[i] = vetor[id_minimo]
        vetor[id_minimo] = temp
    return vetor

# Insertion sort  O(n**2)
def insertion_sort1(vetor):
    n = len(vetor)
    for i in range(1, n):
        marcado = vetor[i]
        j = i - 1
        while j >= 0 and marcado < vetor[j]:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = marcado
    return vetor

def insertion_sort2(vetor):
    # Percorre cada elemento
    for i in range(1, len(vetor)):
        k = i
        # Insere o pivô na posição correta
        while k > 0 and vetor[k] < vetor[k - 1]:
            vetor[k], vetor[k - 1] = vetor[k - 1], vetor[k]
            k = k - 1
    return vetor   # (acrescentado para facilitar os testes)

# Shell sort  O(n**2) - O(n log n)
def shell_sort1(vetor):
    n = len(vetor)
    h = 1
    while h > 0:
        for i in range(h, n):
            c = vetor[i]
            j = i
            while j >= h and c < vetor[j - h]:
                vetor[j] = vetor[j - h]
                j = j - h
                vetor[j] = c
        h = int(h / 2.2)
    return vetor

def shell_sort2(vetor):
    intervalo = len(vetor) // 2
    while intervalo > 0:
        for i in range(intervalo, len(vetor)):
            temp = vetor[i]
            j = i
            while j >= intervalo and vetor[j - intervalo] > temp:
                vetor[j] = vetor[j - intervalo]
                j -= intervalo
            vetor[j] = temp
        intervalo //= 2
    return vetor

# Quick sort  O(n log n), pior caso O(n**2)
# CORRIGIDO: no notebook original a troca do pivô estava dentro do for
# e o valor padrão final=len(vetor)-1 não funciona (vetor não existe na definição).
def particao(vetor, inicio, final):
    pivo = vetor[final]
    i = inicio - 1
    for j in range(inicio, final):
        if vetor[j] <= pivo:
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]
    vetor[i + 1], vetor[final] = vetor[final], vetor[i + 1]
    return i + 1

def quick_sort(vetor, inicio=0, final=None):
    if final is None:
        final = len(vetor) - 1
    if inicio < final:
        posicao = particao(vetor, inicio, final)
        quick_sort(vetor, inicio, posicao - 1)   # esquerda
        quick_sort(vetor, posicao + 1, final)    # direita
    return vetor

# Merge sort  O(n log n)
def merge_sort(vetor):
    if len(vetor) > 1:
        divisao = len(vetor) // 2
        esquerda = vetor[:divisao].copy()
        direita = vetor[divisao:].copy()

        merge_sort(esquerda)
        merge_sort(direita)

        i, j, k = 0, 0, 0
        # Ordena esquerda e direita
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                vetor[k] = esquerda[i]
                i += 1
            else:
                vetor[k] = direita[j]
                j += 1
            k += 1
        # Ordenação final
        while i < len(esquerda):
            vetor[k] = esquerda[i]
            i += 1
            k += 1
        while j < len(direita):
            vetor[k] = direita[j]
            j += 1
            k += 1
    return vetor

if __name__ == "__main__":
    import timeit
    n = 2000   # nas aulas: 5000 (reduzido aqui para rodar rápido)
    vet = list(np.random.randint(0, 1000, n))
    esperado = sorted(vet)

    algoritmos = [bubble_sort, selection_sort, insertion_sort1, insertion_sort2,
                  shell_sort1, shell_sort2, quick_sort, merge_sort]
    print(f"{'algoritmo':<16}{'correto':<9}tempo (s)")
    for alg in algoritmos:
        resultado = alg(vet.copy())
        ok = list(resultado) == esperado
        t = timeit.timeit(lambda: alg(vet.copy()), number=3) / 3
        print(f"{alg.__name__:<16}{str(ok):<9}{t:.4f}")
