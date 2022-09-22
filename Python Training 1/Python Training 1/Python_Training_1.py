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
#find out if Grace is to wash plate today
if grace_age > my_age and joshuas_age and sochimas_age:
    print("Not to wash plate today")
elif joshuas_age and my_age <= grace_age:
    print ("Not to wash \n plate today")
else: 
    print("Grace has to wash plate today")

    #Dictionary
    person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
    #add or update a new key to the dictionary
    person["friend"] =  "Joses" #added a new friend to the person's details
    person.update({"age": 29, "country": "Nigeria"}) #updating the list
    del person["friend"]
    print(person)
