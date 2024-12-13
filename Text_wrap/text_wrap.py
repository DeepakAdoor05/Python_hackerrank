def wrap(string, max_width):
    my_list = []
    for i in range(0, len(string), max_width): # 0 4 8 12 16 20 24
        # if i % max_width == 0:  Instead of using step in loop, we can use this method also.
        my_list.append(string[i:i+max_width])
    return ("\n".join(my_list))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)