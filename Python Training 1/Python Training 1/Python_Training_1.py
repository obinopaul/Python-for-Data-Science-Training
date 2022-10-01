from math import *

'''
my_name = input ("write your name ")
my_age = input("write your age ")
# print (my_name) #this is a comment
print(type(my_name))
print(type(my_age))
print( my_name + " is my name, \ni am " + my_age + " years old")
#last_output = print( my_name + " is my name, \ni am " + my_age + " years old")
#print (last_output.upper())

first_topic = "working with numbers"
second_topic = "Getting input from users"
print( second_topic.upper())
print( second_topic.replace("input", "data").upper()) #replaced the text and capitalized the results
print ( (first_topic[0:12] + " texts and" + first_topic [12:]).upper()) #re
'''

#working with numbers
my_age = 26
sochimas_age = 34
grace_age = 18
joshuas_age = 28
my_favourite_colors = ["white", "blue", "green", "milk", "grey", "brown"]
my_favourite_numbers = [12, 13, 10, 6, 4, 3, 7]
'''
print(abs (my_age))
print(max( my_favourite_numbers))
print(min( my_favourite_numbers))
print(pow( max(my_favourite_numbers) , min( my_favourite_numbers)))
print(floor(23.6))
print(ceil(23.6))
print(sqrt( max(my_favourite_numbers) * min( my_favourite_numbers)))
print(30%3)
print(32//3)
print(floor(32/3))
print(ceil(32/3))

print(my_age == joshuas_age)
print(my_age >= joshuas_age)
print(my_age <= joshuas_age)
print(my_age != joshuas_age)
'''
##find out if Grace is to wash plate today
#if grace_age > my_age and joshuas_age and sochimas_age:
#    print("Not to wash plate today")
#elif joshuas_age and my_age <= grace_age:
#    print ("Not to wash \n plate today")
#else: 
#    print("Grace has to wash plate today")

    ##Dictionary
    #person = {
    #'first_name':'Asabeneh',
    #'last_name':'Yetayeh',
    #'age':250,
    #'country':'Finland',
    #'is_marred':True,
    #'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    #'address':{
    #    'street':'Space street',
    #    'zipcode':'02210'
    #}
    #}
    ##add or update a new key to the dictionary
    #person["friend"] =  "Joses" #added a new friend to the person's details
    #person.update({"age": 29, "country": "Nigeria"}) #updating the list
    #del person["friend"]
    #print(person)

    #her_age = input ("write the value of n: ")
    #print ( n + int(n and n) + int(n and n and n))    

#print (25.6//4)
#print (25.6/4)
#x = int(input("add a number: "))
#print(x>=25)
#print(x)
##conditional statement
#if (x%2 == 0) is True:
#    print("This value is an even number")
#else:
#    print ("This value is an odd number")

#x = int(input("add a number: "))
#print(x>=25)
#print(x)
#conditional statement
#numbers = (0,1,2,3,4,5,12,34,21,22,34,45,67)

#for x_amp in numbers:
#    if (x%2 == 0) is True and x not in numbers:
#        print("This value is an even number and not in the dataset")
#        break
#    elif (x%2 == 0) is True and x in numbers:
#        print("This value is an even number and in the dataset")
#        break
#    elif (x%2 == 0) is False and x not in numbers:
#        print("This value is an odd number and not in the dataset")
#        break
#    elif (x%2 == 0) is False and x in numbers:
#        print("This value is an odd number and in the dataset") 
#        break
#    elif (x%2 == 0) is True and x > x_amp in numbers:
#        print("This value is an even number and larger than the dataset")
#        break
#    elif (x%2==0) is True and x<=x_amp in numbers:
#        print ("This value is an even number and smaller than the dataset")
#        break
#    elif (x&2 ==0) is False and x != x_amp in numbers:
#        print ("This value is an odd number and not in the dataset")
#        break
#    else:
#        print ("This value is not what is required")
#        continue 
#    print(x_amp)
    
#email_address = ["acobapaul@gmail.com", "paltwizzy21@gmail.com", "veritas@gmail.com", "ifjos123@gmail.com", "beulahgrace@gmail.com", "acoba_cornel@gmail.com"]
#password = ["repent19", "repent", "repent21", "Repent19$", "repent19$", "ThisIsGooglePassword", "ThisIsFacebookPassword"]

#user_email = str (input("Please input your email address: "))
#user_password = str (input("Please input your password: "))

#for input in email_address and password:
#    if user_email in email_address and user_password in password:
#        print("login details confirmed")
#        break
#    elif user_email not in email_address and user_password in password:
#        print("email address not found")
#        break
#    elif user_email in email_address and user_password not in password:
#        print("incorrect password, Please click 'forgotten password'")
#        break
#    else:
#        print("Incorrect login")

##Functions
#def paul_age (name, age):
#    return "My name is {}, " "and " "my age is {}".format(name, age)

##paul_age()
#print(paul_age("paul",26))

#def my_life ():
#    return ()

#my_life()

# functio to cube a number
#def cube_number ():
#    my_number = int(input("Write the number: "))
#    print (pow(my_number,3))
#    if (my_number %2 == 0) is True:
#        print("This value is an even number")
#    else:
#        print("This value is an odd number")
#    return ("the function was successful")

#print (cube_number ())

#def cube_number (my_number1, my_number2):
#    #my_number1 = float (input("Write the number: "))
#    #my_number2 = float (input("Write the number: "))
#    print (pow(my_number1,my_number2))
#    if (my_number1 %2 == 0) is True:
#        return ("This value is an even number \nthe function was successful")
#    else:
#        return ("This value is an odd number \nthe function was successful")
#    return ("the function was successful")

#print (cube_number (float (input("Write the first number: ")), float (input("Write the second number: "))))

#try: 
#    number_grid = [ [1,2,3], [4,5,6], [7,8,9], [0]   ]
#    print(number_grid [2] [1])
#    #or
#    for row in number_grid:
#        for col in row:
#            print(col [1])

#except:
#    print ("invalid error")

#other types of exceptions
#except ImportError:
    #print("invalid import Error")
#except IndexError:
#    print ("invalid import error")
##for a comprehensive list of exceptions check here (https://www.programiz.com/python-programming/exceptions )

#relocating = open("C:\Users\Cornel\Desktop\Relocating\RELOCATING.docx", "r+")
#print(relocating.readable())

friends = ["Esther", "Sarah", "Gabriel"]
print(friends[1])