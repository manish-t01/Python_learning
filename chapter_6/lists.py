print("")

group1 = ["Manish", "Phangs", "Anok", "Devish"]
group2 = ["Nik", "Ross", 42, "11", True]
group3 = ["A", "B"]
empty_group = []
print("")

print("----------------Learning List-----------------")
print("")

print("Verifying list items.\n----------------------")

print("Anok" in group1)
print("Anok" in group2)
print("")

print("Checking index\n---------------")

print(group1.index("Devish"))
print(group1.index("Manish"))
print("")

print("Printing values form the list by differnt methods.\n--------------------------------------------------")

print(group2[0:])
print(group2[2])
print(group1[-1])
print(group2[0:3])
print(empty_group)
print(group2[1:5])
print(group2[-5:-1])
print(group2[-10:-1])
print("")

print("checking length of the lists.\n---------------------------------")

print(len(group1))
print(len(group2))
print("")

print("Adding items to the existing list by diffrent Methods \n------------------------------------------------------")

# 1st method.
group1.append('Anant')
print(group1)

# 2nd method.
group1.extend(["Bibhuti", "Laxmi"])
print(group1)

# 3rd method.
group1.extend(["Maa", "Papa"])
print(group1)

# 4th method.
group1 += ["Amit"]
print(group1)

# 5th method.
group1 += "NEHA"
print(group1)

# 6th method.
# we can also add list to another list by this method.
group1.extend(group2)
print(group1)
print("")

print("Adding items in the list accroding to the index.\n--------------------------------------------------")

# 1st method.
group3.insert(0, "Z")
print(group3)

# 2nd method.
group3[2:2] = ["hello", "wrold"]
print(group3)

# 3rd method. NOTE: This replaces the element in the list.
group3[2:3] = ["Albert", "Einstine"]
print(group3)

# 4th method.
group3[1] = 'hello'
print(group3)
print("")

print("Removing items from the list\n-------------------------------")

# 1st method.
group2.remove("11")
print(group2)

# 2nd method. NOTE: pop method removes the element from the last of a list.
group2.pop()
print(group2)

# 3rd method. NOTE: removes item accroding to index no from the list.
del group2[2]
print(group2)

# 4th method.NOTE: removes all the items from the list.
# del group3 NOTE: gives error.
group3.clear()
print(group3)
print("")

print("Learning shorting. \n---------------------")
# NOTE shorting works only on the list which contains only one type of data like only integer, only string, or other data types.
group4 = ["Manish", "Akash", "Ravi", "Devv", "Egale"]

group4[1:2] = ["abc"]
print("Before sorting", group4)
group4.sort()
print("After sorting",group4)

group4.sort(key=str.lower) # NOTE:it will sort lower case also
print("After sorting lower case too",group4)
print('')

print("Shorting numbers.\n-----------------------")

group5 = [4,3,5,26,23,15,13,18]
group5.reverse()
print("Reverse:",group5)

# group5.sort(reverse=True)
# print("Reverse & shorted:",group5)

# It preserves or makes of group5 in reverse.
print(sorted(group5, reverse=True))
print('')

# making copies.
# Method 1.
copy1 = group5.copy()
print("Copy1:",copy1)
print("")

# Method 2.
copy2 = list(group5)
print("Copy2:",copy2)
print("")

copy3 = group5[:]
copy3.sort()
print("After sorting copy3:",copy3)
print('')

group6 = [90, 20, 80, 50, 60, 40, 30]
group6.sort()
print(group6)

print(type(group1))

# Another way to make list.
mylist = list ([1, "Neil", True])
print(mylist)
print("------------------List Ends Here----------------")
print("")

print("----------------Learning Tuples-----------------")
print("")

# creating tuples.
# 1st method.
mytuple =tuple(("Manish", 42, True))
print(mytuple)
print(type(mytuple))
print("")

# 2nd method. This is called packing a tuple.
anothertuple = (1,5,3,6,8,6,6,6)
print(anothertuple)
print(type(anothertuple))
print("")

# NOTE: In Python, you cannot directly add or remove elements in a tuple.
# Therefor we use the below method to add elements in the tuple.

newlist = list(mytuple)
newlist.append("Thakur")
newtuple = tuple(newlist)
print(newtuple)
print("")

# unpacking a tuple.
(one, two, *hey) = anothertuple
print(one)
print(two)
print(hey)
print("")

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)
print('')

print(anothertuple.count(6))
print("")

print("------------------Tuple Ends Here----------------")
print("")