test_array = [100, 200, 300]
bonus_array = [1, 2, 3]

list_list = [10, 1, 2]
list_list += test_array
list_list.append(3)
list_list.extend([99, 2])
list_list.insert(0, [6, 2])
list_list.insert(0, 239)

st = {1, 2, 5}
st = st.union(set(bonus_array))
st.add(7)
st.update([89])

string = str(list_list + bonus_array)
string += str(bonus_array)
string += "sdf"
test34 = ["asd", "bsc", "kmd"]
string += "      ".join(test34)

tpl = tuple(list_list + bonus_array)
l_tpl = list(tpl) + test_array
tpl = tuple(l_tpl)

d2 = { 1: "one", 2: "two", 3: None, None: "None", 4: bonus_array }
d2[5] = test_array
d2.update({90: "10"})

print(f"list: {list_list}")
print(f"string: {string}")
print(f"dictionary: {d2}")
print(f"set: {st}")
print("tuple: " + str(tpl))