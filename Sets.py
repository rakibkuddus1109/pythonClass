# Sets : Sequence of values separated with comma declared inside {} and contains unique values only
# Sets are not in fixed order, it may change its order and can't be predicted
# a={3,5,7,"Python",3,6,5,4}
# print(a) # Removes duplicate

# a={} # It is considered as Dict
# a=set() # This is how we declare empty set

# print(dir(set))

# Sets are mutable but elements inside sets should be immutable only (so sets can't contain list/dict)

# add : For adding single element in set
a={3,5,7,"Python",3,6,5,4}
# a.add(54)
# print(a)
# a.add("Chennai")
# print(a)

# update : For adding multiple values at a time in set
# a.update("Chennai",54,65.4) # It would give error as it has int but update values should be in sequence
# a.update(["Chennai",54,65.4])
# print(a)

# remove : To remove any element from set
# a.remove("Python")
# print(a)

# discard : To remove any element from set, if element is not present it would continue without error
# a.update(["Chennai",54,65.4])
# # a.discard("Chennai")
# a.discard("chn")
# print(a)

# pop : Would remove starting element inside set
# a.pop()
# print(a)
# print(a.pop()) # prints which element is getting removed

# clear : removes all elements and makes as an empty set
# a.clear()
# print(a)

# Sets Operations:
    # union(|)
    # intersection(&)
    # difference(-)
    # symmetric difference(^)

# union : is performed between 2 or more sets only
a={3,5,"Python",5.6}
b={5.4,2,"Django",3}
# print(a.union(b))
# print(a|b)

# intersection : To get common element between sets
# print(a.intersection(b))
# print(a&b)

# difference : removes elements of set which is in 2nd argument and returns element of set which is in 1st argument
# print(a.difference(b)) # Subtracting b elements from a
# print(a-b)
# print(b-a) # Subtracting a elements from b

# symmetric difference: To remove common elements from sets and get uncommon elements
# print(a.symmetric_difference(b))
# print(a^b)

# intersection_update
# print(a)
# a.intersection_update(b)
# print(a)

# difference_update
# a.difference_update(b)
# print(a)

# symmetric_difference_update
# a.symmetric_difference_update(b)
# print(a)

# issubset
a={2,3,4,5}
b={3,5}

print(a.issubset(b))

# isuperset
print(a.issuperset(b))

# isdisjoint
print(a.isdisjoint(b))

# copy
c={3,4,5,6}
d=c.copy()
print(c)
print(d)
c.add(7)
print(c)
print(d)

# frozensets : Immutable datatypes
a={1,2,3,4}
b=frozenset({1,2,3,4})
print(b)