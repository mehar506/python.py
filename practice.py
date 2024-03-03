#uses of python (1991 realesed) web dev(server side) + software dev+mathematics+system scripting
#can be used to handle big data and performs complex mathematics
#it can connect database as well and can also read and modify it 
# it can also be used for rapid prototyping and production ready softwares
#Why Python?
#Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
#Python has a simple syntax similar to the English language.
#Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
#Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
#Python can be treated in a procedural way, an object-oriented way or a functional way.


# staring on 31/1/23 using w3schools.com
#The Python print() function is often used to output variables.
#print("hello world") >hello world
# indentation=Indentation refers to the spaces at the beginning of a code line.
'''
import random
if 4<5:
 print("the statement is true and im being treated as a block")
if 4<5:
    print("this also true condtion")
    print("this is also in 2nd if block but the spaces b/w both the statments should equla otherwise error")
number=23
name="mehar ali shah"
print(number)
print(name)'''
#this is syntax for multiline comments '''  '''


#python variables=Variables are containers for storing data values.

'''x=3
y="jhon" this is equal to y='jhon'
print(x)#>3
print(y)
x="ali" 
print(x)#>ali
'''
"""a=str(4)
A="mehar"
b=int(4)
c=float(4)
print(a)#4
print(A)# mehar
print(type(a))#str
print(type(b))#int
print(type(c))#float

Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


assigning multiple values



x,y,z="orange",32,'a'
 #assinging same value to mutlple varable
a=b=c="mehar"
print(x)
print(y)
print(z)
print(a)
print(b)
print(c)


x="mehar"
y=58
#print(x + y) this will give and error instead use (x,y)
print(x,y)

#global variable =Variables that are created outside of a function (as in all of the examples above) are known as global variables
x="mehar ali shah" # this is a global variable
def myfun():
    x="ali shah"# this is a local variable
    print("my name is "+x)

myfun()    # my name is ali shah
print("my name is "+ x)# output = my name is mehar ali shah

#the global key word =If you use the global keyword, the variable belongs to the global scope:
def myf():
    global a
    a="mehar shah"

myf()

#if not using global key word the scope of variable a will not be down there
print("my name is " +a+"  it is now global")


  

  # other demonstration
x="mehar"
def myfuntion():
    global x
    x="global name "
myfuntion()
print("my name is "+x)    #output will be the value of the global 

"""


