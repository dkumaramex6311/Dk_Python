
#Python Version
import sys
print(sys.version)

#Zen of Python
import this

#Why Python?
import antigravity


#list is mutable and hence you can change any element you want
L = [0,2,3]
L[0] = 1
print L


#string is not immutable
s = 'string'
s[0] = 'o' #throws error


# Python creates real copies only if it has to, i.e. if the user, the programmer, explicitly demands it
x=[1,2,4]
print "x",id(x)
y=x
print "y",id(y)
import copy
z = copy.copy(x)
print "z",id(z) 


# If you assign one mutable object to another and then change/edit a value in the first object, the same will be reflected in the second object
x = [1,2,4]
y = x #This just points to the same object i.e. x
print "x", x, id(x), "y", y, id(y) #Ids are same and so are values
x[0] = 0
print "x", x, id(x), "y", y, id(y) #changing a value in x, changes it in y too. Ids are same


# That is not the case with immutable objects because you cannot edit them, just change the value entirely. There are work arounds to copy a mutable object into another without facing the issue discussed above. One such way is as below :
x = [1,2,4]
y = x[:] #Now this won't point to the same object
print "x", x, id(x), "y", y, id(y) #Ids are same and so are values
x[0] = 0
print "x", x, id(x), "y", y, id(y) #changing a value in x, changes it in y too. Ids are same


# Single line comments start with a number symbol.



""" Multiline strings can be written
    using three "s, and are often used
    as comments
"""



# You have numbers
3  


# Math is what you would expect
1 + 1 


8 - 1 


10 * 2 


35 / 5 


# Division is a bit tricky. It is integer division and floors the results automatically. What do you think this will give?


#Think what this will give
34 / 5


# In Python 2.x the divison operater gives integer values, in Python 3.x, it gives the correct Float/Real value



# To fix division we need to learn about floats.
2.0  # This is a float




34.0 / 5.0  #yayy we fixed it


# Ahhh...much better. So if you want to force a float division, multiply the terms with 1.0. This comes especially handy while calculating percentages like this -



#Multiplying by a float number, leads to a float output
45*100*1.0/70
#or you can do 45.0*100/70




# Modulo operation
20 % 15 




100%100




# Exponentiation (x to the yth power)
2 ** 4  




3**2




# Enforce precedence with parentheses
(1 + 3) * 2  # => 8


# In Python, Boolean values are the two constant objects - False and True



# Boolean Operators
# Note "and" and "or" are case-sensitive
True and False 




False or True  # => True


# You can use Bool operators with integers too



#Any 0 value is "False". Everything else is "True"
0 and 2 




-5 or 0 




0 == False




2 == True




1 == True




# negate with "not"
not True




not False




# Equality is ==
print "1 == 1 is", 1 == 1
print "2 == 1 is", 2 == 1


# print is a function in Python 3.x. Functionality is little different, but in most case all you have to do is to put everything after "print" in parentheses like this - print("1 == 1 is", 1 == 1)


# Inequality is !=
print 1 != 1  
print 2 != 1 




# Some more comparisons
print 1 < 10 
print 1 > 10  
print 2 <= 2 
print 2 >= 2  




# Comparisons can be chained!
print 1 < 2 < 3  
print 2 < 3 < 2  




# Strings are created with " or '
print "This is a string."
print 'This is also a string.'




#you can also save strings in a variable
a = "Hello"
b = "World!"
print a
print b




# Strings can be added too!
print "Hello " + "world!"  
# Strings can be added without using '+'
print "Hello " "world!" 




# ... or multiplied
print "Hello" * 3




# A string can be treated like a list of characters
print "This is a string"[0]  
print "This is a string"[1]  
print "This is a string"[-1] 
print "This is a string"[-2] 




# You can find the length of a string
len("This is a string")




# None is an object
print None  


# Like in SQL you have "NULL" and "NA" in R, in python a missing element is denoted by None. To compare something with "None", you need to use "is", not "=="



# Don't use the equality "==" symbol to compare objects to None
# Use "is" instead
print "etc" is None 
print None is None  



# No need to declare variables before assigning to them.
some_var = 5  
print some_var  


