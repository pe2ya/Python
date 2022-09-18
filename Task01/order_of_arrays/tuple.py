list_list = [10, 1, 2, 55, 3, 2, 11, 100, 22]

tpl = tuple(list_list)

st = set(list_list)

string = str(list_list)

print(f"list: {list_list}")
print("tuple: " + str(tpl))
print(f"set: {st}")
print(f"string: {string}")

try:

    d = dict(list_list)
    print(d)
except Exception as e:
    print(f"dictionary: {e}")


d2 = {1: "one", 2: "two"}

print(f"dictionary: {d2}")




