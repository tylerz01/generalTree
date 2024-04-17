from flask import Flask, request, render_template
from tree_game import TreeGame

app = Flask(__name__)
game = TreeGame()

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    message_class = "hidden"
    traversal_order = None

    if request.method == "POST":
        action = request.form.get("action")
        parent_data = request.form.get("parent_data", "")
        data = request.form.get("data", "")

        if action == "grow":
            parent_node = game.find_node_by_data(game.root, parent_data)
            if parent_node:
                success, _ = game.grow(parent_node, data)
                if not success:
                    message = "Not enough resources to grow."
                    message_class = "error"
            else:
                message = "Parent not found."
                message_class = "error"
        elif action == "preorder":
            traversal_order, _ = game.preorder_traversal(game.root)
            message = "Preorder traversal activated."
            message_class = "info"
        elif action == "inorder":
            traversal_order, _ = game.inorder_traversal(game.root)
            message = "inorder traversal activated."
            message_class = "info"
        elif action == "postorder":
            traversal_order, _ = game.postorder_traversal(game.root)
            message = "Postorder traversal activated."
            message_class = "info"

    tree_display = game.get_tree_display_for_html(traversal_order=traversal_order)

    return render_template("home.html", 
                           message=message, 
                           message_class=message_class, 
                           tree_display=tree_display)

if __name__ == "__main__":
    app.run(debug=True)