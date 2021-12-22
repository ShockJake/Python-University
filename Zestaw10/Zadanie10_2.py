# Poprawić implementację tablicową stosu tak, aby korzystała z wyjątków w przypadku pojawienia się błędu. 
# Metoda pop() ma zgłaszać błąd w przypadku pustego stosu. Metoda push() ma zgłaszać błąd w przypadku przepełnienia stosu. 
# Napisać kod testujący stos.

import unittest

class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementów na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full():
            raise OverflowError('Stack is full')
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None    # usuwam referencję
        return data

class TestStack(unittest.TestCase):

    def setUp(self) -> None:
        self.stack = Stack(3)

    def test_init(self):
        self.assertEqual(self.stack.n, 0)
        self.assertEqual(self.stack.size, 3)

    def test_is_empty(self):
        self.assertEqual(self.stack.is_empty(), True)

    def test_push(self):
        self.stack.push(3)
        self.assertEqual(self.stack.items[0], 3)

    def test_is_full(self):
        self.assertFalse(self.stack.is_full())
        self.stack.push(1)
        self.stack.push(1)
        self.stack.push(1)
        self.assertTrue(self.stack.is_full())

    def test_pop(self):
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)

if __name__ == "__main__":
    unittest.main()
