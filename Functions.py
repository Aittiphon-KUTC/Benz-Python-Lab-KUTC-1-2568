# function can reused

def greet_everyone():
    print("Hello Everyone")

greet_everyone()

def greet(name):
    print("Hello ", name)

greet("benz")
greet("Nom")

#without functions
user1="Benz"
print("Hello", user1 ,"Welocome to my website Hope you will enjoy.")

user2="Nom"
print("Hello", user2 ,"Welocome to my website Hope you will enjoy.")

user3="Tag"
print("Hello", user3 ,"Welocome to my website Hope you will enjoy.")

#with functions
def greet_user(name):
    print("Hello", name ,"Welocome to my website Hope you will enjoy.")

greet_user("Benz")
greet_user("Nom")
greet_user("Tag")

def power(base, exponent):
    return base ** exponent

x = power(2,5)
y = power(8,2)

print(x)
print(y)

print(power(2,5))