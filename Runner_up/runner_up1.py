n = int(input())
arr = list(map(int, input().split()))
list = []
for i in arr:
    if i < max(arr):
        list.append(i)
print(max(list))