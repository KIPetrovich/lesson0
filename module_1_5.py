immutable_var = int, float, "String", True,
print(immutable_var)
#tuple[1] = 56                                   # Нельзя изменять кортыжи, т.е. они не изменяемые
#print(immutable_var)

mutable_list = [1, "appel", True,]
print(mutable_list)
mutable_list.append("string")
print(mutable_list)