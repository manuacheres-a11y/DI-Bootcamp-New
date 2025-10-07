#Defi1
number = int(input("type a number"))
length = int(input("type8" \
"44 a length"))
multiples_of_the_number = [number * i for i in range(1, length + 1)]
print(multiples_of_the_number)
#Defi2
word = input("type a word : ")
new_word = ""
for letter in word:
    if not new_word or letter != new_word[-1]:
        new_word += letter
print("Résultat :", new_word)