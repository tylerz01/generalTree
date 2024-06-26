from tree_game import TreeGame

def find_node_by_data(node, data):
    if node.data == data:
        return node
    for child in node.children:
        result = find_node_by_data(child, data)
        if result is not None:
            return result
    return None

def tree_to_graph(node, graph=None, parent=None):
    graph.add_node(node.data)
    if parent:
        graph.add_edge(parent.data, node.data)
    for child in node.children:
        tree_to_graph(child, graph, node)
    return graph

def main():
    game = TreeGame()
    game_running = True

    while game_running:
        print("\nCurrent Tree:")
        game.display_tree()
        print(f"Resources: {game.resources}")
        
        action = input("Choose an action (grow, end): ")

        if action == "grow":
            parent_data = input("Enter parent branch/leaf name (or 'Root' to grow from the root): ")
            data = input("Enter new branch/leaf name: ")

            parent_node = find_node_by_data(game.root, parent_data)
            if parent_node is None:
                print("Parent not found.")
                continue

            success, _ = game.grow(parent_node, data)
            if not success:
                print("Not enough resources to grow.")
        elif action == "end":
            game_running = False
        else:
            print("Invalid action.")

    print("Game Over")

if __name__ == "__main__":
    main()
