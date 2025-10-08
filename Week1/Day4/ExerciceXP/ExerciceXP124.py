#Exercice1
# Intructions:
# Use the provided Pets and Cat classes to create a Siamese breed, instantiate cat objects, and use the Pets class to manage them.
# See the example below, before diving in.
# Step 1: Create the Siamese Class
# Create a class called Siamese that inherits from the Cat class.
# You can add any specific attributes or methods for the Siamese breed, or leave it as is if there are no unique behaviors.
# Step 2: Create a List of Cat Instances
# Create a list called all_cats that contains instances of Bengal, Chartreux, and Siamese cats.
# Example: all_cats = [bengal_obj, chartreux_obj, siamese_obj]
# Give each cat a name and age.
# Step 3: Create a Pets Instance
# Create an instance of the Pets class called sara_pets, passing the all_cats list as an argument.
# Step 4: Take Cats for a Walk
# Call the walk() method on the sara_pets instance.
# This should print the result of calling the walk() method on each cat in the list.
# Example:
class Pets():
    def __init__(self, animals):
        self.animals = animals
    def walk(self):
        for animal in self.animals:
            print(animal.walk())
class Cat():
    is_lazy = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def walk(self):
        return f'{self.name} is just walking around'
class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'
class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
# Step 1: Create the Siamese class
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Step 2: Create a list of cat instances
all_cats = []

cat1 = Siamese("Jasmine",12)
cat2 = Chartreux("Neige",3)
cat3 = Bengal("Lilou",14)

all_cats.append(cat1)
all_cats.append(cat2)
all_cats.append(cat3)

# Step 3: Create a Pets instance of the list of cat instances
sara_pets = Pets(all_cats)

# Step 4: Take cats for a walk
sara_pets.walk()

print(all_cats)

# Exercice 2 : Chiens
# Instructions:
# Étape 1 : Créer la classe Chien

# Créez une classe appelée Dogavec les attributs name, age, et weight.
# Implémenter une bark()méthode qui renvoie «aboie”.
# Implémentez une run_speed()méthode qui renvoie weight / age * 10.
# Implémentez une fight(other_dog)méthode qui renvoie une chaîne indiquant quel chien a gagné le combat, en fonction de run_speed * weight.

class Dog():
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"
    def run_speed(self):
        return self.weight / self.age * 10

# Étape 2 : Créer des instances de chien
# Créez trois instances de la Dogclasse avec des noms, des âges et des poids différents.
# Étape 3 : Méthodes de test du chien
# Appelez les méthodes bark(), run_speed(), et fight()sur les instances de chien pour tester leur fonctionnalité.

def fight(self, other_dog):
        dog1 = self.run_speed() * self.weight
        dog2 = other_dog.run_speed() * other_dog.weight
        if dog1 > dog2:
            return f"{self.name} won the figth"
        else:
            return f"{other_dog.name} won the fight"
        
dog1 = Dog("Lady",2,18)
dog2 = Dog("Telma",3,25)
dog3 = Dog("Eugénie",14,35)

print(dog1.bark())
print(dog2.bark())
print(dog3.bark())

print(dog1.run_speed())
print(dog2.run_speed())
print(dog3.run_speed()) 

# Exercice 4 : Classes familiales et personnelles
# Instructions:
# Étape 1 : Créer la Personclasse
# Définissez une Personclasse avec les attributs suivants :
# first_name
# age
# last_name(chaîne, doit être initialisée comme une chaîne vide)
class Person():
    def __init__(self,first_name,age,last_name=""):
        self.first_name = first_name
        self.age = age
        self.last_name =last_name
# Ajoutez une méthode appelée is_18():
# Il devrait revenir Truesi la personne a 18 ans ou plus, sinon False.
    def is_18(self):
        if self.age >= 18:
            return True
        else:
            return False

# Étape 2 : Créer la Familyclasse
# Définir une Familyclasse avec :
# Un last_nameattribut
# Une membersliste qui stockera Persondes objets (doit être initialisée comme une liste vide)
# Ajoutez une méthode appelée born(first_name, age):
# Il devrait créer un nouvel Personobjet avec le prénom et l'âge donnés.
# Il faudrait attribuer le nom de famille à la personne.
# Il faudrait ajouter cette nouvelle personne à la membersliste.
# Ajoutez une méthode appelée check_majority(first_name):
# Il devrait rechercher membersdans la liste une personne avec cela first_name.
# Si la personne existe, appelez sa is_18()méthode.
# Si la personne a plus de 18 ans, indiquez :
# "You are over 18, your parents Jane and John accept that you will go out with your friends"
# Sinon, imprimez :
# "Sorry, you are not allowed to go out with your friends."
# Ajoutez une méthode appelée family_presentation():
# Il devrait imprimer le nom de famille.
# Ensuite, il devrait imprimer le prénom et l'âge de chaque membre de la famille.
class Family:
    def __init__(self,last_name):
        self.last_name = last_name
        self.members = []
    
    def born(self,first_name,age):
        person = Person(first_name,age)
        person.last_name = self.last_name
        self.members.append(person)

    def check_majority(self,first_name):
        for member in self.members:
            if first_name == member.first_name:
                is18 = member.is_18()
                if is18:
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")

    def family_presentation(self):
        print(f"This is the {self.last_name}")
        for member in self.members:
            print(f"{member.first_name} is {member.age}")

# Comportement attendu :

# Une fois mis en œuvre, votre programme devrait vous permettre de :

# Créez une famille avec un nom de famille.
# Ajoutez des membres à la famille en utilisant la born()méthode.
# Utilisé check_majority()pour voir si quelqu'un est autorisé à sortir.
# Afficher les informations familiales avec family_presentation().
# N'oubliez pas de tester vos classes en créant une instance de Family, en ajoutant des membres et en appelant chaque méthode pour voir le résultat attendu.

family = Family("Tuche")
family.born("Jeff",45)
family.born("Cathy",42)
family.born("Donald",14)
family.born("Steph",18)
family.born("Wilfried",22)

family.check_majority("Donald")
family.check_majority("Steph")
family.family_presentation()