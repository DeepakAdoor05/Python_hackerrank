import string  # For using capwords()
def solve(s):
    return(string.capwords(s,' '))

s= input()
print(solve(s))