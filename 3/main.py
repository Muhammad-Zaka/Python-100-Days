## Basic Conditional Statement
# print("Welcome to the rllercoaster")
# height= int(input("Enter height CM? "))

# if height >= 120:
#     print("You are good to go")
# else:
#     print("Not allowed")

##Odd and Even Number check
# number= int(input("Enter a number"))

# if number%2 == 0:
#     print("Even")
# else:
#     print("Odd")

## Weight and Age Check
# height= int(input("Enter height CM? "))
# price=0

# if height >= 120:
#     print("You are good to go")
#     age=int(input("Enter Age? "))
#     photos= input("Want Photos? Y/N ") 
#     if age <=18:
#         price=7
#     else:
#         price=12
#     if photos=="Y":
#         price+=3
#     print(price)
# else:
#     print("Not allowed")

# ## Update BMI
# height=float(input("Enter height CM ? "))
# weight=float(input("Enter weight KG ? "))
# bmi=int(weight / (height/100)**2)
# print(bmi)
# #print(height)
# #print(weight)
# if bmi < 18.5:
#     print("under Weight") 
# elif bmi>18.5 and bmi<25:
#     print("Normal Weight")
# elif bmi>25 and bmi<30:
#     print("Normal Weight")
# elif bmi>30 and bmi<35:
#     print("Normal Weight")
# else:
#     print("Clinically Obese")
    
# ## PIZZA Problem
# size= input("Size? S M L ")
# add_pepperoni=input("Want pepperoni? Y/N ")
# add_cheese=input("Want cheese? Y/N ")
# price=0
# if size == "S":
#     price=15
#     if add_pepperoni=="Y":
#         price+=2
# elif size == "M":
#     price=20
#     if add_pepperoni=="Y":
#         price+=3
    
# elif size == "L":
#     price=25
#     if add_pepperoni=="Y":
#         price+=3
# else:
#     print("Enter a valid input")
# if add_cheese=="Y":
#     price+=1

# print (f"Price: ${price}")






## Love Calculator
his_name=input("Enter his name? ".upper)
her_name=input("Enter her name? ".upper)
t=0
l=0
for x in his_name:
    if x=="T" or x=="R" or x=="U" or x=="E":
        t+=1
    if x=="L" or x=="O" or x=="V" or x=="E":
        l+=1
        
for x in her_name:
    if x=="T" or x=="R" or x=="U" or x=="E":
        t+=1
    if x=="L" or x=="O" or x=="V" or x=="E":
        l+=1

print(f"Percentage: {t}{l}%")



