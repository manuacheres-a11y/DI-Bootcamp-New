import random

class Game:
    def get_user_item(self):
        """Demande à l'utilisateur de choisir pierre, papier ou ciseaux"""
        options = ['pierre', 'papier', 'ciseaux']
        user_choice = None

        while user_choice not in options:
            user_choice = input("Choisissez pierre, papier ou ciseaux : ").strip().lower()
            if user_choice not in options:
                print("Choix invalide. Essayez encore.")

        return user_choice

    def get_computer_item(self):
        """Choisit aléatoirement pierre, papier ou ciseaux pour l'ordinateur"""
        options = ['pierre', 'papier', 'ciseaux']
        computer_choice = random.choice(options)
        return computer_choice

    def get_game_result(self, user_item, computer_item):
        """Détermine le résultat du jeu"""
        if user_item == computer_item:
            return "match nul"
        elif (
            (user_item == "pierre" and computer_item == "ciseaux") or
            (user_item == "papier" and computer_item == "pierre") or
            (user_item == "ciseaux" and computer_item == "papier")
        ):
            return "victoire"
        else:
            return "défaite"

    def play(self):
        """Joue un tour complet du jeu"""
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"\nVous avez sélectionné : {user_item}")
        print(f"L'ordinateur a sélectionné : {computer_item}")

        if result == "victoire":
            print("🎉 Vous avez gagné !")
        elif result == "match nul":
            print("🤝 C’est un match nul !")
        else:
            print("😞 Vous avez perdu.")

        return result
    
# from game import Game

def get_user_menu_choice():
    """Affiche le menu principal et récupère le choix de l'utilisateur"""
    print("\n=== Menu Principal ===")
    print("(1) Jouer une nouvelle partie")
    print("(2) Afficher les scores")
    print("(x) Quitter")
    
    choice = input("Votre choix : ").strip().lower()

    while choice not in ['1', '2', 'x']:
        print("Choix invalide. Veuillez réessayer.")
        choice = input("Votre choix : ").strip().lower()

    return choice


def print_results(results):
    """Affiche les résultats finaux du jeu"""
    print("\n=== Résultats du jeu ===")
    print(f"Victoires : {results['victoire']}")
    print(f"Défaites : {results['défaite']}")
    print(f"Matchs nuls : {results['match nul']}")
    print("\nMerci d'avoir joué ! 👋")


def main():
    results = {"victoire": 0, "défaite": 0, "match nul": 0}

    while True:
        choice = get_user_menu_choice()

        if choice == '1':
            game = Game()
            result = game.play()
            results[result] += 1

        elif choice == '2':
            print_results(results)

        elif choice == 'x':
            print_results(results)
            break


if __name__ == "__main__":
    main()