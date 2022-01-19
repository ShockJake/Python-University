# Implemetetation of AVL Tree using Python

AVLTree is a is a self-balancing binary search tree (BST).

## Time and memory complexity

![Time and memory complexity](./png/TimeAndMemoryComplexity.png 'Time and memory complexity')

## Advantages of AVL Trees

- Better search times. That is O(log n)
- The height of the Tree is always balanced and does not grow beyond log n, n being the total number of nodes in the Tree
- Gives better time complexities in comparison to BSTs
- They have self-balancing capabilities

## Disadvantages of AVL Trees

- Longer running times for insert and remove operations
- Very difficult to implement
- Have high constant factors

## Applications of AVL Trees

- Used as sets and dictionaries at times
- Often used in databases where frequent lookups are required
- Used for indexing purposes too

## Class AVLTree

Class AVLTree is a class that represents a AVL tree and has such methods:

```python
myTree = AVLTree()

myTree.insert(10)
myTree.remove(10)
myTree.contatins(10)
myTree.printInOrder()
myTree.printPreOrder()
myTree.printPostOrder()
myTree.findMinNodeValue()
myTree.findMaxNodeValue()
myTree.clear()
```

- ### Constructor

```python
# --- Basic constructor ---
AVLTree()
```

> Basic constructor with no arguments, creates empty AVL tree.

- ### Operations

![AVLTree example](./png/AVL_Tree_Example.gif 'AVLTree example')

- ### Public methods

```python
myTree.insert(10)
```

Inserts new element to the tree by following algorythm:

1. A newNode is always inserted as a leaf node with balance factor equal to 0.
2. Go to the appropriate leaf node to insert a newNode using the following recursive steps. Compare newKey with rootKey of the current tree.

If newKey < rootKey, call insertion algorithm on the left subtree of the current node until the leaf node is reached.

Else if newKey > rootKey, call insertion algorithm on the right subtree of current node until the leaf node is reached.

Else, return leafNode.

3. Compare leafKey obtained from the above steps with newKey:

If newKey < leafKey, make newNode as the leftChild of leafNode.

Else, make newNode as rightChild of leafNode.

4. Update balanceFactor of the nodes.

5. If the nodes are unbalanced, then rebalance the node.

If balanceFactor > 1, it means the height of the left subtree is greater than that of the right subtree. So, do a right rotation or left-right rotation

If newNodeKey < leftChildKey do right rotation.
Else, do left-right rotation.

If balanceFactor < -1, it means the height of the right subtree is greater than that of the left subtree. So, do right rotation or right-left rotation

If newNodeKey > rightChildKey do left rotation.
Else, do right-left rotation

---

```Python
myTree.remove(10)
```

Removes element from the tree using folowing algorythm:

1. Locate nodeToBeDeleted.

2. There are three cases for deleting a node:

If nodeToBeDeleted is the leaf node (ie. does not have any child), then remove nodeToBeDeleted.

If nodeToBeDeleted has one child, then substitute the contents of nodeToBeDeleted with that of the child. Remove the child.

If nodeToBeDeleted has two children, find the inorder successor w of nodeToBeDeleted (ie. node with a minimum value of key in the right subtree).

a) Substitute the contents of nodeToBeDeleted with that of w.

b) Remove the leaf node w.

3. Update balanceFactor of the nodes.

4. Rebalance the tree if the balance factor of any of the nodes is not equal to -1, 0 or 1.

a) If balanceFactor of currentNode > 1,

If balanceFactor of leftChild >= 0, do right rotation.

Else do left-right rotation.

b) If balanceFactor of currentNode < -1,

If balanceFactor of rightChild <= 0, do left rotation.

Else do right-left rotation.

---

```Python
myTree.contatins(10)
```

Checks if the Tree contain geiven element.

---

```Python
myTree.printInOrder()
```

![Inorder-traversal](./png/Inorder-traversal.gif 'Inorder-traversal')

Returns string that contains all elements of the tree in the In order.

---

```Python
myTree.printPreOrder()
```

![Preorder-traversal](./png/Preorder-traversal.gif 'Preorder-traversal')

Returns string that contains all elements of the tree in the Pre order.

---

```Python
myTree.printPostOrder()
```

![Postorder-traversal](./png/Postorder-traversal.gif 'Postorder-traversal')

Returns string that contains all elements of the tree in the Post order.

---

```Python
myTree.findMinNodeValue()
```

Finds node with the smallest value.

---

```Python
myTree.findMaxNodeValue()
```

Finds node with the biggest value.

---

```Python
myTree.clear()
```

Deletes all nodes of the tree.

---
