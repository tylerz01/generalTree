from tree_node import TreeNode
class TreeGame:
    def __init__(self):
        self.root = TreeNode("Root")
        self.resources = 100  

    def grow(self, parent_node, new_data):
        if self.resources > 0:
            new_node = TreeNode(new_data)
            parent_node.add_child(new_node)
            self.resources -= 10 
            return True
        return False

    def display_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        print(' ' * level * 2 + node.data)
        for child in node.children:
            self.display_tree(child, level + 1)
