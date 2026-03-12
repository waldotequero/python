#list datastructure
#ordered
# indexed
names = ["Alice", "Bob", "Charlie"]
names.append("Jeff")
names.insert(1,"Mary")
print(names)
names[0] = "David"
print(f"my name is {names[0]}")
# changeable/mutable


# tuples datastructure
# ordered
# indexed
# unchangeable/immutable
country=("Kenya", "Uganda", "Tanzania", "Rwanda", "Burundi")
print(country)
print(f"I was born in {country[2]}")


# set datastructure
# unordered
# unindexed
# unchangeable/immutable
cars={"Toyota", "Honda", "Ford", "BMW", "Mercedes"}


# dictionary datastructure
# key value pair
# mutable
staff={"name":"Alice", "age":30, "position":"Manager"}
print(f"employee name is {staff['name']}")
print(f"employee age is {staff['age']}")
print(f"employee position is {staff['position']}")  