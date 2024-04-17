class TreeNode:
    def __init__(self, data, color_class=None):
        self.data = data
        self.children = []
        self.color_class = color_class 

    def add_child(self, child_node):
        self.children.append(child_node)
