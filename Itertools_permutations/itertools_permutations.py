from itertools import permutations
# print(list(permutations(['1','2','3'])))
# [('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
# print(list(permutations('abc',3)))
# [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
S, k = input().split()
k = int(k)
# print(S,k)
# print(list(permutations(S,k)))
for i in sorted(permutations(S,k)):
    string = "".join(i)
    print(string)