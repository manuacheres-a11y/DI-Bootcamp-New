from game import Game

def get_user_menu_choice():
    """Affiche le menu principal et renvoie le choix de l'utilisateur."""
    print("\n=== Menu Principal ===")
    print("1. Jouer une nouvelle partie")
    print("2. Afficher les scores")
    print("x. Quitter le jeu")

    choice = input("Votre choix : ").strip().lower()
    if choice in ['1', '2', 'x', 'q']:
        return choice
    else:
        print("Choix invalide. Réessayez.")
        return get_user_menu_choice()

def print_results(results):
    """Affiche les résultats finaux."""
    print("\n=== Résumé du jeu ===")
    print(f"Victoires : {results['win']}")
    print(f"Défaites : {results['loss']}")
    print(f"Matchs nuls : {results['draw']}")
    print("\nMerci d'avoir joué à Pierre-Papier-Ciseaux ! 👋")

def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        if choice == '1':
            game = Game()
            result = game.play()
            results[result] += 1

        elif choice == '2':
            print_results(results)

        elif choice in ['x', 'q']:
            print_results(results)
            break

if __name__ == "__main__":
    main()