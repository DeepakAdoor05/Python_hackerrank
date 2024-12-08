def split_and_join(line):
    string = line.split()   # The given string is splitted and converted to a list of strings. (default delimiter is space)
    string = "-".join(string)
    return string

line = input()
result = split_and_join(line)
print(result)