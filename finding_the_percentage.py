n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
print(student_marks)
value_list = student_marks.get(query_name)
print(value_list)
sum = 0
for i in value_list:
    sum = sum + i
average = sum/len(value_list)
print(f"{average:.2f}")         #:.2f => 2 decimal points (56.00)
