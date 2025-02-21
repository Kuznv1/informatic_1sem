class Node:
    def __init__(self, value):
        self.left   = None
        self.right  = None
        self.parent = None
        self.value = value

class Splay_tree:
    def __init__(self):
        self.root = None

    def rotate(parent, child):
        gparent = parent.parent
        if gparent != None:
            if gparent.left == parent:
                gparent.left = child
            else:
                gparent.right = child

        if parent.left == child:
            parent.left, child.right = child.right, parent
        else:
            parent.right, child.left = child.left, parent

        keep_parent(child)
        keep_parent(parent)
        child.parent = gparent

