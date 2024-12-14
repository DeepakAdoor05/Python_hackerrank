n, m = map(int,input().split())
s1 = 'WELCOME'
s = '.|.'
# part-1 Upper
for i in range(n//2):
    print((s*(i*2+1)).center(m,'-'))

# part-2 Middle
print(s1.center(m,'-'))

# part-3 Lower
for i in range(n//2-1,-1,-1):
    print((s*(i*2+1)).center(m,'-'))