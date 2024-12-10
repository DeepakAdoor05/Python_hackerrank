def mutate_string(string, position, character):
    #print(string)
    mutable_string = string[:position] +character+ string[position+1:]
    return mutable_string

s = input()         # string is immutable
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)