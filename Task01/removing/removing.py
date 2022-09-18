list_list = [10, 1, 2, 55, 3, 2, 11, 100, 22]
list_list.pop()
list_list.remove(2)

st = set(list_list)
st.pop()
st.remove(2)
st.discard(100)

string = str(list_list)
string = string.replace("[10, ", "")
string = string.removeprefix("1, 55")
string = string.removesuffix("100]")

tpl = tuple(list_list)
l_tpl = list(tpl)
l_tpl.pop()
# continue like you do in list
tpl = tuple(l_tpl)


d2 = {1: "one", 2: "two", 3: None, None: "None", 4: "apple"}
d2.pop(1)
d2[2] = ""
d2.popitem()

print(f"list: {list_list}")
print(f"list after clear: {list_list.clear()}")
print(f"string: {string}")
print(f"dictionary: {d2}")
print(f"dictionary after clear: {d2.clear()}")
print(f"set: {st}")
print(f"set after clear: {st.clear()}")
print("tuple: " + str(tpl))

