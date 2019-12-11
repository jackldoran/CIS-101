import random
a = 1
b = 20
Length=random.randint(a,b)
Width=random.randint(a,b)

print("Length = ")
print(Length)

print("Width = ")
print(Width)

print("Area = Length x Width")

Area = Length*Width

print("Area = ")


print(Area)

if Area >= 100:
    print("The room is huge!")
if Area < 100:
    print("The room is small.")
if Area == 100:
    print("Just right...")




