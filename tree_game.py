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
            return True, new_node
        return False, None

    def _gather_levels(self, node, depth=0, levels=None, parent_data=""):
        if levels is None:
            levels = []
        if len(levels) <= depth:
            levels.append([])
        node_repr = f"{parent_data}->{node.data}" if parent_data else node.data
        levels[depth].append(node_repr)
        
        for child in node.children:
            self._gather_levels(child, depth + 1, levels, node.data)
        return levels

    def display_tree(self):
        levels = self._gather_levels(self.root)
        max_width = max(len(" ".join(level)) for level in levels)
        for level in levels:
            level_str = " ".join(level).center(max_width)
            print(level_str)