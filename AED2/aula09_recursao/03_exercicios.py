# Aula 09 - Exercícios

# Exercício 1 (notebook): soma de uma lista
def soma_lista_recursiva(lista):
    if not lista:                 # caso base
        return 0
    return lista[0] + soma_lista_recursiva(lista[1:])

# Exercício 2 (notebook): potenciação recursiva
def potencia(base, expoente):
    if expoente == 0:             # caso base
        return 1
    return base * potencia(base, expoente - 1)

# Exercício 3 (slides): soma dos dígitos
def soma_digitos(n):
    if n < 10:                    # caso base: um único dígito
        return n
    else:
        ultimo_digito = n % 10
        resto_do_numero = n // 10
        return ultimo_digito + soma_digitos(resto_do_numero)  # passo recursivo

# Exercícios teóricos dos slides:
# 1) ENADE -> alternativa D (todo caso recursivo precisa de caso base e de um problema menor)
# 2) Fibonacci recursivo -> alternativa C, O(2^n)

if __name__ == "__main__":
    print(soma_lista_recursiva([1, 2, 3, 4, 5]))   # 15
    print(soma_lista_recursiva([]))                # 0
    print(potencia(2, 10))                         # 1024
    print(potencia(5, 0))                          # 1
    print(soma_digitos(123))                       # 6
