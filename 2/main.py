# # 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# # 🚨 Don't change the code above 👆

# two_digit_number=str(two_digit_number)
# num1=two_digit_number[0]
# num2=two_digit_number[1]
# print(int(num1)+int(num2))


#PEMDAS


# #Calculate BMI
# weight= input("Enter weight")
# height= input ("Input Height")
# bmi= (int(weight) /float(height)**2)
# print (int(bmi))



# ## Round Function
# print (round(8/3,3))

# ## Floor Division
# # it will print the result in int and discard all the values after decimal
# print (round(8//3))

# ##
# score =0
# score+=1
# print(score)
# isWinning= True

# #F STRING
# print(f"your score is {score}")

# 365
# 52.1429
# 12

# age=input("Enter age")
# finalAge=90
# ageLeft= finalAge - int(age)
# remainingDays= ageLeft*365
# remainingWeeks= ageLeft*52
# remainingMonths=ageLeft*12
# # print(f"Days remaining: {remainingDays}")
# # print(f"Weeks remaining: {remainingWeeks}")
# # print(f"Months remaining: {remainingMonths}")
# # print(f"Years remaining: {ageLeft}")

# print(f"you have {remainingDays} days, {remainingWeeks} weeks, {remainingMonths} months left")


print("Welcome to the tip calculator\n")
totalBill= input("What was the total bill? ")
tipPercentage= input("What percentage would you like to give? 10, 12, or 15? ")
totalPersons= input("How many people to split the bill? ")
tip=(round(float(totalBill),2)/100)*round(float(tipPercentage),2)
bill_after_tip=float(totalBill)+float(tip)
split=float(bill_after_tip)/int(totalPersons)
#roundedSplit=round(split,2)

## Output Formatting
roundedSplit="{:.2f}".format(split)
print(f"Each person should pay: ${roundedSplit}")
