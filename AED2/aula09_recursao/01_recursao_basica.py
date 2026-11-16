# Aula 09 - Recursão
# ---- Mostrar mensagens ----
for _ in range(5):
    print('Recursão')

def recursao(i):
    print('Recursão')
    i += 1
    if i == 5:
        return
    else:
        recursao(i)

print('\nrecursao(0):')
recursao(0)
print('\nrecursao(4):')
recursao(4)

# ---- Somar valores ----
def soma1(n):
    soma = 0
    for i in range(n + 1):
        soma += i
    return soma

def soma2(n):
    if n == 0:
        return 0
    return n + soma2(n - 1)

print('\nsoma1(5) =', soma1(5))
print('soma2(5) =', soma2(5))

# ---- Fatorial ----
def fatorial(n):
    if n > 1:
        return n * fatorial(n - 1)
    else:
        return 1

# versão em uma linha (slide 19)
def fatorial_1linha(n):
    return (n * fatorial_1linha(n - 1)) if n > 1 else 1

print('fatorial(5) =', fatorial(5))
print('fatorial_1linha(5) =', fatorial_1linha(5))
