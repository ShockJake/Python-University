class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    # *kod z lekcji

    def __init__(self):
        self.length = 0   # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        # return self.length == 0
        return self.head is None

    def count(self):   # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node: Node):
        if self.head:   # dajemy na początek listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node: Node):   # klasy O(1)
        if self.head:   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):          # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node

    def remove_tail(self):   # klasy O(n)
        # Zwraca cały węzeł, skraca listę.
        # Dla pustej listy rzuca wyjątek ValueError.
        if self.is_empty():
            raise ValueError("Pusta lista")
        node = self.head
        if self.head == self.tail:
            to_remove = self.tail
            self.head = self.tail = None
            self.length = 0
            return to_remove
        else:
            while node.next != self.tail:
                node = node.next
            to_remove = self.tail
            node.next = None
            self.tail = node
            self.length -= 1
            return to_remove

    def join(self, other: object):    # klasy O(1)
        # Węzły z listy other są przepinane do listy self na jej koniec.
        # Po zakończeniu operacji lista other ma być pusta.
        if other.is_empty():
            pass
        elif self.is_empty():
            self.head = other.head
            self.tail = other.tail
            self.length = other.length
        else:
            self.tail.next = other.head
            self.tail = other.tail
            self.length += other.length
        other.clear()

    def clear(self):    # czyszczenie listy
        self.length = 0
        while self.head != self.tail:
            node = self.head
            self.head = self.head.next
            del node
        self.head = self.tail = None


def printList(list: SingleList):
    node = list.head
    for i in range(list.length):
        print(node.data)
        node = node.next


def main():
    sL = SingleList()
    sL.insert_head(Node(11))
    sL.insert_tail(Node(12))
    sL.insert_tail(Node(13))
    sL.insert_tail(Node(14))
    sL.insert_tail(Node(15))

    printList(sL)
    sL.remove_tail()
    printList(sL)

    sL2 = SingleList()
    sL2.insert_head(Node(16))
    sL2.insert_tail(Node(17))
    sL2.insert_tail(Node(18))
    sL2.insert_tail(Node(19))
    sL2.insert_tail(Node(20))

    sL.join(sL2)
    printList(sL)


if __name__ == '__main__':
    main()
