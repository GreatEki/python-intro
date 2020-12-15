import datetime

# Calculate the mean scores of students in a class

# def mean(theValue):
#     # if type(theValue) == dict:
#     if isinstance(theValue, dict):
#         the_mean = sum(theValue.values()) / len(theValue)
#     else:
#         the_mean = sum(theValue) / len(theValue)

#     return the_mean

# temperatures = [7.7, 6.4, 9.6]
# grades = { "Mary": 6.3, "John": 9.9, "Luke": 8.8}

# print(mean(grades)) 

# Inputs - accepting entries from the use through the console
# def weather_condition(temperature):
#     if temperature > 7:
#         return "Warm"
#     else:
#         return 'Cold'

# userInput = float(input('Enter the Weather Temperature:'))

# print(weather_condition(userInput))


# # Sting Formatting
# def stringFormmatting(theEntry):
#     # message = 'Hello %s' % theEntry
#     message = f'Hello {theEntry}'
#     return message

# userInput = input('Enter your Name: ')
# print(stringFormmatting(userInput))


# Accepting Multiple Entries from  Input
# Formatting strings with more than one  variable
def twoEntries(firstName, lastName):
    # message = 'Your Fullname is %s %s' % (firstName, lastName) 
    when = datetime.datetime.now()
    message = f'Hello {firstName} {lastName}, today is {when}'
    #  We wrapped the variables in a tuple - % (firstName, lastName)
    return message

first_name = input('Enter FirstName:')
last_name = input('Enter LastName:')

print(twoEntries(first_name, last_name))