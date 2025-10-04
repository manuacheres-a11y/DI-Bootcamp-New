#Exercise 1 : Hello World - Print the following output in one line of code:
text = "Hello World "
for i in range(4):
    print(text)
#Exercise 2 : Some Math - Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).
a = 99
b = 3
c = 8
result = (a^b) * c
print(result)
#Exercise 3 : What’s your name ? - Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.
my_name = "manu"
your_name = input("what's your name ?")
if your_name == my_name:
    print("hey brother")
else:
    print("No way")
#Exercise 4 : Tall enough to ride a roller coaster / Write code that will ask the user for their height in centimeters. / If they are over 145cm print a message that states they are tall enough to ride./ If they are not tall enough print a message that says they need to grow some more to ride.
height = int(input("What' your height in cm ?"))
if height > 145:
    print("ok, enough tall to ride")
else:
    print("sorry you can't go")
#Exercise 5 : Favorite Numbers - Key Python Topics: Sets / Adding/removing items in a set / Set concatenation (using union)heir height in centimeters. / If they are over 145cm print a message that states they are tall enough to ride./ If they are not tall enough print a message that says they need to grow some more to ride.
my_fav_numbers = {6,9,10,12,20}
my_fav_numbers.add(35)
my_fav_numbers.add(42)
print("after  completing, my_fav_numbers 's :", my_fav_numbers)
my_fav_numbers.remove(42)
print("after  removing, my_fav_numbers 's :",my_fav_numbers)
friend_fav_numbers = {1, 2, 3, 6}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)
#Exercise 6 : Tuple
my_tuple = (1, 2, 3, 4)
print("Tuple initial :", my_tuple)
try:
    my_tuple.append(5)
    print(my_tuple)
except:
    print("Erreur")
#Exercise 7 : Manipulation de listes   
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
print(basket)
basket.append("Kiwis")
print(basket)
basket.insert(0,"Apples")
print(basket)
print(basket.count("Apples"))
basket.clear()
print(basket)
#Exercise 8 : Sandwich Orders
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
print("Commandes après suppression du pastrami :", sandwich_orders)
finished_sandwiches=[]
print(finished_sandwiches)
sandwich_orders_two = sandwich_orders[:]
print(sandwich_orders_two)
for sandwich in sandwich_orders_two :
    finished_sandwiches.append(sandwich)
    sandwich_orders.remove(sandwich)
    print(f"I made your {sandwich}")

