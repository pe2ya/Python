list_list = [10, 1, 2, 55, 3, 2, 11, 100, 22]

tpl = tuple(list_list)

st = set(list_list)

string = str(list_list)

d2 = {1: "one", 2: "two", 1: "last one"}

print(f"list: {len(list_list)}")
print("tuple: " + str(len(tpl)))
print(f"string: {len(string)}")
print(f"set: {len(st)}")
print(f"dictionary: {len(d2)}")
