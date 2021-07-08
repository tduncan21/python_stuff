def get_user_input():
    total_bill = float(input("What was the total bill? $"))
    tip_percentage = float(input("What percentage tip would you like to give? "))
    num_people = int(input("How many people to split the bill? "))
    calculate_tip(total_bill, tip_percentage, num_people)


def calculate_tip(total_bill, tip_percentage, num_people):
    converted_percentage = (tip_percentage * 0.01) + 1
    final_total_per_person = round(((total_bill / num_people) * converted_percentage), 2)
    print_output(final_total_per_person)


def print_output(final_total_per_person):
    print("Each person should pay: ${:.2f}".format(final_total_per_person))


print("Welcome to the tip calculator!")
get_user_input()



#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
