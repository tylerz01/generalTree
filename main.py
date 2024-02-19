from tree_game import TreeGame
def main():
    game = TreeGame()
    game_running = True

    while game_running:
        print("\nCurrent Tree:")
        game.display_tree()
        print(f"Resources: {game.resources}")
        
        action = input("Choose an action (grow, end): ")

        if action == "grow":
            data = input("Enter new branch/leaf name: ")
            if not game.grow(game.root, data):
                print("Not enough resources to grow.")
        elif action == "end":
            game_running = False
        else:
            print("Invalid action.")

    print("Game Over")

if __name__ == "__main__":
    main()
