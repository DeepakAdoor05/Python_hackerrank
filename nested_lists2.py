grade=[]
res = []
index_value = []
n = int(input())
for _ in range(n):
        name = input()
        mark = float(input())
        grade.append(mark)
        res.append([name, mark])
print(res)
grade = set(grade)
print(grade)
grade.remove(min(grade))
name = []
for val in res:
       if val[1] == min(grade):
              name.append(val[0])
print(name)
for name in sorted(name):
       print(name)