def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 ==0:
                leap = True
                print("Leap year")
            else:
                leap = False
                print("Not Leap year")
        else:
            leap = True
            print("Leap year")
    else:
        leap = False
        print("Not Leap year")
    
    return leap

year = int(input())
print(is_leap(year))