# Stworzyć ADT w postaci kolejki losowej, z której elementy będą pobierane w losowej kolejności.
# Zadbać o to, aby każda operacja była wykonywana w stałym czasie, niezależnie od liczby elementów w kolejce.

from random import random
import unittest


class RandomQueue:

    def __init__(self, size):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.head = 0           # pierwszy do pobrania
        self.tail = 0           # pierwsze wolne

    def insert(self, data):
        if self.is_full():
            raise ValueError(
                'Queue is full, please pop one or more elements to operate on it')
        else:
            self.items[self.tail] = data
            self.tail = (self.tail + 1) % self.n

    def remove(self):   # zwraca losowy element
        if self.is_empty():
            raise ValueError('Queue is empty')
        else:
            random_index = int(random() * self.tail)
            result = self.items[random_index]
            self.items[random_index] = self.items[self.tail-1]
            self.tail = (self.tail - 1) % self.n
            return result

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def clear(self):     # czyszczenie listy
        end = self.head
        while end != self.tail:
            self.items[end] = None
            end = (end + 1) % self.n
        self.tail = self.head


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = RandomQueue(4)

    def test__init__(self):
        self.assertEqual(self.queue.n, 5)

    def test_insert(self):
        self.queue.insert(1)
        self.assertEqual(self.queue.tail, 1)
        self.queue.insert(2)
        self.queue.insert(3)
        self.queue.insert(4)
        try:
            self.queue.insert(5)
        except ValueError:
            print('Queue is full, please pop one or more elements to operate on it')

    def test_remove(self):  # zwraca losowy element
        try:
            self.queue.remove()
        except ValueError:
            print('Queue is empty and not operable')
        self.queue.insert(6)
        self.queue.insert(7)
        self.queue.insert(8)
        self.assertTrue(self.queue.remove() != None)

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.insert(9)
        self.assertFalse(self.queue.is_empty())

    def test_is_full(self):
        self.assertFalse(self.queue.is_full())
        self.queue.insert(10)
        self.queue.insert(11)
        self.queue.insert(12)
        self.queue.insert(13)
        self.assertTrue(self.queue.is_full())

    def test_clear(self):     # czyszczenie listy
        self.queue.insert(14)
        self.queue.insert(15)
        self.assertFalse(self.queue.is_empty())
        self.queue.clear()
        self.assertTrue(self.queue.is_empty())


if __name__ == "__main__":
    unittest.main()
