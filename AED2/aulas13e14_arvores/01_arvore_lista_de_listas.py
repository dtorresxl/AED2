# Aulas 13 e 14 - Árvores binárias: LISTA DE LISTAS

# Cria árvore binária com raiz r
def binary_tree(r):
    return [r, [], []]

# Insere novo ramo à esquerda da raiz
def insert_left(root, new_branch):
    # Analisa a subárvore à esquerda
    t = root.pop(1)
    # Se a subárvore à esquerda não é vazia, o novo ramo vira raiz dela
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root

# Insere novo ramo à direita da raiz
def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root

def get_root_val(root):
    return root[0]

def set_root_val(root, new_val):
    root[0] = new_val

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]

if __name__ == "__main__":
    print("--- Testando a implementação ---")
    r = binary_tree(3)
    insert_left(r, 4)
    insert_left(r, 5)
    insert_right(r, 6)
    insert_right(r, 7)
    print(r)
    l = get_left_child(r)
    print(l)
    set_root_val(l, 9)
    print(r)
    insert_left(l, 11)
    print(r)

    print("\n--- Exercício dos slides ---")
    x = binary_tree('a')
    insert_left(x, 'b')
    insert_right(x, 'c')
    insert_right(get_right_child(x), 'd')
    insert_left(get_right_child(get_right_child(x)), 'e')
    print(x)
    # ['a', ['b', [], []], ['c', [], ['d', ['e', [], []], []]]]