# Unlike some low-level languages like C and Java, there is no need to declare the type of variable in Python.
# All you have to do is define a variable and assign a value to it. 
# Python will automatically read what kind of variable it is - be it string or integer or float or any other data types that we will discuss below. Examples are as below :



my_float = 2.35; print my_float
my_string = "Hi there!"; print my_string



# Lists are equivalent to arrays in most other programming languages and are used to store sequences




# Lists store sequences
li = []
# You can start with a prefilled list
other_li = [4, 5, 6]
print li, other_li




#A list can contain anything e.g numbers along with strings etc
my_list = [1, "a", "Python", 1.25]
print my_list




# Add stuff to the end of a list with append
li.append(1) 
li.append(2) 
li.append(4)  
li.append(3)  
print li




# Remove from the end with pop
li.pop()  
print li



# Let's put it back
li.append(3)  
print li




# Access a list like you would any array
print li[0]  
print li[1]


# As I said, numbering in Python starts from 0, NOT 1



# Assign new values to indexes that have already been initialized with =
li[0] = 42
print li
li[0] = 1  # Note: setting it back to the original value
print li




# Look at the last element
li[-1]  # => 3




# Looking out of bounds is an IndexError
li[4]  # Raises an IndexError




# You can look at ranges with slice syntax.
# (It's a closed/open range for you mathy types.)
li[1:3]  





print "li[2:] is ", li[2:]  # => [4, 3]
# Omit the end
print "li[:3] is ",li[:3]  # => [1, 2, 4]
# Select every second entry
print "li[::2] is ",li[::2]  # =>[1, 4]
# Reverse a copy of the list
print "li[::-1] is ",li[::-1]  # => [3, 4, 2, 1]
# Use any combination of these to make advanced slices
# li[start:end:step]


# We encourage you to play around with different combinations of a,b, and c(i.e. start, end, and step) to get comfortable with the notation. They also work the same with strings. for example :



print "Hello World! [2:] is => ", "Hello World!"[2:] 
# Omit the end
print "Hello World![:3] is => ","Hello World!"[:3]  
# Select every second entry
print "Hello World![::2] is => ","Hello World!"[::2] 
# Reverse a copy of the list
print "Hello World![::-1] is => ","Hello World!"[::-1] 




# Remove arbitrary elements from a list with "del", i.e. with location
del li[2]  
print li




# You can add lists
li + other_li



# Concatenate lists with "extend()"
li.extend(other_li) # Now li is [1, 2, 3, 4, 5, 6]
print li
# Note: values for li and for other_li are not modified.




# Remove first occurrence of a value
li.remove(2)  # li is now [1, 3, 4, 5, 6]
print li
li.remove(2)  # Raises a ValueError as 2 is not in the list
print li




# Insert an element at a specific index
li.insert(1, 2)  # li is now [1, 2, 3, 4, 5, 6] again
print li




# Get the index of the first item found
print li.index(2)  # give 1 and not 2, why? because numbering starts from 0
print li.index(7)  # Raises a ValueError as 7 is not in the list




# Check for existence in a list with "in"
print 1 in li 
print 8 in li 



# Examine the length with "len()"
len(li)




#matrix can be thought of list of lists i.e. each row as list and then list of rows
my_matrix = [[1,2,3],[4,5,6]] #2x3 matrix


# A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.



# Tuples are like lists but are immutable.
tup = (1, 2, 3)
print tup[0]  
tup[0] = 3  # Raises a TypeError




# You can do all those list thingies on tuples too
print len(tup)  # => 3
print tup + (4, 5, 6)  # => (1, 2, 3, 4, 5, 6)
print tup[:2]  # => (1, 2)
print 2 in tup  # => True




# You can unpack tuples (or lists) into variables
a, b, c = (1, 2, 3)  # a is now 1, b is now 2 and c is now 3
d, e, f = 4, 5, 6  # you can leave out the parentheses
print "a =", a
print "Rest values are", b, c, d, e, f




# Tuples are created by default if you leave out the parentheses
g = 4, 5, 6 
print g




# Now look how easy it is to swap two values
e, d = d, e  # d is now 5 and e is now 4


# Python! Its magic!

