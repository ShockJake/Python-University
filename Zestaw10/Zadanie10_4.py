# Poprawić metodę get(), aby w przypadku pustej kolejki zwracała wyjątek.
# Poprawić metodę put() w tablicowej implementacji kolejki, aby w przypadku przepełnienia kolejki zwracała wyjątek.
# Napisać kod testujący kolejkę.

import unittest


class Queue:

    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.head = 0           # pierwszy do pobrania
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.tail + 1) % self.n == self.head

    def put(self, data):
        if self.is_full():
            raise OverflowError(
                'Queue is full, please pop one or more elements to operate on it')
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if self.is_empty():
            raise ValueError('Queue is empty and not operable')
        data = self.items[self.head]
        self.items[self.head] = None   # usuwam referencję
        self.head = (self.head + 1) % self.n
        return data

    def toString(self):
        result = ''
        if self.is_empty():
            raise ValueError('Queue is empty and not operable')
        if self.n > 1:
            for i in range(len(self.items) - 1):
                result += str(self.items[i]) + ' '
        return result


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.q = Queue(4)
        self.q.put(5)
        self.q.put(4)
        self.q.put(3)
        self.q.put(2)

    def test_is_empty(self):
        self.assertEqual(self.q.is_empty(), False)

    def test_put(self):
        self.assertEqual(self.q.toString(), '5 4 3 2 ')

    def test_is_full(self):
        self.assertEqual(self.q.is_full(), True)

    def test_get(self):
        self.assertEqual(self.q.get(), 5)


if __name__ == '__main__':
    unittest.main()
