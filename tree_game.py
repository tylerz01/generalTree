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

    def get_tree_display_for_html(self, traversal_order=None):
        def build_html(node, depth=0):
            node_class = "node" if depth == 0 else "child-node"
            color_class = getattr(node, 'color_class', '')
            order_attr = ""
            
            if traversal_order:
                node_data_list = [item[0] for item in traversal_order]
                if node.data in node_data_list:
                    node_order = node_data_list.index(node.data) + 1
                    order_attr = f' data-traversal-order="{node_order}"'

            html_out = f'<div class="{node_class} {color_class}"{order_attr}>{node.data}</div>'
            
            if node.children:
                children_html = ''
                for child in node.children:
                    connect_line = '<div class="connect-line"></div>'
                    children_html += f'<div class="node-container">{connect_line}{build_html(child, depth + 1)}</div>'
                html_out += f'<div class="children">{children_html}</div>'
            return html_out

        return f'<div class="node-container">{build_html(self.root)}</div>'

    def preorder_traversal(self, node, visited=None, order=0):
        if visited is None:
            visited = []
        if node is not None:
            visited.append((node.data, order))
            order += 1
            for child in node.children:
                order = self.preorder_traversal(child, visited, order)[1]
        return visited, order

    def inorder_traversal(self, node, visited=None, order=0):
        if visited is None:
            visited = []
        if node is not None:
            if node.children:
                order = self.inorder_traversal(node.children[0], visited, order)[1]
            visited.append((node.data, order))
            order += 1
            if len(node.children) > 1:
                order = self.inorder_traversal(node.children[1], visited, order)[1]
        return visited, order

    def postorder_traversal(self, node, visited=None, order=0):
        if visited is None:
            visited = []
        if node is not None:
            for child in node.children:
                order = self.postorder_traversal(child, visited, order)[1]
            visited.append((node.data, order))
            order += 1
        return visited, order
