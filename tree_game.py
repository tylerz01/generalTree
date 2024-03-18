from tree_node import TreeNode

class TreeGame:
    def __init__(self):
        self.root = TreeNode("Root")
        self.resources = 100
        
    def find_node_by_data(self, node, data):
        if node.data == data:
            return node
        for child in node.children:
            result = self.find_node_by_data(child, data)
            if result is not None:
                return result
        return None
    
    def grow(self, parent_node, new_data):
        if self.resources > 0:
            new_node = TreeNode(new_data)
            parent_node.add_child(new_node)
            self.resources -= 10
            return True, new_node
        return False, None

    def get_tree_display_for_html(self):
        def build_html(node, depth=0):
            node_class = "node" if depth == 0 else "child-node"
            html_out = f'<div class="{node_class}"><button type="button">{node.data}</button></div>'
            
            if node.children:
                html_out += '<div class="children">' 
                for child in node.children:
                    html_out += f'<div class="node-container">{build_html(child, depth + 1)}</div>'
                html_out += '</div>'
            return html_out

        return f'<div class="node-container">{build_html(self.root)}</div>'


