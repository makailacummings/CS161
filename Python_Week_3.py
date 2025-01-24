#This will ask the user their name and then say hello and repeat their name
name = input("What is your name?")
print("Hi", name)

#I will ask the user their age and then tell them how old they will be 5 years from that age. The original code  written makes an error because you cannot add a string and an integer. The user's input needs to be turned into an integer before you can add. See below.
user_age = int(input("Please enter your age:"))
print("In 5 years,",name+ ", you will be" , user_age + 5)

#This will ask the user how many years they would like to their age and then give them the new age they will be using their input
years_to_add = int(input("How many years would you like to add to your current age?"))
future_age = user_age + years_to_add
print("In", str(years_to_add), "years, you will be",str(future_age),"years old." )

#This is determining the total amount of money a worker made in a week and their annual pay based off of that
hours_worked = float(input("Enter the amount of hours you have worked this week:"))
hourly_wage = float(input("Enter your hourly wage without the $ sign:"))
weekly_money = hours_worked * hourly_wage
annual_gross_pay = weekly_money * 52
print("Your gross pay this week is", str(weekly_money), "dollars")
print("Your estimated annual gross pay will be", str(annual_gross_pay), "dollars")