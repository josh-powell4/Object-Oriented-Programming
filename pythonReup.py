my_name = "Josh Powell"
print("Welcome to the course, " + my_name + "!")

'''This is a reup/training of Python --- Course material from Stack Skills
--- Python for Everyone '''

#COMMENTS
# This variable will be used to count the number of words written in ALL CAPS
#all_caps_count = 0
# This code will calculate the odds of your team winning the championship
#calculate_odd_of_winning_championship()
# the code below will not run
# all_lowercase_count = 0

#The code Here will be written our in this sandbox, placed in notepad++, 
#and finally saved for upload to github.

#What if you want your comments to be on multiple lines?
''' This is the beginning 
of a multi-line comment.
Notice that none of this code will run '''
##And also
""" This is the beginning 
of a multi-line comment.
Notice that none of this code will run """

#But mixing single and double quotes doesn't work
#""" This is the beginning 
##Notice that none of this code will run '''

''' This is a test of multilines
Convert these lines'''

##PRINT Function
#From the Giving tree
print("Come, Boy, sit down. Sit down and rest. And the boy did. And the tree was happy.")
###Challenge
#Print Hello World
print("Hello world!")

#Print Multiple Lines
##If you print it like ths...
'''print("Come, Boy, sit down. Sit down and rest. 
And the boy did. 
And the tree was happy.")'''
##An error will occur so do this:

print("""Come, Boy, sit down. Sit down and rest. 
And the boy did. 
And the tree was happy.""")

###Challenge
print("""Two roads diverged in a wood, and I—
I took the one less traveled by, 
And that has made all the difference.""")

#Datatypes

##Strings + Challenge
# Print your favorite color using the print() command.

# If your print statement uses double-quotes ", change them to single-quotes '. 
# If it uses single-quotes ', change them to double-quotes ".
print('blue')
print("purple")
print("""blue, 
purple, 
gold, 
green""")

##Strings w/ Quotes + Challenge
'''What happens if we have the following text that we want to convert to a string:

"Sarah said, "I would not do that if I were you."

If we surround our text with double quotes as in the following we will get a syntax error:'''
# - print("Sarah said, "I would not do that if I were you."")

##Solution
# - print('Sarah said, "I would not do that if I were you."')

''' The opposite is true as well. The following is invalid syntax because the inner and outer quotes match:

print('I'm excited to see you!') '''
##Solution
# - print("I'm excited to see you!")

###Challenge
##print("Arthur said, "The power you seek is within you."")
###Solution
print('Author said, "The power you seek is within you."')
##print('What's the weather going to be like today?')
###Solution
print("What's the weather going to be like today?")

#Variables w/ Challenge
#Example
name = "Rob"
print(name)
"""This code provides a variable called name and we have used the = assignment operator to assign the variable a value of the string "Rob"

Ok, but what can we now do with this superpower? Let's find out!

The following code: 

name = "Rob"
print(name)
Will result in: 

Rob
Did you notice that in the print() function you didn't pass in a string "Rob". Instead you passed in a variable name that contained the value of the string "Rob"."""

name2 = "Josh the Almighty Joey in the Army"
print(name2)

'''"There are only two hard things in Computer Science: cache invalidation and naming things."

-- Phil Karlton'''

##Variable Naming Rules
'''Variable names can contain only letters, numbers, and underscores. They can start with a letter or an underscore but not a number. For instance, you can call a person_1 but not 1_person.
Spaces are not allowed in variable names, but underscores can be used to separate words in variable names. For example, welcome_message works, but welcome message will cause errors.
Avoid using Python keywords and function names; that is, do not use words that Python has reserved for a particular programmatic purpose, such as the word print. Here are a few other examples:
Variables names should be short but descriptive. For example, apple is better than a, apples_on_tree is better than a_o_t, and apple_count is better than count_of_apples.
Be careful when using lowercase letter l and uppercase letter O because they could be confused with the numbers 1 and 0.'''

#Challenge
# fix the following invalid or not best practice variable names

# fix invalid variable name
#1_place = "Sam"
#print(1_place)
## Solution
place_1 = "Sam"
print(place_1)

# fix invalid variable name
#my motto = "If you aren't first you're last"
#print (my motto)
## Solution
my_Motto = "If you aren't first you're last"
print("my_Motto")

# choose variable name to describe number of widgets sold
x = 256
print(x)

# choose variable name that is more succinct
did_i_eat_vegetables_yesterday = False
print(did_i_eat_vegetables_yesterday)


#ERRORS
''' This code has an error: '''
#print("This is going to output an error. Do you know why?')
''' As you can see it's the ) in the code.'''

###There are two common errors you will encounter while writing Python: SyntaxError and NameError

"""SyntaxError

In this case we are being told that we have a SyntaxError: EOL while scanning string literal

With the ^ character pointing to the closing ) and the message SyntaxError: EOL while scanning string literal can you figure out what the problem is?

The error is that the string we are trying to print isn't surrounded by matching single or double quotes. We have an opening ' and a closing ". Because we are never appropriately closing the string we are getting a SyntaxError. If we change the opening single or double quote to match the closing single or double quote then our SyntaxError will be fixed."""

##NameError's occur when you haven't been precise with your names and Python runs into a word it doesn't recognize.
###Example
'''
greeting = "Hello Python!"
print(greting)
'''

# Challenge
'''You might encounter a SyntaxError if you open a string with double quotes and end it with a single quote. Update the string so that it starts and ends with the same punctuation.
You might encounter a NameError if you try to print a single word string but fail to put any quotes around it. 
Python expects the word of your string to be defined elsewhere but can't find where it's defined. Add quotes to either side of the string to squash this bug.
Update the malformed strings in the workspace to all be strings.'''

