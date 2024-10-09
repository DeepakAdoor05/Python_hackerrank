x = int(input("x :"))
y = int(input("y :"))
z = int(input("z :"))
n = int(input("n :"))
# syntax : newlist = [expression(element) for element in oldlist if condition]
""" 
Eg:-   
    numbers = [2,3,4,6]
    list = [x*2 for x in numbers if x%2 == 0]
    print(list)

    o/p : [4, 8, 12]

"""
array = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]

print(array)