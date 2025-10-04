from datetime import datetime
# Demander la date de naissance
date_naissance = input("Entrez votre date de naissance (format DD/MM/YYYY) : ")

# Convertir en objet date
date = datetime.strptime(date_naissance, "%d/%m/%Y")

# Calculer l'âge
today = datetime.today()
age = today.year - date.year - ((today.month, today.day) < (date.month, date.day))

# Dernier chiffre de l'âge = nombre de bougies
bougies = age % 10
if bougies == 0:
    cbougies = 10  # Pour éviter zéro bougie, option sympa :)

# Construire les bougies
nbre_bougies = "i" * bougies

# Afficher le gâteau
print("      ___" + nbre_bougies + "___")
print("     | H a p p y |")
print("   __|___________|__")
print("  |^^^^^^^^^^^^^^^^^|")
print("  | B i r t h d a y |")
print("  |                 |")
print("  ~~~~~~~~~~~~~~~~~~~")

print(f"\nJoyeux anniversaire ! Tu as {age} ans 🎉")