# Fix SyntaxError
##weather = "The weather today is cloudy'
###Solution
weather = "The weather today is cloudy"
print(weather)

# Fix NamingError 
##print(Hi)
### Solution
Hi = "Hello"
print(Hi)


#Numbers
'''
Integers

An int is a whole number such as 1, 2, 3 or 4. As well, as their negative values and including the number 0. You might use integers to count the number of guests coming for dinner or how many cups you have on the dinner table.

You can add (+), subtract (-), multiply (*), and divide (/) integers in Python.
'''
print(2 + 3)
# outputs 5

print(3 - 2)
# outputs 1

print(2 * 3)
# outputs 6

print(3 / 2)
# outputs 1.5

'''
Floats

Python calls any number with a decimal point a float. This term is used in most programming languages, and it refers to the fact that a decimal point can appear at any position in a number. Every programming language must be carefully designed to properly manage decimal numbers so numbers behave appropriately no matter where the decimal point appears.

'''
# Adding two floats
print(0.2 + 0.3)
# outputs .5

# Multiplying an integer by a float
print(3 * 0.2)
# outputs 0.6

# Dividing an integer by a float
5 / 2.5
# outputs 2

## Challenge
'''1.  Let's pretend that you are a fan of baseball and your favorite player is a pitcher. 
Let's use integers to to track your favorite pitchers strikeouts for a specific year. Go ahead and create a variable baseball_season and provide an integer for a specific year. After that create a variable, strikeouts, and record an integer for strikeouts in a year. '''
# Define the baseball_season and strikeouts integer variables below:
baseball_season = 2022
strikeouts = 240


'''2. Now, let's capture your favorite pitchers ERA (Earned Run Average). 
This is the average amount of runs a pitcher allows over nine-innings and is almost always going to involve decimal points. Create the variable earned_run_average and assign it a float between 0.01 and 9.99'''
# Define the earned_run_average float variable below: 
earned_run_avg = 3.04


#String Concatenation & Number Concatenation
''' 
When we add two strings together we call this string concatenation.

The best way to describe it is when you take two separate strings – stored by the interpreter – and merge them (without any added space in-between) so that they become one.

For instance, one string would be “hello” and the other would be “ python”. When you use concatenation to combine them it becomes one string, or “hello python”.
'''
strng_1 = "Josh"
strng_2 = "Powell"
print(strng_1 + " " +  strng_2)
string_3 = 2
string_4 = 3
numbers = string_3 + string_4
print(numbers)

# space before the p
print("hello" + " python")

# space after the o
print("hello " + "python")

# concatenate a string with a space
print("hello" + " " + "python")


## Challenge 1
string1 = "It was the best of times, "
string2 = "it was the worst of times, "
string3 = "it was the age of wisdom, "
string4 = "it was the age of foolishness, "
string5 = "it was the epoch of belief, "
string6 = "it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way - in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only."

# Define paragraph below:
paragraph = string1 + string2 + string3 + string4 + string5 + string6

#print(paragraph)
print(paragraph)

'''
What if we want to concatenate a number with a string?
Ex:
lucky_number = 7
message = "My lucky number is "
period = "."
print(message + lucky_number + period)

We are going to get a TypeError: must be str, not int. This is our first TypeError
''' 
##str() function
'''
When you use integers within strings like this, you need to specify explicitly that you want Python to use the integer as a string of characters. 
You can do this by wrapping the variable in the str() function, which tells Python to represent non-string values as strings.
'''
#So to fix this... The best way to go about it is by

"""
lucky_number = 7
message = "My lucky number is "
print(message + str(lucky_number))

# Prints "My lucky number is 7."

or...

guests = 5
start_message = "There are"
end_message = "guests coming to dinner."
print(start_message, guests, end_message)

# Prints "There are 5 guests coming to dinner."
"""

### Challenge 2
message_start = "A marathon is "
message_finish = " miles."
marathon_distance = 26.2

# Print a string that says:
# "A marathon is 26.2 miles."
print(message_start + str(marathon_distance) + message_finish)


#Multiply Equals 

##If we have a number saved to a variable and we want to multiply the current value of the variable you can use the *= (multiply-equals) operator.
# First we have a variable with a number saved for earnings in a month
earnings = 2000

# Then we need to update that variable
# Let's say we want to find the salary for the year
earnings *= 12

# The new value is the old value
# Multiplied by the number after the multiply-equals
print(earnings)
# Prints 24000

### multiply-equals operator can also be used for strings as well:
laughter = "ha"
laughter *= 4
print(laughter)
# Prints hahahaha

### Challenge
# Take the initial income you earn per hour and multiply 
# that by the hours you worked that day and print the results.

# Income earned per hour
income = 10

# Hours worked today
hours_worked_today = 5

# Find income earned today
income *= 5
# Print todays income
print(income)


#IMPORT MATH
import math
dollars = 82.12
whole_dollar = math.floor(dollars)
print(whole_dollar)
# Prints 82 

# importing math to give us access to the floor() method
import math

# floating point value that we want to round down
dollars = 82.12

# assign to whole_dollar the value of dollars passed to the math.round() function
whole_dollar = math.floor(dollars)

print(whole_dollar)
# Prints 82 

### Challenge
# import in the math library
import math

# This is the amount of money you have in your piggy bank
money_in_piggy_bank = 84.70

# Print the value of money in your piggy bank rounded to the nearest integer
print(math.ceil(money_in_piggy_bank))
