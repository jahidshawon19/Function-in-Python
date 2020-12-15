""" 
Author: Jahid Hasan Shawon 
Email: jahidshawon1730@gmail.com

"""



# Define a Function
def greeting():
    print ("Hello Rubab Tech")

greeting()

# passing inforamtion to a function

def propose(girl_name):
    print ("I love you"+girl_name.title()+"! Please Accept me")

propose("Boroloker Beti")


# Interview question:What are Arguments and Parameters?
def propose(girl_name): # Here girl_name is Argument
 propose("Boroloker Beti") # Here Boroloker Beti is Parameters


#Positional Arguments

def describe_product(category,item_name,price):

    print("Category: "+category.title()+"\nItem Name: "+item_name.title()+"\nPrice: "+str(price).title()+"\n\n")

describe_product("pant","denim",4500)
describe_product("shirt","easy",2500)


#Keyword Arguments

def describe_product(category,item_name,price):

    print("Category: "+category.title()+"\nItem Name: "+item_name.title()+"\nPrice: "+str(price).title()+"\n\n")

describe_product(category="pant",item_name="denim", price=4500) #just change here


#Default Values

def myfun(food,drink="cocacola"):
    print("I love "+drink.title()+" and "+food.title())

myfun("pasta")

# simple return value

def inforamtion(first_name,last_name):
    full_name = first_name+" "+last_name
    return full_name.title()

x = inforamtion("hammad","ali")
print("Name is "+x)

#Making an Argument Optional

def displayInfo(first_name,last_name,middle_name=""): #The middle name is optional, so it’s listed last in the definition
    if middle_name:
        full_name = first_name+" "+middle_name+" "+last_name
    else:
        full_name = first_name+" "+last_name
    
    return full_name.title()


x = displayInfo("jahid","hasan","shawon")
print(x)
y = displayInfo("asikul","islam")
print(y)


# Returning a Dictionary

#p-1
def person(first_name,last_name,age):
    x = {'first':first_name,
         'last':last_name,
         'age':age
    }
    return x

z = person("donald","trump",25)
print(z)

#p-2  (You can easily extend this function to accept optional values)
def person(first_name,last_name,age,phone=""):

    x = {'first':first_name,
         'last':last_name,
         'age':age
    }
    if phone:
        x['phone'] = phone
    return x

z = person("donald","trump",25,12345)
print(z)



# Using a Function with a while Loop

def propose(nibbi,nibba):
    statment = "hey "+nibbi.title()+", I am "+nibba.title()+" Will you mary me?"
    return statment

while True:
    yourName = input("What is your Name: ")
    crushName = input("What is your Crush Name: ")
    if crushName == 'rani mondol':
        break
    feedback = propose(crushName,yourName)
    print(feedback)


# Passing a List

def patel(crush):
    for x in crush:
        print(x.title()+" I Love You")
        
mycrush = ["chokina","jorina","aluni"]
patel(mycrush)


# Passing an Arbitrary Number of Arguments

#p-1
def luckyNumber(*num):
    print(num)

luckyNumber(11)
luckyNumber(12,32,31,0) 
#p-2 
def orderFood(*food):
    for x in food:
        print("you ordered: "+x)

orderFood("burger")
orderFood("chicken","pizza","soup")

Mixing Positional and Arbitrary Arguments

def orderFood(quantity, *food):
    print("Quantity: "+str(quantity))
    for x in food:
        print("You Ordered: "+x)

orderFood(3,"pizza")
orderFood(10,"kacci","burger")

# Using Arbitrary Keyword Arguments

def createProfile(first_name,last_name, **moreInfo):
    profile = {}
    profile['first'] = first_name 
    profile['last'] = last_name 
    
    for key ,value in moreInfo.items():
        profile[key] = value 

    return profile     


studentProfile = createProfile("tamim","billah", id="C173000")
print(studentProfile)
customerProfile = createProfile("Abul","hossen", phone="01246894",email="abul@gmail.com")
print(customerProfile)
