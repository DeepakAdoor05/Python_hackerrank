n = int(input())
lst = []
for i in range(n):
    cmd = input().split()   # eg: append 6  => cmd=['append','6']
    if cmd[0] == 'append':
        lst.append(int(cmd[1]))
    elif cmd[0] == 'insert':    #insert 0 5
        lst.insert(int(cmd[1]),int(cmd[2]))
    elif cmd[0] == 'remove':
        lst.remove(int(cmd[1]))
    elif cmd[0] == 'print':
        print(lst)
    elif cmd[0] == 'pop':
        lst.pop()
    elif cmd[0] == 'sort':
        lst.sort()
    else: 
        lst.reverse()