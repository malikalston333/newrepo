#Input of age & name
name = input ("What's your name")
age = int(input("How old are you?"))

print(type(age))
#Display Results
print ("Hello, " + name + "!")
print ()
print("You are " + str(age) + " years old.")
print(type(age))
print()

#Display if you have to learn or fine like wine
if age >= 30:
    print(type(age))
    print ("You are fine like wine!")
else:
    print ("You have alot to learn.")