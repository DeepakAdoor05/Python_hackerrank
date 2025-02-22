def merge_the_tools(string, k):
    m = 0
    l = []
    for i in range(len(string)//k):
        l.append(string[m:m+k])
        m += k
    # print(l)                                                  ['AAB', 'CAA', 'ADA']
    for v in l:
        # print(list(v))                                        ['A', 'A', 'B']
        # print(dict.fromkeys(list(v)))                         {'A': None, 'B': None}
        # print(dict.fromkeys(list(v), 1))                      {'A': 1, 'B': 1}
        # print(dict.fromkeys(list(v)).keys())                  dict_keys(['A', 'B'])
        # print(list(dict.fromkeys(list(v)).keys()))            ['A', 'B']
        print(''.join(list(dict.fromkeys(list(v)).keys())))     # AB

string, k = input(), int(input())       # AABCAAADA  3
merge_the_tools(string, k)