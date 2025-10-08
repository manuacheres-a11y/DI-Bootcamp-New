# Exercice 3 : Chiens domestiqués
# Objectif : Créer une PetDogclasse qui hérite Doget ajoute des entraînements et des astuces.
# Instructions:
# Étape 1 : Importer la classe Dog
from ExerciceXP124 import Dog
import random

# Étape 2 : Créer la classe PetDog
# Créez une classe appelée PetDogqui hérite de la Dogclasse.
# Ajoutez un trainedattribut à la __init__méthode, avec une valeur par défaut de False.
# trainedsignifie que le chien est entraîné à faire quelques tours.
# Implémentez une train()méthode qui imprime la sortie de bark()et définit trainedsur True.
# Implémenter une play(*args)méthode qui imprime «tous jouent ensemble".
# *argsCette méthode contient une liste d'instances de chien.
# Implémentez une do_a_trick()méthode qui affiche une astuce aléatoire si trainedest True.
# Utilisez cette liste pour les astuces aléatoires :
# tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
# choisissez un index de rendu à chaque appel de la méthode.
class PetDog(Dog):
    def __init__(self,name,age,weight,trained=False):
        self.name = name
        self.age = age
        self.weight = weight
        self.trained = trained

    def train(self):
        self.trained = True
        return self.bark()
    
    def play(self,*args):
        dogs_list_string = ""
        for dog in args:
            if dogs_list_string != "":
                dogs_list_string = dogs_list_string + ", " + dog.name
            else:
                dogs_list_string = dog.name
        print(f"{dogs_list_string} : all play together")

    def do_a_trick(self):
        tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
        if self.trained is True:
            print(f"{self.name} {random.choice(tricks)}")


# Étape 3 : tester les méthodes PetDog
dog1 = PetDog("Lady",2,18)
dog2 = PetDog("Telma",3,25)
dog3 = PetDog("Eugénie",14,35)
print(dog1.train())
dog1.do_a_trick()
dog1.play(dog1,dog2,dog3)

