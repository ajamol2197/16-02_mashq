# 1-m
a = {"tom", "bob", "alice", "tom"}
print(a)

# 2-m
a = {"mike", "bill", "ted"}
b = set(a)
print(b)

# 3-m
j = {"tom", "bob", "alice"}
print(len(j))

# 4-m
a = set()
a.add("cammma")
print(a)

# 5-m
a = {"tom", "bob", "alice"}

i = "tom"
if i in a:
    a.remove(i)
print(a)

# 6-m
a = {"tom", "bob", "alice"}
st = a.copy()
print(st)

# 7-m
a1 = {"tom", "bob", "ali"}
a2 = {"sam", "kane", "bob"}

a3 = a1.union(a2)
print(a3)

# 8-m
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}

users3 = users.intersection(users2)
print(users3)

# 9-m
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}

users3 = users.difference(users2)
print(users3)
print(users - users2)

# 10-m
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}

users3 = users.symmetric_difference(users2)
print(users3)

users4 = users ^ users2
print(users4)

# 11-m
users = {"Tom", "Bob", "Alice"}
sup = {"Sam", "Tom", "Bob", "Alice", "Greg"}

print(users.issubset(sup))
print(sup.issubset(users))
