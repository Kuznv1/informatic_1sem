class Node:                         #Узлы
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, value):
        
        if self.root == None:
            self.root = Node(value)
            return

        t = self.root
        parent = None
        while t != None:
            parent = t
            t = t.left if value < t.value else t.right
        
        new = Node(value)
        new.parent = parent
        if value < parent.value:
            parent.left = new
        else:
            parent.right = new

    def search(self,value):
        t = self.root
        while t != None and t.value != value:
            t = t.left if value < t.value else t.right
        #print('t a ', t.value if t.value == None else None)
        return False if t == None else True
    
    def remove(self, value):
        t = self.root
        parent = None
        while t != None:
            parent = t
            t = t.left if value < t.value else t.right

        if t == None:
            return
        
        if t.left == None and t.right == None:
            if t == parent.left :
                parent.left == None
            else:
                parent.right == None
            return
        
        if t.left == None or t.right == None:
            child = t.left if t.left != None else t.right

            child.parent = parent
            if child.value >= parent.value:
                parent.right = child
            else:
                parent.left = child
            return
        successor = t.right
        while successor.left != None:
            successor = successor.left

        if successor == t.right:
            successor.left == t.left
            successor.parent = t.parent
            successor.left.parent = successor
            successor.parent.left = successor
        else:
            successor.right.parent = successor.parent
            successor.parent.left = successor.right

            successor.parent = t.parent
            successor.left = t.left
            successor.right = t.right

            successor.parent.left = successor
            successor.left.parent = successor
            successor.right.parent = successor

T = Tree()
T.add(7)
T.add(19)
T.add(5)
T.add(6)
T.remove(6)
print(T.search(6))


