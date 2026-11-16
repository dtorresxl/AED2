# Aulas 13 e 14 - Árvores binárias: LISTAS LIGADAS (referências)

class BinaryTree:
    # Construtor
    def __init__(self, valor):
        self.key = valor
        self.left_child = None
        self.right_child = None

    # Insere nó à esquerda
    def insert_left(self, valor):
        # Se não tem filho à esquerda, OK
        if self.left_child == None:
            self.left_child = BinaryTree(valor)
        else:
            # Se tem, pendura a subárvore à esquerda do novo nó
            temp = BinaryTree(valor)
            temp.left_child = self.left_child
            self.left_child = temp

    # Insere nó à direita
    def insert_right(self, valor):
        if self.right_child == None:
            self.right_child = BinaryTree(valor)
        else:
            temp = BinaryTree(valor)
            temp.right_child = self.right_child
            self.right_child = temp

    # Obtém filho à direita / à esquerda
    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    # Atualiza / obtém valor do nó corrente
    def set_root_val(self, valor):
        self.key = valor

    def get_root_val(self):
        return self.key

    # ---- Percursos ----
    # CORRIGIDO: nos slides aparece self.left / self.right,
    # mas os atributos se chamam left_child / right_child.
    def preorder(self):
        print(self.key)                      # raiz
        if self.left_child:
            self.left_child.preorder()       # esquerda
        if self.right_child:
            self.right_child.preorder()      # direita

    def inorder(self):
        if self.left_child:
            self.left_child.inorder()        # esquerda
        print(self.key)                      # raiz
        if self.right_child:
            self.right_child.inorder()       # direita

    def postorder(self):
        if self.left_child:
            self.left_child.postorder()      # esquerda
        if self.right_child:
            self.right_child.postorder()     # direita
        print(self.key)                      # raiz

if __name__ == "__main__":
    r = BinaryTree('a')
    print(r.get_root_val())
    print(r.get_left_child())
    print(r.get_right_child())
    r.insert_left('b')
    print(r.get_left_child().get_root_val())
    r.insert_right('c')
    print(r.get_right_child().get_root_val())
    r.get_left_child().insert_left('d')
    print(r.get_left_child().get_left_child().get_root_val())
    r.get_left_child().insert_right('e')
    print(r.get_left_child().get_right_child().get_root_val())

    print("\npreorder:");  r.preorder()
    print("\ninorder:");   r.inorder()
    print("\npostorder:"); r.postorder()
