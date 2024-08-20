# set is immutable
# sets cannot contain duplicate value
# Sets are unordered
# Sets are unindexed
# set is a collection of well defined objects which is not repeating


s = {1, 5, 32, 54,5, 5, 5, "Harry"};

print(s, type(s))
print(len(s))

s.add(566);
s.remove(1);
print(s, type(s))

# set.pop() # => remove random element from sets
# s.clear(); # => clear the whole set
print(len(s))