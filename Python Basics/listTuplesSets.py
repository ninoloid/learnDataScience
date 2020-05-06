# List is very similar to array in JS
listExample = [1, 3, 2, 4]
tupleExample = (5, 6, 7, 8)
setExample = {'this', 'is', 'a', 'set'}

# length of the list
print(len(listExample))

# value of list by index
print(listExample[2])

listExample.append(2) # same as array.push in JS
listExample.pop() # same as array.pop in JS

# In Python, we can remove the item in the list by index
# using listName.pop(index)

# sort the list
listExample.sort()
print(listExample)

# Tuple is very similar to list as concept
# But, tuple is immutable while list is mutable.
# Tuple can be declared with ()


# SET
# Each element of a set is unique and cannot be changed.
# However the set can take new unique element or remove element from it
# Set is declared with {}
setExample.add('added') # will be added
setExample.add('set') # won't be added as the value isn't unique
print(setExample)