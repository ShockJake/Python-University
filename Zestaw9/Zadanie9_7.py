# Dla drzewa BST napisać funkcje znajdujące największy i najmniejszy element przechowywany w drzewie. 
# Mamy łącze do korzenia, nie ma klasy BinarySearchTree. Drzewo BST nie jest modyfikowane, 
# a zwracana jest znaleziona wartość (węzeł).
# W przypadku pustego drzewa należy wyzwolić wyjątek ValueError lub zwrócić None.

def bst_max(top):
    if top == None:
        raise ValueError
    while top.right != None:
        top = top.right
    return top.data

def bst_min(top):
    if top == None:
        raise ValueError
    while top.left != None:
        top = top.left
    return top.data
