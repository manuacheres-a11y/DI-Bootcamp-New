# game.py
import random

class Game:
    def get_user_item(self):
        """Demande à l'utilisateur de choisir pierre/papier/ciseaux."""
        choices = ['pierre', 'papier', 'ciseaux']
        while True:
            user_input = input("Choisissez (pierre, papier, ciseaux) : ").strip().lower()
            if user_input in choices:
                return user_input
            else:
                print("Choix invalide. Veuillez réessayer.")

    def get_computer_item(self):
        """Renvoie un choix aléatoire pour l'ordinateur."""
        return random.choice(['pierre', 'papier', 'ciseaux'])

    def get_game_result(self, user_item, computer_item):
        """Détermine le résultat du jeu."""
        if user_item == computer_item:
            return "draw"
        
        # Conditions de victoire
        if (
            (user_item == "pierre" and computer_item == "ciseaux") or
            (user_item == "papier" and computer_item == "pierre") or
            (user_item == "ciseaux" and computer_item == "papier")
        ):
            return "win"
        else:
            return "loss"

    def play(self):
        """Joue une partie complète et retourne le résultat."""
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        # Affichage du résultat
        print(f"\nVous avez sélectionné : {user_item}.")
        print(f"L'ordinateur a sélectionné : {computer_item}.")

        if result == "win":
            print("Vous avez gagné ! 🎉")
        elif result == "loss":
            print("Vous avez perdu 😢")
        else:
            print("Égalité 🤝")

        return result