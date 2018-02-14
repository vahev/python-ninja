s = set()

s.add(1)
s.add(2)

# Clears the set
s.clear()

# Creates a copy os given set
sc = s.copy()

# Throws the difference between two sets
s.difference(sc)

# return the elements that are in both sets
s1 = (1, 2, 3)
s2 = (2, 3, 5)
s1.intersection(s2)  # Will return(2, 3)

# Is disjoint if no elements of the first set is in second one
