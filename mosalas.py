x = int(input(" enter number 1 : "))
y = int(input(" enter number 2 : "))
z =int(input(" enter number 3 : "))
if (x < y + z) & (y < x + z) & (z < y + x):
    print("true ")
else:
    print("false")