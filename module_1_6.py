my_disk = {"Ivan": 1389, "Artem": 1986, "Alex": 1989}
print(my_disk)
print(my_disk["Ivan"])
print(my_disk.get("Mariy"))
my_disk.update({"Lera": 2001,
                "Max": 1986})
a = my_disk.pop("Alex")
print(a)
print(my_disk)

my_set = {1, 5, 5, 8, 8, 9, 'Appel'}
print(my_set)
my_set.add((1, 3, 5))
my_set.add(3.0)
my_set.discard(1)
print(my_set)

