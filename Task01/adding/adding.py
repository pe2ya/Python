test_array = [100, 200, 300]
bonus_array = [1, 2, 3]

list_list = [10, 1, 2, 55, 3, 2, 11, 100, 22]
list_list += test_array

st = set(list_list)
st.union(set(bonus_array))

string = str(list_list + bonus_array)
string += str(bonus_array)

d2 = {1: "one", 2: "two", 3: None, None: "None", 4: bonus_array}
d2[5] = test_array

print(f"list: {list_list}")
print(f"string: {string}")
print(f"dictionary: {d2}")
print(f"set: {st}")
try:
    tpl = tuple(list_list + bonus_array)
    l_tpl = list(tpl) + test_array
    tpl = tuple(l_tpl)
    print("tuple: " + str(tpl))

except Exception as e:
    print(e)
else:
    print("\n\nProgram executed correctly")




