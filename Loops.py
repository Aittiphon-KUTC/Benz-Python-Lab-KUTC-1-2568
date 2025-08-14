
#for loop
print("Counting from 1 to 5:")
for i in range (1,6):
    print(i)

print ("\n Reversed counting from 5 to 1:")
for i in range(5, 0, -1):
    print(i)

#while loop
count=1
print("while loop")
while count <= 5:
    print (count)
    count = count + 1

#Reversed while loop
count=5
print("\nReversed while loop")
while count >= 1:
    print (count)
    count = count - 1


# looping thru a list
fruit = ["apple", "banana", "cherry"]
print("My fruit")
for x in fruit:
    print(x)

# Reversed looping thru a list
print("\nMy fruit in reversed")
for x in reversed(fruit):
    print(x)

# Loop with enumrate
print("Fruit with indicies")
for index, fruit in enumerate(fruit):
    print(f"{index}:{fruit}")

# Break and continue
print("\n Loop with Break")
for i in range(1,10):
    if i > 5:
        break
    print(i)

print("\n Loop with Contiune")
for i in range(1,10):
    if i % 2 == 0:
        continue # Skip even number
    print(i)

# Infinits loop with break condition
print("\n Infinits loop Break")
i = 1
while True:
    print(i)
    i = i+1
    if i > 5:
        break