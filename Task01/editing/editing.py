list_list = [10, 1, 2, 55, 3, 2, 11, 100, 22]
list_list[3] = 22

tpl = tuple(list_list)

st = set(list_list)
# impossible

string = str(list_list)
string.replace("[10, 1", "aboba")

d2 = {1: "one", 2: "two"}
d2[1] = "yacht"
d2.update({2: "tree"})

print(f"list: {list_list}")
print("tuple: " + str(tpl))
print(f"set: {st}")
print(f"string: {string}")
print(f"dictionary: {d2}")

try:
    tpl[0] = 11
except Exception as e:
    print(e)

try:
    string[2] = "asd"   # looks like shit
except Exception as e:
    print(e)
