#This will determine if a number is divisible by 5 based off of user's input
num=int(input("please give me a whole number:"))
if num % 5 == 0:
    print(f"{num} is divisible by 5.")
else:
    print(f"{num} is not divisible by 5.")

# Creating a dictionary of states and their capitals with the if/elif/else approach
states_capitals = {
    "Wisconsin": "Madison",
    "Colorado": "Denver",
    "California": "Sacramento",
    "Texas": "Austin",
    "New York": "Albany",
    "Florida": "Tallahassee"
}
state = input("The options for states are Wisconsin, Colorado, California, Texas, New York, and Florida. It is capital sensitive! Enter the name of a state: ")
if state == "Wisconsin":
    print("The capital of Wisconsin is Madison.")
elif state == "Colorado":
    print("The capital of Colorado is Denver.")
elif state == "California":
    print("The capital of California is Sacramento.")
elif state == "Texas":
    print("The capital of Texas is Austin.")
elif state == "New York":
    print("The capital of New York is Albany.")
elif state == "Florida":
    print("The capital of Florida is Tallahassee.")
else:
    print("I do not know that one.")

#Now I will do the same thing using match case
states_capitals = {
    "Wisconsin": "Madison",
    "Colorado": "Denver",
    "California": "Sacramento",
    "Texas": "Austin",
    "New York": "Albany",
    "Florida": "Tallahassee"
}
state = input("The options for states are Wisconsin, Colorado, California, Texas, New York, and Florida. It is capital sensitive! Enter the name of a state: ")
match state:
    case "Wisconsin":
        print("The capital of Wisconsin is Madison.")
    case "Colorado":
        print("The capital of Colorado is Denver.")
    case "California":
        print("The capital of California is Sacramento.")
    case "Texas":
        print("The capital of Texas is Austin.")
    case "New York":
        print("The capital of New York is Albany.")
    case "Florida":
        print("The capital of Florida is Tallahassee.")
    case _:
        print("I do not know that one.")

#This will be the if/then/else approach
state = input("The options for states are Wisconsin, Colorado, California, Texas, New York, and Florida. It is capital sensitive! Enter a State name: ")
if state == "Wisconsin":
    print("Madison")
elif state == "Colorado":
    print("Denver")
elif state == "California":
    print("Sacramento")
elif state == "Texas":
    print("Austin")
elif state == "New York":
    print("Albany")
elif state == "Florida":
    print("Tallahassee")
else:
    print("I do not know that one.")

#This will be the dictionary approach
states_capitals = {
    "Oregon": "Salem",
    "Washington": "Olympia",
    "Idaho": "Boise",
    "Wisconsin": "Madison",
    "Colorado": "Denver",
    "California": "Sacramento"
}
state = input("Your options are Oregon, Washington, Idaho, Wisconsin, Colorado, and California. It is upper case sensitive.Enter the name of a state: ")
capital = states_capitals.get(state, "Not found")
print(f"The capital of {state} is: {capital}")

#Lastly, the matchcase approach
state = input("Your options are Oregon, Washington, Idaho, Wisconsin, Colorado, and California. It is upper case sensitive.Enter a State name: ")
match state:
    case "Oregon":
        print("The capital of Oregon is Salem.")
    case "Washington":
        print("The capital of Washington is Olympia.")
    case "Idaho":
        print("The capital of Idaho is Boise.")
    case "Wisconsin":
        print("The capital of Wisconsin is Madison.")
    case "Colorado":
        print("The capital of Colorado is Denver.")
    case "California":
        print("The capital of California is Sacramento.")
    case _:
        print("I do not know that one.")

#This is elif in a function definition, using the information from exercise 4. As well as docstrings to document the function
def pool_admission(age):
    """
    This function calculates the entrance price to the pool based on the given age.

    The pricing is as follows:
    - Under 2 years: free
    - Age 2–11: $3
    - Age 12–60: $6
    - Over 60 years: $4

    Parameters:
    age (int): The age of the person.

    Returns:
    int: The price for the pool admission based on the person's age.
    """
    if age < 2:
        return 0
    elif age < 12:
        return 3
    elif age <= 60:
        return 6
    else:
        return 4
age = int(input("You'd like to buy a ticket to the pool! Enter your age to find out the ticket price: "))
price = pool_admission(age)
print(f"The pool admission price for age {age} is ${price}.")

#I will determine how many times the string "160" shows up on the coccbobcat.com
import requests
url = "http://coccbobcat.com"
response = requests.get(url)
if response.status_code == 200:
    html_content = response.text
    count = html_content.count("160")
    print(f'The substring "160" appears {count} times in the HTML source of {url}.')
else:
    print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")

#Now I will write a program to determine the number of processes running on my system psutil
import psutil
processes = psutil.pids()
print(f"Number of running processes: {len(processes)}")
print("Process finished with exit code 0")


