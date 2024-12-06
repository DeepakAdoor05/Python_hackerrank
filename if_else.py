n = int(input().strip())
if n in range(1, 101):
    if n % 2 != 0:
        print("Weird")
    else:
         if n in range(2, 6):    # if n >= 2 and n <= 5:
            print("Not Weird")
         elif n in range(6, 21): # elif n >= 6 and n <= 20:
            print("Weird")
         else:                   # elif n > 20:
            print("Not Weird")