# A dictionary is an associative array (also known as hashes). Any key of the dictionary is associated (or mapped) to a value. The values of a dictionary can be any Python data type. So dictionaries are unordered key-value-pairs



# Dictionaries store mappings
empty_dict = {}
# Here is a prefilled dictionary
filled_dict = {"one": 1, "two": 2, "three": 3}
print empty_dict
print filled_dict




#Another way
keys = ['david', 'chris', 'stewart']
values = ['504', '637', '921']
D = dict(zip(keys, values))
print D


# You can see that unlike in lists or tuples, the values inside dictionary are not ordered 



# Look up values with []
print filled_dict["one"]  




# Get all keys as a list with "keys()"
filled_dict.keys()  # => ["three", "two", "one"]
# Note - Dictionary key ordering is not guaranteed.
# Your results might not match this exactly.




# Get all values as a list with "values()"
filled_dict.values()  # => [3, 2, 1]
# Note - Same as above regarding key ordering.




# Get all key-value pairs as a list of tuples with "items()"
filled_dict.items()




# Check for existence of keys in a dictionary with "in"
print "one" in filled_dict 
print 1 in filled_dict  




# Looking up a non-existing key is a KeyError
filled_dict["four"]


# Use "get()" method to avoid the KeyError
print filled_dict.get("one")  # => 1
print filled_dict.get("four")  # => None
# The get method supports a default argument when the value is missing
print filled_dict.get("one", "Not Found")  # => 1
print filled_dict.get("four", "Not Found")  # => 4
# note that filled_dict.get("four") is still => None
# (get doesn't set the value in the dictionary)




# set the value of a key with a syntax similar to lists
filled_dict["four"] = 4 
print filled_dict




# "setdefault()" inserts into a dictionary only if the given key isn't present
filled_dict.setdefault("five", 5) # filled_dict["five"] is set to 5
print filled_dict
filled_dict.setdefault("five", 6) # filled_dict["five"] is still 5
print filled_dict


# A Set is an unordered collection data type that is iterable, mutable, and has no duplicate elements



# Sets store ... well sets (which are like lists but can contain no duplicates)
empty_set = set()
print empty_set
# Initialize a "set()" with a bunch of values
some_set = set([1, 2, 2, 3, 4])
print some_set
#The second 2 was ignored



# order is not guaranteed, even though it may sometimes look sorted
another_set = set([4, 3, 2, 2, 1])  # another_set is now set([1, 2, 3, 4])
print another_set




# Since Python 2.7, {} can be used to declare a set
filled_set = {1, 2, 2, 3, 4}  # => {1, 2, 3, 4}

# Add more items to a set
another_set.add(5)
print another_set


# Just like in Maths, you can perform normal set operations on sets in Python. This is not that important for us, just good to know



# Do set intersection with &
other_set = {3, 4, 5, 6}
print another_set & other_set 

# Do set union with |
print another_set | other_set  

# Do set difference with -
print {1, 2, 3, 4} - {2, 3, 5}  

# Do set symmetric difference with ^
print {1, 2, 3, 4} ^ {2, 3, 5}  

# Check if set on the left is a superset of set on the right
print {1, 2} >= {1, 2, 3}  

# Check if set on the left is a subset of set on the right
print {1, 2} <= {1, 2, 3} 




# Check for existence in a set with in
print 2 in filled_set  # => True
print 10 in filled_set  # => False
print 10 not in filled_set # => True




# Check data type of variable
print type(li)   
print type(filled_dict)  
print type(5)  


# You can perform some sensible type conversions easily using int(), str(), float() etc functions



#Converting type of variables
my_int = 1
my_float = 1.25
print "float(my_int) =", float(my_int)
print "str(my_int) =", str(my_int)
print "int(my_float) =", int(my_float)
print "str(my_float) =", str(my_float)



some_var = 5

# Here is an if statement. Indentation is significant in python!
if some_var > 10:
    print "some_var is totally bigger than 10."
elif some_var < 10:  # This elif clause is optional.
    print "some_var is smaller than 10."
else:  # This is optional too.
    print "some_var is indeed 10."




name = "Guido"
if name == "Guido" and 4<2 and 2 in [1,2]:
    print "It worked!"
