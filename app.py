from flask import Flask, request, render_template
from tree_game import TreeGame

app = Flask(__name__)
game = TreeGame()

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    message_class = "hidden" 

    if request.method == "POST":
        action = request.form.get("action", "")
        if action == "preorder":
            visited = game.preorder_traversal(game.root)
            tree_display = " -> ".join(visited)
        elif action == "postorder":
            visited = game.postorder_traversal(game.root)
            tree_display = " -> ".join(visited)
        if action == "grow":
            parent_data = request.form.get("parent_data")
            data = request.form.get("data")
            if parent_data and data: 
                parent_node = game.find_node_by_data(game.root, parent_data)
                if parent_node:
                    success, message = game.grow(parent_node, data)
                    if not success:
                        message_class = "error" 
                    message = "Parent not found."
                    message_class = "error"
            else:
                message = "Please fill in both fields."
                message_class = "error"
        elif action == "preorder":
            pass
        elif action == "inorder":
            pass
        elif action == "postorder":
            pass
        elif action == "end":
            game.end_game() 
            return render_template("game_over.html") 

    tree_display = game.get_tree_display_for_html() 

    return render_template("home.html", 
                           message=message, 
                           message_class=message_class, 
                           tree_display=tree_display)

if __name__ == "__main__":
    app.run(debug=True)