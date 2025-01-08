#This is an F string describing my dead dog's breed and name:)
pet_type = 'Italian Mastiff'
pet_name = 'Beau'
print(f"I had an {pet_type} and his name was {pet_name}. ")

#Now I am asking the user to input info, in order to print out super exciting information that they already know haha
name = input(f"Enter your first name:")
age = int(input(f"Enter your current age...just a number...don't mess up my sentence;):"))
savings = int(input(f"Enter your yearly savings..just a number:"))
oldie = age + 10
total_savings = savings * 5
average_savings = total_savings/12
print(f"Hello {name}! You are currently {age} years old. In 10 years, you will be {oldie}. If you save ${savings} each year, in 5 years, you will have saved ${total_savings}. Your average monthly savings is ${average_savings}.")

#This will be an F string to print out the current seconds in the month!
import calendar
from datetime import datetime
current_date = datetime.now()
current_year = current_date.year
current_month = current_date.month
days_in_month = calendar.monthrange(current_year, current_month)[1]
seconds_in_month = days_in_month * 24 * 60 * 60
print(f"The number of seconds in the current month ({calendar.month_name[current_month]}) is: {seconds_in_month}")

#This will calculate how many "dozens" are created and the remainder of eggs, based off of the number that the user inputs
eggs = int(input(f"Enter the Number of eggs:"))
dozens = eggs//12
remainder = eggs%12
print(f"This makes {dozens} dozens of eggs, with {remainder} left over.")