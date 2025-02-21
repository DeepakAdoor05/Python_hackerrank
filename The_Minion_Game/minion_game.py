def minion_game(string):
    s_count = 0
    k_count = 0
    # vow = 'AEIOU'
    for i in range(len(string)):
        if string[i] in ['A','E','I','O','U']:
            k_count += len(string) - i
        else:
            s_count += len(string) - i
    if s_count > k_count:
        print("Stuart",s_count)
    elif s_count < k_count:
        print("Kevin",k_count)
    else:
        print("Draw")
s = input()
minion_game(s)