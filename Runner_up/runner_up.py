n = int(input())
arr = map(int, input().split())
list = []
j,k=-100,-100
for i in arr:
    list.append(i)
    list.sort()
for i in list:
    if j < i:
        k = j
        j = i
print(list)
print(k)