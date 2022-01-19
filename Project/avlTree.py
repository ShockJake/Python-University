
class AVLTree:

    class Node:
        def __init__(self, value):
            self.value = value
            self.left: AVLTree.Node = None
            self.right: AVLTree.Node = None
            self.height = 1

    class EmptyTreeException(Exception):
        def __init__(self, message='Tree is empty and not operable') -> None:
            self.message = message
            super().__init__(message)

    # Basic constructor
    def __init__(self):
        self.root: AVLTree.Node = None

    #   --- Private helping methods ---

    def __getHeight(self, node: Node) -> int:
        if node == None:
            return 0
        return node.height

    def __getBalance(self, node: Node) -> int:
        if node == None:
            return 0
        return self.__getHeight(node.left) - self.__getHeight(node.right)

    def __rightRotateNode(self, node: Node) -> Node:
        t1: AVLTree.Node = node.left
        t2 = t1.right

        t1.right = node
        node.left = t2

        node.height = max(self.__getHeight(node.left),
                          self.__getHeight(node.right)) + 1
        t1.height = max(self.__getHeight(t1.left),
                        self.__getHeight(t1.right)) + 1

        return t1

    def __leftRotateNode(self, node: Node) -> Node:
        t1: AVLTree.Node = node.right
        t2 = t1.left

        t1.left = node
        node.right = t2

        node.height = max(self.__getHeight(node.left),
                          self.__getHeight(node.right)) + 1
        t1.height = max(self.__getHeight(t1.left),
                        self.__getHeight(t1.right)) + 1

        return t1

    # Next methods have their public analogs, it was done for better understanding and avoiding writing 'self.root' everywhere

    def __findMinNode(self, node: Node) -> Node:
        result = node
        while result.left != None:
            result = result.left
        return result

    def __findMaxNode(self, node: Node) -> Node:
        result = node
        while result.right != None:
            result = result.right
        return result

    def __insert(self, node: Node, value) -> Node:
        if node == None:
            return AVLTree.Node(value)

        if value < node.value:
            node.left = self.__insert(node.left, value)
        elif value > node.value:
            node.right = self.__insert(node.right, value)
        else:
            return node

        node.height = 1 + max(self.__getHeight(node.left),
                              self.__getHeight(node.right))

        balance = self.__getBalance(node)

        if balance > 1:
            if value < node.left.value:
                return self.__rightRotateNode(node)
            else:
                node.left = self.__leftRotateNode(node.left)
                return self.__rightRotateNode(node)
        if balance < -1:
            if value > node.right.value:
                return self.__leftRotateNode(node)
            else:
                node.right = self.__rightRotateNode(node.right)
                return self.__leftRotateNode(node)

        return node

    def __remove(self, node: Node, value) -> Node:
        if node == None:
            return node

        if value < node.value:
            node.left = self.__remove(node.left, value)
        elif value > node.value:
            node.right = self.__remove(node.right, value)
        else:
            if node.left == None or node.right == None:
                if node.left != None:
                    newNode: AVLTree.Node = node.left
                else:
                    newNode: AVLTree.Node = node.right

                if newNode == None:
                    newNode = node
                    node = None
                else:
                    node = newNode
            else:
                newNode: AVLTree.Node = self.__findMinNode(node.right)
                node.value = newNode.value
                node.right = self.__remove(node.right, newNode.value)

        if node == None:
            return node

        node.height = 1 + max(self.__getHeight(node.left),
                              self.__getHeight(node.right))

        balance = self.__getBalance(node)

        if balance > 1:
            if value < node.left.value:
                return self.__rightRotateNode(node)
            else:
                node.left = self.__leftRotateNode(node.left)
                return self.__rightRotateNode(node)
        if balance < -1:
            if value > node.right.value:
                return self.__leftRotateNode(node)
            else:
                node.right = self.__rightRotateNode(node.right)
                return self.__leftRotateNode(node)

        return node

    def __contains(self, node: Node, value) -> bool:
        while node != None:
            if node.value == value:
                return True
            if value < node.value:
                node = node.left
            else:
                node = node.right

        return False

    def __clearNodes(self, node: Node):
        if node != None:
            node.left = self.__clearNodes(node.left)
            node.right = self.__clearNodes(node.right)

        return None

    def __printInOrder(self, node: Node):
        result = ''
        if node == None:
            return result
        result += self.__printInOrder(node.left)
        result += str(node.value) + ' '
        result += self.__printInOrder(node.right)
        return result

    def __printPreOrder(self, node: Node):
        result = ''
        if node == None:
            return result
        result += str(node.value) + ' '
        result += self.__printPreOrder(node.left)
        result += self.__printPreOrder(node.right)
        return result

    def __printPostOrder(self, node: Node):
        result = ''
        if node == None:
            return result
        result += self.__printPostOrder(node.left)
        result += self.__printPostOrder(node.right)
        result += str(node.value) + ' '
        return result

    # --- Public methods ---

    def isEmpty(self) -> bool:
        return self.root == None

    def findMinNodeValue(self):
        if self.isEmpty():
            raise self.EmptyTreeException()
        return self.__findMinNode(self.root).value

    def findMaxNodeValue(self):
        if self.isEmpty():
            raise self.EmptyTreeException()
        return self.__findMaxNode(self.root).value

    # Inserts new element to the tree.
    def insert(self, value):
        if self.isEmpty():
            self.root = self.Node(value)
        self.root = self.__insert(self.root, value)

    # Removes element from the tree.
    def remove(self, data):
        if self.isEmpty():
            raise
        self.root = self.__remove(self.root, data)

    # Checks if three contains element with given value.
    def contains(self, value) -> bool:
        if self.isEmpty():
            raise self.EmptyTreeException()
        return self.__contains(self.root, value)

    # Deletes all nodes of tree
    def clear(self):
        if self.isEmpty():
            raise self.EmptyTreeException()
        self.root = self.__clearNodes(self.root)

    def printInOrder(self):
        if self.isEmpty():
            raise self.EmptyTreeException()
        return self.__printInOrder(self.root)

    def printPreOrder(self):
        if self.isEmpty():
            raise self.EmptyTreeException()
        return self.__printPreOrder(self.root)

    def printPostOrder(self):
        if self.isEmpty():
            raise self.EmptyTreeException()
        return self.__printPostOrder(self.root)
