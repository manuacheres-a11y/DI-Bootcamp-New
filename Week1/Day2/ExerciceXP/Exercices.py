# #Exercise 1: Converting Lists into Dictionaries
# #You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.
# Lists:
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected Output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
keys = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]
dictionnaire = dict(zip(keys, values))
print(dictionnaire)

# 🌟 Exercise 2: Cinemax #2
# Key Python Topics:
# Looping through dictionaries
# Conditionals
# Calculations
# Instructions
# Write a program that calculates the total cost of movie tickets for a family based on their ages.
# Family members’ ages are stored in a dictionary.
# The ticket pricing rules are as follows:
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $15
# Family Data:
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# Loop through the family dictionary to calculate the total cost.
# Print the ticket price for each family member.
# Print the total cost at the end.
# Bonus:
# Allow the user to input family members’ names and ages, then calculate the total ticket cost.
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
def ticket_calculator(family):
    total_cost = 0
    for member, age in family.items():
        if age < 3:
            total_cost = total_cost
            print(f"it is free for {member} !")
        elif age <= 12:
            total_cost = total_cost + 10
            print(f"{member} has to pay 10 US dollars")
        elif age > 12:
            total_cost = total_cost + 15
            print(f"{member} has to pay 15 US dollars")
    return total_cost

total_cost = ticket_calculator(family)
print(f"The total cost for the whole family is : {total_cost} US dollars")

while(True):
    add_family_members = input("Do you want to add more family member(s) ? (Y/N)")
    if add_family_members == "Y":
        new_member_name = input("What is their name ?")
        new_member_age = int(input("What is their age ?"))
        family[new_member_name]=new_member_age
    else:
        break

total_cost = ticket_calculator(family)
print(f"The total cost for the whole family is : {total_cost} US dollars")

# 🌟 Exercise 3: Zara
# Key Python Topics:
# Creating dictionaries
# Accessing and modifying dictionary elements
# Dictionary methods like .pop() and .update()
# Instructions
# Create and manipulate a dictionary that contains information about the Zara brand.
# Brand Information:
# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green
# Create a dictionary called brand with the provided data.
# Modify and access the dictionary as follows:
# Change the value of number_stores to 2.
# Print a sentence describing Zara’s clients using the type_of_clothes key.
# Add a new key country_creation with the value Spain.
# Check if international_competitors exists and, if so, add “Desigual” to the list.
# Delete the creation_date key.
# Print the last item in international_competitors.
# Print the major colors in the US.
# Print the number of keys in the dictionary.
# Print all keys of the dictionary.
# Bonus:
# Create another dictionary called more_on_zara with creation_date and number_stores. Merge this dictionary with the original brand dictionary and print the result.

brand = {"name" : "Zara", "creation_date" : 1975, "creator_name" : "Amancio Ortega Gaona", "type_of_clothes" :"men, women, children, home", "international_competitors" : "Gap, H&M, Benetton", "number_stores" : 7000, "major_color" : {"France" : "blue", "Spain" : "red", "US" : "pink, green"}}
print(brand)
brand.update({"number_stores" : 2})
print(f"Zara is a brand which offers some clothes for {brand["type_of_clothes"]}")
brand["country_creation"]= "Spain"
print(brand)
for key, value in brand.items():
    if key == "international_competitors":
        brand[key] = brand[key] + ", Desigual"
print(brand)
brand.pop("creation_date")
print(brand)
print(brand["major_color"]["US"])
number_of_keys = 0
for key in brand :
    number_of_keys += 1
print(f"There are {number_of_keys} keys in that dictionary")
for key in brand :
    print(key)


# 🌟 Exercise 4 : Some Geography
# Goal: Create a function that describes a city and its country.
# Key Python Topics:
# Functions with multiple parameters
# Default parameter values
# String formatting
# Step 1: Define a Function with Parameters
# Define a function named describe_city().
# This function should accept two parameters: city and country.
# Give the country parameter a default value, such as “Unknown”.
def describe_city(city, country="unknown"):
# Step 2: Print a Message
# Inside the function, set up the code to display a sentence like “ is in “.
    print(f"{city} is in {country}")
# Replace <city> and <country> with the parameter values.
# Step 3: Call the Function
# Call the describe_city() function with different city and country combinations.
# Try calling it with and without providing the country argument to see the default value in action.
# Example: describe_city("Reykjavik", "Iceland") and describe_city("Paris").
describe_city("Reykjavik", "Iceland")
describe_city("Paris")
# Expected Output:
# Reykjavik is in Iceland.
# Paris is in Unknown.

# 🌟 Exercise 5 : Random
# Goal: Create a function that generates random numbers and compares them.
# Key Python Topics:
# random module
# random.randint() function
# Conditional statements (if, else)
# Step 1: Import the random Module
import random
# At the beginning of your script, use import random to access the random number generation functions.
# Step 2: Define a Function with a Parameter
# Create a function that accepts a number between 1 and 100 as a parameter.
random_number = random.randint(1,100)
# Step 3: Generate a Random Number
# Inside the function, use random.randint(1, 100) to generate a random integer between 1 and 100.
print(random_number)
# Step 4: Compare the Numbers
# If they are the same, print a success message. Otherwise, print a fail message and display both numbers.
# Step 5: Call the Function
# Call the function with a number between 1 and 100.
# Expected Output:
# Success! (if the numbers match)
# Fail! Your number: 50, Random number: 23 (if they don't match)
def int_accept(number):
    if 1 < number <=100:
        random_number = random.randint(1, 100)
        if number == random_number:
            print("Sucess!")
        else:
            print(f"Fail! Your number: {number}, Random number: {random_number}")
    else:
        return None
