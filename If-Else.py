# Basic If else 

total = 29

if total > 30 : 
    print("Pass")
elif total > 20 :
    print("Good Job")
else : 
    print("Fail")

# Multiple check 
age = 19
licence = True

if age >= 18 and licence :
    print("you can drive a car")
elif age>=18 and not licence :
    print("you need to get a driver license first")
else :
    print("you can not drive a car")

# Nested if else 
score = 90

if score>=80 :
    print("You Pass")
    if score>= 80 :
        print("You got A")
    elif score>= 70 :
        print("You got B")
    elif score>= 60 :
        print("You got C")
else: 
    print("You fail")


# Use In conditionals

fruit = "banan"
if fruit in ["apple", "banana", "orange"]:
    print(f"{fruit} is in the list")
else:
    print(f"{fruit} is not in the list")

# Ternary oneline if else

age = 20

status = "adult" if age >= 18 else "minor"
print(f"Status: {status}")

# compare string
password ="scret123"

if password == "scret123" :
    print("Access complete")
else :
    print("No Access")

# chaining comparisons
x = 15
if 10 < x < 20 :
    print("X is beteen 10 and 20")

# truthy or falsy
user_input = "fsdf"
if user_input:
    print("Input approved")
else :
    print("No input")