#python data types 
"""Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType 

you can use the type() funtion to know the data types of variables


python does not have character datatype
Example	Data Type	Try it
x = "Hello World"    =	str	
x = 20           = int	
x = 20.5	    =float	
x = 1j      =	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	                   range	
x = {"name" : "John", "age" : 36}	 dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	                       bool	
x = b"Hello"                    	bytes	
x = bytearray(5)	           bytearray	
x = memoryview(bytes(5))	  memoryview	
x = None	                 NoneType	


Type Conversion
You can convert from one type to another with the int(), float(), and complex() methods:



this is type casting


x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0
print(random.randrange(20,30))
"""
#python strings='hello' is the same as "hello". strings are arrays 
#multiline strings
#a="""this is the value of your time """
"""
print(a[0])#t
counter="e"
numer=0
for x in a:
    print(x)
    if(x==counter):
        numer=numer+1
print(numer)
print(len(a))# the len() funtions return the value of total characters or length of the string
#checking a word or character in a string using in keyword
print("is " in a)# this returns true or the false value if word or the letter present in the string returns true otherwise false
print("mehar " not in a)# this also return true bcz mehar is not present in the sting
if " mehar " not in a:
    print ("mehar word is not present in the string a "
  


#sliceing the strings=You can return a range of characters by using the slice syntax.
b="mehar ali shah"
print(b[6:9])# ali [starting index :ending index]
print(b[6:])# from index 6 to all at end



  # Modify string
  #upper() = returns the uppercase
a="   Meahr Ali Shah"
print(a.upper())
print(a.lower())
print(a.strip())# removes whitespaces from beg and end
print(a.replace("Ali","hyd"))
print(a.split(" A"))#A will be removed and the string will be splited into two parts




  #string methods
a="mehar"
b=" ali"
c=" shah"
print(a+b+c)
#But we can combine strings and numbers by using the format() method!
number=58
name="mehar ali "
s="my roll number is {} and my name is {} "# the {}< show the argument given to foramt method it can take multiple arguments

print(s.format(number, name))# my roll number is 58 and my name is mehar ali

#using escape character for those words which simply can not be written in the string normally
txt = "We are the so-called \"Vikings\" from the north."



 this is the list of the methods used in the python
  

  Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning



  #boolean
a=12
b=45
if a<b:
    print("a is less than b")
else :
    print("a is greater than b ")
print(bool(a))# all nuber true except 0 all strings true except empty

print(bool(b))

in following conditions the bool funtion returns false
In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.


 funtions can also return boolean valuse
 
 
 
 
def f():
    return True
if f():
    print("yes!")
else:
    print("no!")    



x="mehar"
print(isinstance(x,int))# this returns false coz the x is not int type 
def sum(a , b):
    return a+b
print (sum(23,45))
def game(a):
    if a=="a":
        print("you won")
    else :
         print("you loss")
print(game("a"))
a=["mehar","ali","shah"]
for x in a:
    print(x)
    


    #operator in python=Operators are used to perform operations on variables and values.
   # Python divides the operators in the following groups:

#Arithmetic operators
#Assignment operators
#Comparison operators
#Logical operators
#Identity operators
#Membership operators
#Bitwise operator
a=10
b=2

#arthematic operators
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)#this is floar division answer will be in int form





Operator	Example	Same As	Try it
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3





comparision operator
Operator	Name	Example	Try it
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y



identity operators
is 	Returns True if both variables are the same object	x is y	
is not	Returns True if both variables are not the same object



membership operator

Operator	Description	Example	Try it
in 	Returns True if a sequence with the specified value is present in the object	x in y	
not in	Returns True if a sequence with the specified value is not present in the object





#list in python=Lists are used to store multiple items in a single variable. it allows duplicate values

rollnumber=[52,55,58,59,63,"hi", False]
for x in rollnumber:
    print(x)
print("the roll number of mehar ali is  " ,rollnumber[2])
print(len(rollnumber))# number of items in the list 

print(type(rollnumber))#list
#using list constructer
varialz=list(("mehar",58,"ali",86))
print(varialz)
for x in varialz:
    print(x)



Python Collections (Arrays)


List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members

There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.


l=[2,34,6,4,4,7,4,3,6,6]
l1=["ali ", "meer", "shah"]
l[1]=23 # we can modifiy list now the value if item at index 1 will be 23

print(l)
print(l[-1])# this gives the last item in the list 

print(l[2:5])# index 2 to 5 index items will be printed
print(l[4:])# from index 4 to end
print(l[:4]) # till the four index but not fourth item itself
if 3 in l:
    print("your number is present")
l[2:4]=["mehar", "shah"]# now these values will be at the indexe from 2=mehar 3=shah as 4 is not included
print(l)
l[1:3]=[40]
print(l)
# using insert() method to insert values in the list
l.insert(2,"second_item")# insert(ind_no, value) this will not update the second item but sit at its index and second item bcmz 3
print(l)
#using append() to add items at end
l.append("meharali")

print(l)
# use extend() to append other list to the current list
l.extend(l1)
print(l)
#removing list item
l.remove("meharali")
print(l)
# use pop() to remove item from the specified index
l.pop(2)# if only l.pop() this removes last item
print(l)

# del keyword to remove item from the specified index
del l[4]# del l[] this will delete complete whole list
print(l)
# clear() to clear the list and list bcmz empty
l1.clear()
print(l1)
print(l)
#for x in l:
 #   print(x)
#use range() and len() to loop through list using index
#for i in range(len(l)):
 #   print(l[i])

# using while loop
i=0
while i<len(l):
    print(l[i])
    i=i+1
#another way
[print(x) for x in l]

l=[2,34,6,4,64,7,4,3,6,6]
l2=["meahr","ali","zubair","kashif"]
# sorting the list 
l.sort()
l2.sort()
print(l)
print(l2)
l.sort(reverse=True)# this sorts the list in the reverse order

print(l)

# custoomizing sort function
def myf(n):
    return abs(n-50)#Sort the list based on how close the number is to 50:
l.sort(key=myf)
print(l)
l2.sort(key=str.lower)# chech the case_insensitvity
print(l2)
l2.reverse()# this will reverse the list order ie frist item from z

print(l2)
# making the copy of the list using copy() method
l3=l2.copy()
print(l3)
# other way to copy a list
l4=list(l3)
print(l4)
# joing two list
l5=l+l2
print(l5)
# other way
for i in l:
    l3.append(i)
print(l3)

List Methods
Python has a set of built-in methods that you can use on lists.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list


mytuple=("apple","orage","banaa","mango",434)
t=("coffe",)
e=("tea")
print(type(t))#tuple
print(type(e))# str
print(len(mytuple))#4
print(type(mytuple))# tuple
print(mytuple[0])#first item
print(mytuple[-1])# last item 
print(mytuple[1:3])# retruns 2nd third elements last index npot includes
if "banaa" in mytuple:
    print("yes availible")
# updating tuple after converting it into list 
t=(3,5,2,5)
l=list(t)
l[0]=55
t=tuple(l)
print(t)
#adding elements using append method of list after converting the tuple into list then list int tuple
l=list(t)
l.append(44)
t=tuple(l)
print(t)
#adding tow tuples
t1=(11,22)
t+=t1
print(t)
#removing elements using same concept of the list conversion
l=list(t)
l.remove(44)
t=tuple(l)
print(t)
#deleting a tuple using del keyword
del t1
 # print(t1) this will show an error bcz the tuple do not exist anymore
print(t)
# unpacking the tupple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


  
  #If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


# looping through tuple
for x in t:
    print(x)

#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found


# stes in python
myset={2,4,5,6}
print(myset)

for x in myset:
    print(x)


#using set() constructor
thisset=set((3,5,7))
print(thisset)
thisset.add(55)# adds 55 at the end 
set1={11,22}
thisset.update(set1) # update(can be any iterable ie list tuple dictionary etc)
print(thisset)

thisset.remove(22) # or discard(22) if 22 doest't exist this will not raise an error but remove method will do

print(thisset)
 
 # pop() removes a random item
s1={"saddar","zohaib","mehar", "ali"}
s1.pop()
print(s1)
# clear() empties the set
s1.clear() # this list exist but the elements are cleared
print(s1) 
del s1# this deletes the set
# union() like update() can be used to add tow sets
# intersection_update() retrun only the duplicate values from two sets

x={4,3,6}
y={4,2,7}
x.intersection_update(y)
print(x)# 4 output
# symmetric_difference_update()= keeps all items except duplicates
a={2,53,45}
b={45,2,6}
a.symmetric_difference_update(b)
print(a)#{53, 6}output


Set Methods
Python has a set of built-in methods that you can use on sets.

Method	Description
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()


# python dictionaries =Dictionaries are used to store data values in key:value pairs.
thisdic={
    "brand":"Ford",
    "model":"mustang",
    "year":1964,
    "year":2020
}
print(thisdic)
print(thisdic["brand"])# ford
print(thisdic["year"])# duplicate valuse will be overriden output=2020
print(len(thisdic))# output=3
print(type(thisdic))# dict
# constructor of dict
thisd=dict(name="mehar", age=20, caste="syed", dpt="software")
 # accessing the dict data
x=thisd.get("name")
print(x)
print(thisd["age"])
k=thisd.keys()
print(k)# prints all
thisd["name"]="mehar ali shah"
print(thisd["name"])# mehar ali shah = output
v=thisd.values()
print(v)# this will retrun all the values assigend to keys ie 20 mehar syed etc
# adding new values to dict
thisd["gender"]="male"
print(thisd)
x=thisd.items()# The items() method will return each item in a dictionary, as tuples in a list
print(x)
# removing item from the dict
thisd.pop("age")
print(thisd)
# popitem() removes random item from the dict
# del keyword is used to delete the item with specified key
# clear() empties the dict


# looping through the dict keys
for e in thisd:
    print(e)# keys
    print(thisd[e])# values
# coping dictionary
newdict=thisd.copy()
print(newdict)

#Create three dictionaries, then create one dictionary that will contain the other three dictionaries:



child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

a=209
b=29
if a<b:
  print("b is greater than a")
elif a>b:
  print("a is greater than b")

else:
  print("a==b")


a=10322
c=232342
b=1000
 #if a>b:print("a is greater than b") this is a short hand of if condition 
print("A") if a>b else print("B")# shorthand of if else condition ternary teqniq
print("A") if a>b else print("=") if a==b else print("B")
if a>b and b>c:
  print("a is greatest ")
elif a<b and b<c:
  print("c is greatest")

else:
  print("b is greatest")
if a>b or b<c:
  print("atleast one condition is true so i executed")
if not a>b:
  print("condition reversed by the Not operator")
x=14
if x>10:
  print(" X is greater than 10")
  if x>20:
    print("X is also greater than 20")
  else :
    print(" x is less than 20 i geust hence i executed")

if a>b:
  pass # this is used when u do not want to write anythin in the if block and also ignoring the error 

i=1
while i<=10:
  print(i)
  
  if i==5:
    break # if continue than only five will be excluded from the iteration
  i+=1

a=1
while a<=5:
  print(a)
  a+=1

else :
  print("the condition of while is no more ture")

fruits=["mango", "banan","orange","apple","quauas"]
for x in fruits:

  print(x)
  if x=="apple":
    break
# or 
for a in "sweets":# this string will be broken down into the letters and will be printed these letters
  print(a)
  if a=='e':
    continue

for b in range(6):
  print(b)
for c in range(2,30,3):# range(start, end, increment)
  print(c)
else:
  print("finally the range method ended")



#nested loops
vegetables=["allu", "gobi","bengan","piaz"]
season=["all","winter","winter","midlle"]
for v in vegetables:
  for s in season:
    print(v,s)
    


# funtions in python
def myfuntion():# creating funtion
  print("this is a funtion")
# calling funtion
myfuntion()
def argumentalfun(name):
  print("hello sir my name is " +name)
argumentalfun("mehar")
argumentalfun("ali")
def multiargumentalfun(name, age, job):
  print("my name is " +name)
  print("my age " ,age) # only string can be concatenated using + sign
  print("i am a " + job)
multiargumentalfun("mehar",20,"software engineer")
 # if the number of argument are unknow u can use * sign and a name for agruments to be passed 
def arbitorayargument(*names):
  print("the last one is  "+names[5])
arbitorayargument("mehar ","ali","zohaib", "muzafar", "zulfi","unkkonw")
# keyword arguments
def myf(c1, c2,c3):
  print("the youngest child is " +c3)
myf(c1="ali ", c2="parveez",c3="zameer")
# default parameter value
def myff(country="pakistan"):
  print("the names of countries  " + country)
myff("india")
myff("china")
myff("iran")
myff()# this will give pakistan
# passing a list as an agrument in the funtion
def listf(food):
  for i in food:
    print(i)
fds=["apple", "banana","oragne"]
listf(fds)
# return values in funtion
def myfun(x):
  return 2*x
print(myfun(10))

# recursion of function= funtion calls it
def tri_ursion(k):
  if(k > 0):
    result = k + tri_ursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_ursion(6)



#A lambda function is a small anonymous function.

#A lambda function can take any number of arguments, but can only have one expression.
    # syntax   lambda arguments : expression
x=lambda a:a+10
print(x(5))# 15
a=lambda x,y:x*y
print(a(5,7))#35
name=lambda fistname: fistname+"shah  "
print(name("mehar"))# mehar shah
age=lambda a:a+10
print(age(10))# 20
#The power of lambda is better shown when you use them as an anonymous function inside another function.
def myf(b):
  return lambda a: a*b
x=myf(4)
print(x(4))# returns 16




Python Classes/Objects
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.



The __init__() Function
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are nec



class myclass:
   x=10
object_class=myclass()
print(object_class.x)
object_class=myclass()# 10 will be printed
class person:
  #Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class. we can right it what so ever we want but it should be first parameter
  def __init__(self , name, age):# _init_ class is executed first 
    self.name=name
    self.age=age
p1=person("mehar",20)
print(p1.age)
print(p1.name)
class uni:
  def __init__(self, name, type , openyear,):
    self.name=name
    self.type=type
    self.openyear=openyear
muet=uni("meharn", "engineering university",1969)
print(muet.name)
print(muet.openyear)
print(muet.type)

    

class human:
  def __init__(self):
    print("humans are to distinguish from this earthe")
h=human()
print(h)   

class birds:
  def __init__(self, name , color):
    self.name=name
    self.color=color
  def myfunc(self):
    print("the name of the birsd is "+self.name+" and the cloro of the birds is "+self.color)
b1=birds("parrot","green")
b1.myfunc()
# u can modify the object properties
b1.name="greenbird"
b1.myfunc()
# use del key word to delete objects propeerties
del b1.color
b1.myfunc()

 
 #python inheritance
Inheritance allows us to define a class that inherits all the methods
 and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class person:
  def __init__(self, fname, lname):
    self.fn=fname
    self.ln=lname
  def myf(self):
    print(self.fn, self.ln)
obj1=person("mehar","Ali")
obj1.myf()
# creating a child class for person class
class student(person):
  pass# Note: Use the pass keyword when you do not want to add any other properties or methods to the class.
student1=student("mehar ali", "shah")
student1.myf()# mehar ali shah
#adding __init__ function rather than pass keyword
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()
#Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()





Python Iterators:
An iterator is an object that contains a countable number of values

Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().



"""