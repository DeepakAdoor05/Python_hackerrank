def count_substring(string, sub_string):
    count = 0
    for _ in range(0,len(string)):
        if sub_string in string:
            position = string.index(sub_string)
            #print(position)
            length = len(sub_string)
            #print(length)
            string = string[:position] + string[position+length-1:]
            #print(string)
            count += 1
        else:
            break
    return count

string = input().strip()
sub_string = input().strip()
    
count = count_substring(string, sub_string)
print(count)