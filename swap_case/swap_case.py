def swap_case(s):
    letter = ""
    for i in s:
        if i == i.lower():
            i = i.upper()
        else:
            i = i.lower()
        letter = letter + i
    return letter


s=input()
result = swap_case(s)
print(result)