else:
    print "Whoops!"
    
if name == "Guido" and 4<2 or 2 in [1,2]:
    print "It worked!"
else:
    print "Whoops!"





#for loop examples
#looping using element
a = [1,2,3,4]
for i in a:
    print i
for animal in ["dog", "cat", "mouse"]:
    print animal




#looping with location
for i in range(len(a)):
    print a[i]
for loc in range(len(["dog", "cat", "mouse"])):
    print ["dog", "cat", "mouse"][loc]



#Can be used with strings also
#looping with location
for character in "Hello World!":
    print character




#for loop with if
for i in range(10):
    if i%2==0:
        continue #continue forces the loop to continue with the next iteration
    if i%7==0:
        break #break forces loop to break
    print i




#nested loop to print matrix
my_matrix = [[1, 2, 3],[4, 5, 6]]
print "Printing by value"
for row in my_matrix:
    for col in row:
        print col,
    print "\n" #scope of this print is inside of the first for loop
print "Printing by location"
for row in range(len(my_matrix)):
    for col in range(len(my_matrix[row])):
        print my_matrix[row][col],
    print "\n"


# "range(number)" returns a list of numbers from zero to the given number.<br>
# "range(lower, upper)" returns a list of numbers from the lower number to the upper number minus one.<br>
# This is exactly like what we do with lists li[a:b:c]. Just that instead of colon, we use a comma.
# Here are some examples -



#range is an important function to generate arrays of integers
print range(5)
print range(1,6)
print range(1,6,2)




#while loop example
x = 0
while x < 4:
    print x
    x += 1 #  += is equivalent to x = x+1



# Works on Python 2.6 and up:
try:
    # Use "raise" to raise an error
    raise IndexError("This is an index error")
except IndexError as e:
    pass  # Pass is just a no-op. Usually you would do recovery here.
except (TypeError, NameError):
    pass  # Multiple exceptions can be handled together, if required.
else:  # Optional clause to the try/except block. Must follow all except blocks
    print "All good!"  # Runs only if the code in try raises no exceptions
finally:  # Execute under all circumstances
    print "We can clean up resources here"


# That was little complicated and advanced. For now here is a simple example:



#A simpler example
n = int(raw_input("Please enter a number: ")) #raw_input is used to take input from user
#When it asks, enter "abc"


# raw_input() is input() in Python 3.x



#So it raised an error because you were trying to input a string, while the program was expecting integer
#here is how you fix it
while True:
    try:
        n = raw_input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("No valid integer! Please try again ...")
print "Great, you successfully entered an integer!"



# A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusing.

# Python has some built-in functions that are available  to use without importing any module e.g. len(), raw_input(), int(), str(), range() etc. Few of these you have already used above, here are some more examples :



print "abs(-1) =", abs(-1)




#converts tuples to list
print list({1,2,3})



#returns x to the power of y
print(pow(3,2))



#Add items of an Iterable
print sum([1,2,3,4])




#max of items of an Iterable
print max((1,2,3,4,0))




#Invokes the built-in Help System
help(len)





#List Methods
my_list = [6, 2, 4, 7]
my_list.append(5)
print my_list




my_list.sort()
print my_list




my_list.sort(reverse=True)
print my_list




#dictionary methods
my_dict = {"a":1, "b":2, "c":3}
print "keys =", my_dict.keys()
print "values =", my_dict.values()
print "items =", my_dict.items()




#string methods
my_string = "Hello World!"
#Checks if All Characters are Alphabets
print "my_string.isalpha() =", my_string.isalpha()
print "my_string[:5].isalpha() =", my_string[:5].isalpha()
#converts to lowercase
print "my_string.lower() =", my_string.lower() #try upper()
#	Returns the Highest Index of Substring
print "my_string.find('H') =", my_string.find('H')


# There are multiple pre-built libraries from which you can import functions



#Importing a library
import math
print math.sqrt(16)




#Importing a particular function from a library
from math import sqrt
print sqrt(16) #No need to write math.sqrt



#Importing everything from a library
from math import *
print sqrt(16) #No need to write math.sqrt
print sin(pi/2) #pi is defined inside "math" library




