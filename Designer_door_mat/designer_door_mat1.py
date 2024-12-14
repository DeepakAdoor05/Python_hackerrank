R, C = map(int, input().split(" "))

# part-1 Upper
for i in range(1,R,2):
    print((".|."*i).center(C,"-"))

# part-2 Middle
print("WELCOME".center(C,"-"))

# part-3 Lower
for i in range(R-2,-1,-2):  # range(7, -1, -2)
    print((".|."*i).center(C,"-"))