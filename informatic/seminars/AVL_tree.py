class Node:
    def __init__(self, value):
        self.left   = None
        self.right  = None
        self.height = None
        self.value = value

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if  node is None:
            return 0
        return node.height

    def balance(self, node):
        if node is None:
            return 0
        else:
            return self.height(node.left) - self.height(node.right)
    
    def add(self, root, value):
        if root is None:
            return Node(value)
        elif value < root.value:
            root.left = self.add(root.left, value)
        else:
            root.right = self.add(root.right, value)
        if self.height(root.left) is not None and self.height(root.right) is not None:
            root.height = 1 + max(self.height(root.left), self.height(root.right))
        elif self.height(root.left) is not None:
            root.height = 1 + self.height(root.left)
        elif self.height(root.right) is not None:
            root.height = 1 + self.height(root.right)
        elif self.height(root.left) is None and self.height(root.right) is None:
            root.height = 1
        balance = self.balance(root)

        # левый поворот
        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        # правый поворот
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        # Left-Right поворот с родителем
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left 
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root
    
    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y
    
    def search(self, root, value):
        if not root or root.value == value:
            return root
        if root.value < value:
            return self.search(root.right, value)
        return self.search(root.left, value)

    def add_value(self, value):
        self.root = self.add(self.root, value)

    def search_value(self, value):
        return self.search(self.root, value)
    

a = AVLTree()
a.add_value(3)
a.add_value(8)
a.add_value(2)
a.add_value(7)
print(a.search(7))