int_accept(50)



# 🌟 Exercise 6 : Let’s create some personalized shirts !
# Goal: Create a function to describe a shirt’s size and message, with default values.
# Key Python Topics:
# Functions with parameters and default values
# Keyword arguments
# Step 1: Define a Function with Parameters
# Define a function called make_shirt().
# This function should accept two parameters: size and text.
def make_shirt(size="large",text="I love Python"):
    print(f"the shirt size is {size} and {text}")
# Step 2: Print a Summary Message
# Set up the function to display a sentence summarizing the shirt’s size and message.
# Step 3: Call the Function
make_shirt("XXXL","oups !")
print(make_shirt)
# Step 4: Modify the Function with Default Values
# Modify the make_shirt() function so that size has a default value of “large” and text has a default value of “I love Python”.

# Step 5: Call the Function with Default and Custom Values
# Call make_shirt() to make a large shirt with the default message.
make_shirt()
# Call make_shirt() to make a medium shirt with the default message.
make_shirt("medium")
# Call make_shirt() to make a shirt of any size with a different message.
make_shirt("XL","are you sure of your size ?")
# Step 6 (Bonus): Keyword Arguments
# Call make_shirt() using keyword arguments (e.g., make_shirt(size="small", text="Hello!")).
# Expected Output:
# The size of the shirt is large and the text is I love Python.
# The size of the shirt is medium and the text is I love Python.
# The size of the shirt is small and the text is Custom message.

# 🌟 Exercise 7 : Temperature Advice
# Goal: Generate a random temperature and provide advice based on the temperature range.
# Key Python Topics:
# Functions
# Conditionals (if / elif)
# Random numbers
# Floating-point numbers (Bonus)
# Handling seasons (Bonus)
# Step 1: Create the get_random_temp() Function
import random
# Create a function called get_random_temp() that returns a random integer between -10 and 40 degrees Celsius.
def get_random_temp(season):
    if season == "Winter":
        temperature = -2
    elif season == "Spring":
        temperature = 15
    elif season == "Summer":
        temperature = 35
    elif season == "Autumn":
        temperature = 22
    return temperature
# Step 2: Create the main() Function
# Create a function called main(). Inside this function:
def main(season):
    random_temp = get_random_temp(season)
    print(f"The temperature right now is {random_temp} degrees Celsius.")
    if random_temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif random_temp >=0 and random_temp <= 16:
        print("Quite chilly! Don't forget your coat")
    elif 16 <= random_temp <= 23:
        print("Nice weather.")
    elif 24 <= random_temp <= 32:
        print("A bit warm, stay hydrated,")
    elif 32 <= random_temp <= 40:
        print("It's really hot! Stay cool.")
main("Winter")
# Call get_random_temp() to get a random temperature.
# Store the temperature in a variable and print a friendly message like:
# “The temperature right now is 32 degrees Celsius.”
# Step 3: Provide Temperature-Based Advice
# Inside main(), provide advice based on the temperature:
# Below 0°C: e.g., “Brrr, that’s freezing! Wear some extra layers today.”
# Between 0°C and 16°C: e.g., “Quite chilly! Don’t forget your coat.”
# Between 16°C and 23°C: e.g., “Nice weather.”
# Between 24°C and 32°C: e.g., “A bit warm, stay hydrated.”
# Between 32°C and 40°C: e.g., “It’s really hot! Stay cool.”
# Step 4: Floating-Point Temperatures (Bonus)
# Modify get_random_temp() to return a random floating-point number using random.uniform() for more accurate temperature values.
# Step 5: Month-Based Seasons (Bonus)
# Instead of directly generating a random temperature, ask the user for a month (1-12) and determine the season using if/elif conditions.
# Modify get_random_temp() to return temperatures specific to each season.
# Expected Output:
# The temperature right now is 32 degrees Celsius.
# It's really hot! Stay cool.

month_input = int(input("Choose a month between 1 and 12"))

season_list = ["Winter","Winter","Spring","Spring","Spring","Summer","Summer","Summer","Autumn","Autumn","Autumn","Winter"]

season_list_length = len(season_list)

for season in range(1, season_list_length + 1):
    if month_input == season:
        season_output = season_list[season-1]
print(f"The season is : {season_output}")
main(season_output)


# 🌟 Exercise 8: Pizza Toppings
# Key Python Topics:
# Loops
# Lists
# String formatting
# Instructions:
# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.

toppings = []
price=10

while(True):
    topping = input("Please write a topping would you like to your pizza. If you want to quit, type 'quit'")
    if topping == "quit":
        break
    else:
        toppings.append(topping)
        price = price + 2.50
print("This is your toppings :")
for topping in toppings:
    print(topping)
print(f"The total cost of the pizza is : {price}$")
