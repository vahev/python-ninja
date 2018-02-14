# A set of advanced List methods
ls = [1, 2, 3]

# Appends a new elements into the list at the Appends
# You can append a List into another List
ls.append(4)  # [1, 2, 3, 4]
ls.append([4, 5])  # [1, 2, 3, [4, 5]]

# Counts a given object into the list and return the no of coincidences
ls.count(1)  # 1

# Given a List of elements, they will be added to the extended list
ls.extend([4, 5])  # [1, 2, 3, 4, 5]

# Will return the index of a given elelment
ls.index(2)  # 1

# Will insert a new value in the position specified
ls.insert(2, 'inserted')  # [1, 2, 'inserted']

# Remove th value if it is contained into the list
ls.remove('inserted')  # [1, 2]

# Will reverse the order of the elements of a list
ls.reverse()  # [3, 2, 1]
