def count_substring(string, sub_string):
    c=0
    x=-1
    while x < len(string):
        # string.find(sub_string,start,end)
        z = string.find(sub_string,x+1) # Finds the index of the sub-string from the string
        if z == -1: # If not finds returns -1
            break
        c += 1
        x=z
    return c

string = input().strip()
sub_string = input().strip()
    
count = count_substring(string, sub_string)
print(count)