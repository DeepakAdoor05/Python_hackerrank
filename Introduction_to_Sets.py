def average(array):
    set_arr=set(array)
    return sum(set_arr)/len(set_arr)

n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)

# Sample Input
# 10
# 161 182 161 154 176 170 167 171 170 174

# Sample Output
# 169.375