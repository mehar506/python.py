#print("starting python on 4/10/2023  ")
# this is a comment in python 

''' this is multicommment in python
# getting input from user
name=input("enter ypour name")
print("your name is ",name)
if 3<4:
 print(" this statement is true")
    # print(" are u ok") here it will show syntax error
else:
    print("this statement is not true")
x=3
x=str(3)
print(type(x))
a,b,c= 1,34,5
d=e=f=58
print(a,b, c)  #1 34 5
print(d,e,f) #58 58 58
n1=23
n2=345
print(n1+n2)



#m="mehar" # global variable 
def name():
    m="ali" # local 
    print("hey my name is ",m)
    
name() # hey my name is  ali
print(m)# mehar 


x=range(12)
print(x)
import random
print(random.randrange(1,10))
sentence="this is the name which i will never forgert "

#print(len(sentence))

print("name" in sentence)
#for n in sentence:

print ("mehar " not in sentence) # true
 
 
if "name" in sentence:
    print("yes , 'name' is present") # this is out put 
   # print(n)
a ="hello world "
print(a[2:5])# indexing concept
print(a[:5]) # this will slice the sting from start
print(a[3:])# slice from end 
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
coded=txt.encode()
print(coded)
def fun(n):
    return abs(n-10)
number=int(input("enter the number"))
print(fun(number))'''


class myclass:
    x=6
#print(myclass)
#p1=myclass()
#p2=myclass()
#print(p1.x + p2.x)

class mehar:
    def __init__(self, name , age):
        self.name=name
        self.age=age
        
p1=mehar("Mehar Ali ", 21)   
print(p1.age)
print(p1.name)     

class animal:
    def __init__(self, nam , type) :
        self.n=nam
        self.t=type
animal1=animal("lion", "fighter")
animal2=animal("pigen", "flying")
print(animal1.n, animal1.t)
print(animal2.n,animal2.t)
print("after cloning from the git now im adding this print statement ")