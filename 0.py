class Node:
    def __init__(self, data, positive_child=None, negative_child=None):
        self.data = data
        self.positive_child = positive_child
        self.negative_child = negative_child

    def __str__(self) -> str:
        return self.data

class Decision:
    def __init__(self, root: Node):
        self.root = root

    def collect_leaves(self, node):
        ## ---------------------------
        ## This node has no children. It is a leaf
        ## ---------------------------
        if not node.positive_child and not node.negative_child:
            return [node]
        ## ---------------------------

        ## ---------------------------
        ## Recursively collect the leaves of children
        ## ---------------------------
        leaves = []
        if node.positive_child:
            leaves.extend(self.collect_leaves(node.positive_child))
        if node.negative_child:
            leaves.extend(self.collect_leaves(node.negative_child))
        return leaves
        ## ---------------------------

    def return_all_leaves(self):
        return self.collect_leaves(self.root)

my_decsion = Decision(
    Node(
        "root",
        Node("root_a", None, None),
        Node(
            "root_b",
            Node("root_b_1", None),
            Node("root_b_2", None),
        ),
    )
)

for node in my_decsion.return_all_leaves():
    print(node)