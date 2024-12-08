def swap_case(s):
    x = ""
    for c in s:
        if c.islower():
            c=c.upper()
        else:
            c=c.lower()
        x += "".join(c)
    return x


s=input()
result = swap_case(s)
print(result)

"""  
        --Another method--
def swap_case(s):
    return s.swapcase()

s = input()
result = swap_case(s)
print(result)
"""