#modules may have sub modules, in which case you can use dot (.)
from sklearn.preprocessing import StandardScaler




#To get help on a fucntion or library you can use help() function
help(math.sqrt)




help(math)




#To get all modules currently installed on your system.takes some time to run, you can uncomment and run
#help("modules")




#A function without any parameters
def bark():
    print "bark! bark!"
bark()




#A function which doesn't return anything
def add(a,b):
    print "a+b is", a+b
#calling the function
add(2,3) #2 and 3 are arguments to parameters a and b



#A function which does return something
def multiply(a,b):
    return a*b
multiply(2,3)




#A function with default parameters
def divide(a=5, b=1):
    return a/b
print "divide() =",divide()
print "divide(10) =",divide(10)
print "divide(10,5) =",divide(10,5)




global_variable = 1 #You can access this anywhere 
def f(x):
    f_local_variable = 2 #You can access this only inside f(x)
    global f_declared_global_variable
    f_declared_global_variable = 3 #You can access this anywhere because we declared it global
    
def g(x):
    print "#####  Inside function  #####"
    g_local_variable = 4 #You can access this only inside g(x)
    global g_declared_global_variable
    g_declared_global_variable = 5 #You can access this anywhere because we declared it global
    try:
        print global_variable
    except NameError:
        print "Error printing global_variable "
    try:
        print f_local_variable
    except NameError:
        print "Error printing f_local_variable "
    try:
        print g_local_variable
    except NameError:
        print "Error printing g_local_variable "
    try:
        print f_declared_global_variable
    except NameError:
        print "Error printing f_declared_global_variable"
    try:
        print g_declared_global_variable
    except NameError:
        print "Error printing g_declared_global_variable"
g(x)

print "#####  Outside function  #####"

try:
    print global_variable
except NameError:
    print "Error printing global_variable "
try:
    print f_local_variable
except NameError:
    print "Error printing f_local_variable "
try:
    print g_local_variable
except NameError:
    print "Error printing g_local_variable "
try:
    print f_declared_global_variable
except NameError:
    print "Error printing f_declared_global_variable"
try:
    print g_declared_global_variable
except NameError:
    print "Error printing g_declared_global_variable"




#An example of recursive function
def factorial(n):
    if n==1: return n
    else: return n*factorial(n-1)
print factorial(5)




#returning multiple outputs
def multiple_outputs(x,y):
    return x+1, y+1
print multiple_outputs(1,2) #returns a tuple




#lambda operator or lambda function is used for creating small, one-time and anonymous function objects in Python
def add(x, y): 
    return x + y
  
# Call the function
print "With defined function ",add(2, 3) 

#Equivalent lambda
add = lambda x, y : x + y 
print "With lambda ",add(2, 3) 




#map functions expects a function object and any number of iterables like list, dictionary, etc. 
#It executes the function_object for each element in the sequence and 
#returns a list of the elements modified by the function object.

def multiply2(x):
  return x * 2
print "With defined function ",map(multiply2, [1, 2, 3, 4]) 

print "With lambda ",map(lambda x : x*2, [1, 2, 3, 4]) 




#list of two dictionaries
dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
print "Example 1:", map(lambda x : x['name'], dict_a)
print "Example 2:", map(lambda x : x['points']*10,  dict_a) 
print "Example 3:", map(lambda x : x['name'] == "python", dict_a)



#We can pass multiple sequences to the map functions
list_a = [1, 2, 3]
list_b = [10, 20, 30]
print map(lambda x, y: x + y, list_a, list_b) 





#filter function expects two arguments, function_object and an iterable. 
#function_object returns a boolean value. 
#function_object is called for each element of the iterable and 
# filter returns only those element for which the function_object returns true
a = [1, 2, 3, 4, 5, 6]
print filter(lambda x : x % 2 == 0, a) 




dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
print filter(lambda x : x['name'] == 'python', dict_a) 





#The function reduce(func, seq) continually applies the function func() to the sequence seq. It returns a single value.
print reduce(lambda x,y: x+y, [47,11,42,13])




#Calculating the sum of the numbers from 1 to 100
print reduce(lambda x, y: x+y, range(1,101))




