s = input()
print(any([i.isalnum() for i in s]))    # any([True, True, True]) => True
print(any([i.isalpha() for i in s]))
print(any([i.isdigit() for i in s]))    # any([False, False, True]) => True
print(any([i.islower() for i in s]))
print(any([i.isupper() for i in s]))