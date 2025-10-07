# Exercice 1 : Les chats
# Utilisez la Catclasse fournie pour créer trois objets chats. Créez ensuite une fonction pour trouver le chat le plus âgé et afficher ses informations.
# Étape 1 : Créer des objets Chat
# Utilisez la Catclasse pour créer trois objets chats avec des noms et des âges différents.

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
 
# Étape 2 : Créer une fonction pour trouver le chat le plus vieux
def find_oldest_cat(cat1, cat2, cat3):
        if cat1.age > cat2.age and cat1.age > cat3.age:
            oldest = cat1
        elif cat2.age > cat1.age and cat2.age > cat3.age:
            oldest = cat2
        else:
            oldest = cat3

        return oldest
# Créez une fonction qui prend les trois objets chat en entrée.
# À l'intérieur de la fonction, comparez les âges des chats pour trouver le plus vieux.
# Renvoie l'objet chat le plus ancien.

# Étape 3 : Imprimez les détails du chat le plus âgé

cat1 = Cat("Felix",3)
cat2 = Cat("Minouche",8)
cat3 = Cat("Rocky",6)

# Appelez la fonction pour obtenir le chat le plus âgé.
# Imprimez une chaîne formatée : « Le chat le plus âgé est <cat_name>, et a <cat_age>ans. »
# Remplacez <cat_name>et <cat_age>par le nom et l'âge du chat le plus âgé.
oldest_cat = find_oldest_cat(cat1,cat2,cat3)
print(f"The oldest cat is {oldest_cat.name} and is {oldest_cat.age} years old")

# Exemple:

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# # Step 1: Create cat objects
# # cat1 = create the object

# # Step 2: Create a function to find the oldest cat
# def find_oldest_cat(cat1, cat2, cat3):
#     # ... code to find and return the oldest cat ...

# # Step 3: Print the oldest cat's details


# 🌟 Exercice 2 : Chiens
# Objectif : créer une Dogclasse, instancier des objets, appeler des méthodes et comparer les tailles de chiens.



# Sujets clés de Python :

# Classes et objets
# Instanciation d'objet
# Méthodes
# Attributs
# Instructions conditionnelles ( if)

# Instructions:

# Créez une Dogclasse avec des méthodes pour aboyer et sauter. Instanciez des objets chiens, appelez leurs méthodes et comparez leurs tailles.



# Étape 1 : Créer la classe Chien

# Créez une classe appelée Dog.
# Dans la __init__méthode, prenez nameet heightcomme paramètres et créez les attributs correspondants.
# Créez une bark()méthode qui imprime «ça fait ouaf !
# Créez une jump()méthode qui imprime «sautscm de haut ! », où xest height * 2.

class Dog:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height

    def bark(self):
        print("dog is saying ouaf ouaf")         
         
    def jump(self):
        print(f"jumps {self.height*2} cm")

# Étape 2 : Créer des objets chien
# Créez davids_dogdes sarahs_dogobjets avec leurs noms et hauteurs respectifs.

davids_dog = Dog("Pluto", 40)
sarahs_dog = Dog("Toutou", 70)

# Étape 3 : Imprimer les détails du chien et les méthodes d'appel
# Imprimez le nom et la taille de chaque chien.
# Appelez les méthodes bark()et jump()pour chaque chien.

print(davids_dog.name, davids_dog.height)
print(sarahs_dog.name, sarahs_dog.height)


# Étape 4 : Comparer les tailles de chiens

davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
sarahs_dog.jump()

# 🌟 Exercice 3 : Qui est le producteur de la chanson ?
# Objectif : Créer une Songclasse pour représenter les paroles des chansons et les imprimer.
# Créez une Songclasse avec une méthode pour imprimer les paroles des chansons ligne par ligne.

# Étape 1 : Créer la classe de chanson
# Créez une classe appelée Song.
# Dans la __init__méthode, prenez lyrics(une liste) comme paramètre et créez un attribut correspondant.
# Créez une sing_me_a_song()méthode qui imprime chaque élément de la lyricsliste sur une nouvelle ligne.

class Song :
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line) 


stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()

# 🌟 Exercice 4 : Après-midi au zoo
# 1. Créez une classe appelée Zoo.
class Zoo:
    def __init__(self, zoo_name):
# Initialiser une liste vide appelée animals à garder une trace des noms d'animaux.
        self.animals = []
# 3. Ajoutez une méthode add_animal(new_animal):
# Cette méthode ajoute un nouvel animal à la animalsliste.
# N'ajoutez pas l'animal s'il est déjà dans la liste.
    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
# 4. Ajoutez une méthode get_animals():
# Cette méthode imprime tous les animaux actuellement présents dans le zoo.
    def get_animals(self):
        for animal in self.animals:
            print(animal)
# 5. Ajoutez une méthode sell_animal(animal_sold):
# Cette méthode vérifie si un animal spécifié existe dans la liste des animaux et, si tel est le cas, le supprime.
    def sell_animal(self,animal_sold):
        for animal in self.animals:
            if animal_sold in self.animals:
                self.animals.remove(animal_sold)

def sort_animals(self):
        sorted_animals = sorted(self.animals)
        dict_animals = {}

        for animal in sorted_animals:
            first_letter = animal[0].upper()
            if first_letter not in dict_animals:
                dict_animals[first_letter] = []
            dict_animals[first_letter].append(animal)
        return dict_animals

def get_groups(self):
    groups = self.sort_animals()
    for letter, animals in groups.items():
        print(f"{letter}: {animals}")