#Determining the maximum of a list of numerical values by using reduce
reduce(lambda a,b: a if (a > b) else b, [47,11,42,102,13])


# List comprehension is an elegant way to define and create list in Python



#We can use list comprehensions for nice maps and filters
print [pow(i,2) for i in [1, 2, 3, 4]]




#We can use conditionals too
print [pow(i,2) for i in [1, 2, 3, 4] if i%2 == 0]




#if-else is allowed too
print [pow(i,2) if i%2 == 0 else i*10.0 for i in [1, 2, 3, 4]]




# You can construct set and dict comprehensions as well.
print {x for x in 'abcddeef' if x in 'abc'}  
print {x: x ** 2 for x in range(5)}



class Snake:
        pass
snake = Snake()
print snake




class Snake:
    name = "python"
snake = Snake()
print snake.name



class Snake:
    name = "python"
    
    def change_name(self, new_name): # note that the first argument is self
        self.name = new_name # access the class attribute with the self keyword
# instantiate the class
snake = Snake()

# print the current object name 
print "Current Name: ", snake.name

# change the name using the change_name method
snake.change_name("anaconda")
print "Current Name: ", snake.name




class Snake:

    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name
# two variables are instantiated
python = Snake("python")
anaconda = Snake("anaconda")

# print the names of the two variables
print "First name :",python.name
print "Second name :",anaconda.name


# A little advanced example



# We subclass from object to get a class.
class Human(object):
    # A class attribute. It is shared by all instances of this class
    species = "H. sapiens"

    # Basic initializer, this is called when this class is instantiated.
    # Note that the double leading and trailing underscores denote objects
    # or attributes that are used by python but that live in user-controlled
    # namespaces. You should not invent such names on your own.
    def __init__(self, name):
        # Assign the argument to the instance's name attribute
        self.name = name

        # Initialize property
        self.age = 0

    # An instance method. All methods take "self" as the first argument
    def say(self, msg):
        return "{0}: {1}".format(self.name, msg)

    # A class method is shared among all instances
    # They are called with the calling class as the first argument
    @classmethod
    def get_species(cls):
        return cls.species

    # A static method is called without a class or instance reference
    @staticmethod
    def grunt():
        return "*grunt*"

    # A property is just like a getter.
    # It turns the method age() into an read-only attribute
    # of the same name.
    @property
    def age(self):
        return self._age

    # This allows the property to be set
    @age.setter
    def age(self, age):
        self._age = age

    # This allows the property to be deleted
    @age.deleter
    def age(self):
        del self._age




# Instantiate a class
i = Human(name="Ian")
print i.say("hi") 



j = Human("Joel")
print j.say("hello")




# Call our class method
i.get_species()




# Change the shared attribute
Human.species = "H. neanderthalensis"
print i.get_species()  
print j.get_species()  




# Call the static method
Human.grunt() 




print "Before Updating :", i.age  
# Update the property
i.age = 42

# Get the property
print "After Updating :", i.age  




# Delete the property
del i.age
i.age





#Setting the working directory
import os
print "Before changing: ", os.getcwd()

#You can either convert all backword slashes to forward slashes or just use "r" before the path
os.chdir(r"G:\INBLRCB_GDMCOMMON\Python")

print "After changing: ", os.getcwd()




#opening in write mode
test = open("test.txt","w")    # open file in current directory
test2 = open(r"G:\INBLRCB_GDMCOMMON\Python\test2.txt","w")  # specifying full path
#Google for full lists of file opening modes



#method write() writes to the file handle
test.write("This is the first line.\n")
test.write("This is the second line.")



#You must close the file after use of it stays in the memory
test.close()




#read(n) reads all the lines into a string
test = open("test.txt","r") 
print test.read()




#Once the file is read, the cursor moves to the final location and you cannot read anything more
print test.readlines()
test.close()




#readlines() all the lines in a list of lines
test = open("test.txt","r") 
print test.readlines()
test.close()





#Using "with" keyword you don't need to close the files manually
with open("test2.txt","w") as test2:
    for i in range(5):
        test2.write(str(i)+'\n')
with open("test2.txt","r") as test2:
    for line in test2.readlines():
        print(line.strip())


