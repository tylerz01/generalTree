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
            new_color_class = "color-1" if parent_node.color_class == "color-0" else "color-0"
            new_node = TreeNode(new_data, color_class=new_color_class)
            parent_node.add_child(new_node)
            self.resources -= 10
            return True, new_node
        return False, None

    def get_tree_display_for_html(self):
        def build_html(node, depth=0):
            node_class = "node" if depth == 0 else "child-node"
            color_class = getattr(node, 'color_class', '')
            html_out = f'<div class="{node_class} {color_class}">{node.data}</div>'
            
            if node.children:
                children_html = ''
                for child in node.children:
                    connect_line = f'<div class="connect-line {node.color_class}"></div>' if depth >= 0 else ''
                    children_html += f'<div class="node-container">{connect_line}{build_html(child, depth + 1)}</div>'
                html_out += f'<div class="children">{children_html}</div>'
            return html_out
    
        return f'<div class="node-container">{build_html(self.root)}</div>'
    

    def preorder_traversal(self, node, visited=None):
        if visited is None:
            visited = []
        if node is not None:
            visited.append(node.data) 
            for child in node.children:  
                self.preorder_traversal(child, visited)
        return visited

    def postorder_traversal(self, node, visited=None):
        if visited is None:
            visited = []
        if node is not None:
            for child in node.children:  
                self.postorder_traversal(child, visited)
            visited.append(node.data)  
        return visited
    
    def inorder(self, node):
        pass
