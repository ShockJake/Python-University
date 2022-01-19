# Tests for AVLTree class:

# tests are done with Python 3.9.10 version

import unittest
from avlTree import *

class TestTree(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = AVLTree()
        self.tree.insert(9)
        self.tree.insert(8)
        self.tree.insert(10)
        self.tree.insert(11)
        self.tree.insert(13)
    
    def test_in_order(self):
        self.assertEqual(self.tree.printInOrder(), '8 9 10 11 13 ')
        
    def test_pre_order(self):
        self.assertEqual(self.tree.printPreOrder(), '9 8 11 10 13 ')
        
    def test_post_order(self):
        self.assertEqual(self.tree.printPostOrder(), '8 10 13 11 9 ')
    
    def test_insert(self):
        self.tree.insert(15)
        self.assertEqual(self.tree.printInOrder(), '8 9 10 11 13 15 ')
    
    def test_remove(self):
        self.tree.remove(8)
        self.assertEqual(self.tree.printInOrder(), '9 10 11 13 ')
    
    def test_findMin(self):
        self.assertEqual(self.tree.findMinNodeValue(), 8)
    
    def test_findMax(self):
        self.assertEqual(self.tree.findMaxNodeValue(), 13)
    
    def test_contains(self):
        self.assertTrue(self.tree.contains(10))
        self.assertFalse(self.tree.contains(12))
    
if __name__ == '__main__':
    unittest.main()