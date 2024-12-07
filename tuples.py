# Run this code in Pypy 3 (since not works on python 3 => due to environment setup difference)

n = int(input())
t=tuple(map(int,input().split()))
print(hash(t))