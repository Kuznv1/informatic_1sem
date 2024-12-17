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
    
    def search_leaves(self, node):
        
        if node.left == None and node.right == None:
            return [node.value]
        
        leaves = []

        if node.right != None:
            leaves.extend((self.search_leaves(node.right)))
        
        if  node.left != None:
            leaves.extend((self.search_leaves(node.left)))
        
        return leaves
    
    # Возвращает true, если данный узел дерева является листом; ложь в противном случае
    '''def isLeaf(root):
        return root is not None and root.left is None and root.right is None
'''
    def all_leaves(self):        
        return self.search_leaves(self.root)

a = Tree()
'''a.add(4)
a.add(8)
a.add(9)
a.add(7)'''
n = int(input())
for element in list(map(int, input().split())):
    if a.search(element) == False:
        a.add(element)

leaves = a.all_leaves()
leaves = sorted(leaves)
print(*leaves)



#возратить значения