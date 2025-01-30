#This will define a function that returns the average of 3 numbers
def average_num(num1, num2, num3):
    """This function takes 3 numbers and returns the average
    Parameters
    ----------
    num1: int
        first
    num2: int
        second
    num3: int
        third
    :returns
    average of 3 numbers as an integer
    """
    return (num1 + num2 + num3)/3
print(average_num(8,3,4))
print(average_num(5,2,9))

#This will be a test of moving the function definition after the print statements
print(average_num(8,3,4))
print(average_num(5,2,9))
def average_num(num1, num2, num3):
    return (num1 + num2 + num3)/3
#The script does run! I think it works because it runs from top to bottom and could notice that there is a function being called on, so it is running through the script to see where that function is defined.

#This will be another test of printing out a value of a parameter outside of the defined function
def average_num(num1, num2, num3):
    return (num1 + num2 + num3)/3
print(average_num(8,3,4))
print(average_num(5,2,9))
#This script doesn't run and comes back with an error because 'num1' is not defined. I think because this variable is already defined within a function (average function), it won't work when it's called outside of the function. I'm taking out the print num1 to run the rest of my program.

#This function converts a dog's age into human years
def dogs_human_age(age):
    """This function calculates a dog's age into human years
       Parameters
       ----------
       age: int
           first
       :returns
       a dog's age into human years
       """
    return(24 + (age-2)*4)
print(f" 7 dog years is equivalent to", dogs_human_age(7), "human years.")

#This function will calculate the value of a car
def calculate_car_value(purchase_price, years, car_type):
    """
    Function to calculate the value of a car after a certain number of years
    based on its type and annual depreciation or appreciation rate.

    Parameters:
    - purchase_price (float): The initial price of the car.
    - years (int): The number of years that have passed.
    - car_type (str): The type of the car (either 'german', 'japanese', or 'italian').

    Returns:
    - The value of the car after the given number of years.
    """
    if car_type.lower() == 'german':
        rate = 0.05
    elif car_type.lower() == 'japanese':
        rate = 0.07
    elif car_type.lower() == 'italian':
        rate = 0.05
    else:
        raise ValueError("Invalid car type. Please choose 'german', 'japanese', or 'italian'.")

    return purchase_price * ((1 - rate) ** years)
car_value = calculate_car_value(20000, 7, 'italian')
print(f"The value of the italian car will be ${car_value:.2f} after 7 years.")
#This was the hardest one ;(

#This will define a function to convert a dog's age into human years and return the result. I will also make a input for a user to add their dog's age.
def dogs_human_age(age):
    """This function calculates a dog's age into human years based on user's input
       Parameters
       ----------
       age: int
           first
       :returns
       a dog's age into human years
       """
    return(24 + (age-2)*4)
print("Dog’s Age calculator:")
dog_name = input("What is your dog’s name? ")
age = int(input(f"How old is {dog_name}? "))
human_years = dogs_human_age(age)
print(f"Your {dog_name} is {human_years} human years old.")

#This will calculate the price of one ice cream cone
def calculate_ice_cream_price(scoops):
    """
    Calculate the price of an ice cream cone based on the number of scoops.
    Parameters:
    scoops (int): The number of scoops of ice cream.
    Returns:
    float: The total price of the cone.
    """
    price = (scoops * 1.15) + 2.25
    return price
def main():
    """
    Main function that interacts with the user to calculate the price of an ice cream cone.
    """
    print("Ice cream cone price calculator:")
    scoops = int(input("How many scoops would you like? "))
    price = calculate_ice_cream_price(scoops)
    print(f"A {scoops}-scoop cone will cost ${price:.2f}")
if __name__ == "__main__":
    main()




