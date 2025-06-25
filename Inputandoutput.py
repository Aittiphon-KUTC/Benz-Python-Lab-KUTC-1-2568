name = input("What your name?")
print("Hello", name)



age = int (input("How old are you"))
years_to_100 = 100 - age
print(f"You will be 100 in {years_to_100} years")



num1 = float(input("Enter your first number:  "))
num2 = float(input("Enter your second number:  "))
result= num1 + num2
print(f"The result of {num1} + {num2} is {result}")

# การพิมพ์เว้นวรรค เพื่อเก็บข้อมูลในตัวแปรถัดไป
x,y = input("Enter two values seperated by space:  ").split()
print(f"frist value : {x}, second value: {y}")


user_input = input("Choose a color for press Enter fot default:  ")
if user_input =="" :
    user_input = " blue"
print(f"Selected color: {user_input}")

length = float(input("Enter length in meters: "))
print(f"That's {length + 100} centimeter")