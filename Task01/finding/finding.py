list_list = [10, 1, 2, 55, 3, 2, 11, 100, 22]

tpl = tuple(list_list)

st = set(list_list)

string = str(list_list)

d2 = {1: "one", 2: "two", 3: "three"}

print(list_list[2])
print(tpl[2])
print(string[2])
print(f"{list(st)[2]}")

print(f"{d2[list(d2.keys())[2]]}")
print(f"{d2.get(list(d2.keys())[2])}")


