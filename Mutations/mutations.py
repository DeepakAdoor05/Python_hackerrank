def mutate_string(string, position, character):
    #print(string)
    mutable_list = list(string)
    mutable_list[position] = character
    string = "".join(mutable_list)
    return string

s = input()         # string is immutable
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)

# abracadabra
# 5 k 