s = input()
string = list(s)
#print(string)
alpha = digit = lower = upper = alnum = False
for char in string:
    if char.isalnum():
        alnum = True
    if char.isalpha():
        alpha = True
    elif char.isdigit():
        digit = True
    if char.islower():
        lower = True
    elif char.isupper():
        upper = True
if alnum == True:
    print(True)
else:
    print("False")
if alpha == True:
    print(True)
else:
    print("False")
if digit == True:
    print(True)
else:
    print("False")
if lower == True:
    print(True)
else:
    print("False")
if upper == True:
    print(True)
else:
    print("False")

# qA2

#True   alphanumeric characters
#True   alphabetical characters
#True   digits
#True   lowercase
#True   uppercase