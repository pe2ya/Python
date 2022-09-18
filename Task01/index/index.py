list_list = [10, 1, 2, 55, 3, 2, 11, 100, 22]

tpl = tuple(list_list)

st = set(list_list)

string = str(list_list)

d2 = {1: "one", 2: "two"}

print(f"list: {list_list[1]}")
print("tuple: " + str(tpl[1]))
print(f"string: {string[1]}")
print(f"dictionary: {d2[1]}")

try:
    print(f"set: {st[1]}")
except Exception as e:
    print(e)
else:
    print("\n\nProgram executed correctly")




