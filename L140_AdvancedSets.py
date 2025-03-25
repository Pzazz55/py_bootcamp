'''
**********************************************************************************************************
Working with Advanced Python Objects - Lesson 138 to 144
**********************************************************************************************************
The below script demonstrates 'Advanced Sets':
- add, clear, copy, difference, difference_update, discard, intersection, intersection_update, isdisjoint,
  issubset, issuperset, symmetric_difference, symmetric_difference_update, union, update
**********************************************************************************************************
'''
#Set does not take any duplciate items.

s = set()

print("\nAdding elements to the Set ::")
print("The set before adding elements is :: ", s)
s.add(1)
s.add(2)
print("The set after adding elements is :: ", s)

print("\nAdding duplicate elements to the Set ::")
print("The set before adding duplicate elements is :: ", s)
s.add(2)
print("The set after adding duplicate elements is :: ", s)
print(s)

print("\nClearing the elements from the Set ::")
print("The set before clearing the elements is :: ", s)
s.clear()
print("The set after clearing the elements is :: ", s)
print(s)

print("\nCopying a Set ::")
s = {1, 2, 3}
sc = s.copy()
print("The copied set is :: ", sc)

print("\nDifference of two or more Set ::")
se1 = {1, 2, 3, 4, 5}
se2 = {1, 3, 5}
print("Set#1 before the Difference is ::", se1) 
print("Set#2 before the Difference is ::", se2)
print("The difference between Set#1 and Set#2 is ::", se1.difference(se2))
print("Set#1 after the Difference is ::", se1) 
print("Set#2 after the Difference is ::", se2)


print("\nDifference Update ::")
se1 = {1, 2, 3}
se2 = {1, 4, 5}
print("Set#1 before the Difference Update is ::", se1) 
print("Set#2 before the Difference Update is ::", se2)
se1.difference_update(se2)
#Returns the first set after removing all the elements that were found in the second set
print("Set#1 after the Difference Update is ::", se1) 
print("Set#2 after the Difference Update is ::", se2) #should not change


print("\nDiscard elements in the Set ::")
s = {1, 2, 3, 7, 9, 4, 5}
print("The set before dicarding the elements is ::", s)
s.discard(1)
print("The set after dicarding the elements is ::", s)


print("\nIntersection of two or more elements in the Set ::")
se1 = {1, 2, 3, 4}
se2 = {1, 3, 5}
print("Set#1 is :: ", se1)
print("Set#1 is :: ", se2)
# se1.intersection(se2)
#returns the common elements between both the sets.
print("Intersection is ::", se1.intersection(se2))
print("Set#1 after the Intersection is ::", se1) 
print("Set#2 after the Intersection is ::", se2) 


print("\nIntersection update will update the set with the intersection of itself ::")
se1 = {1, 2, 3, 4}
se2 = {1, 3, 5}
print("Set#1 is :: ", se1)
print("Set#1 is :: ", se2)
#update the set with the intersection of itself.
se1.intersection_update(se2)
print("Set#1 after the Intersection Update is ::", se1) 
print("Set#2 after the Intersection Update is ::", se2) 

print("\nNull Intersection ::")
se1 = {1, 2}
se2 = {1, 2, 3, 4}
se3 = {5}
print("Returns 'True' if both the Sets don't have NULL Intersection ::", se1.isdisjoint(se2))
print("Returns 'True' if both the Sets don't have NULL Intersection ::", se1.isdisjoint(se3))

print("\nIs Subset ::")
se1 = {1, 2}
se2 = {1, 2, 3, 4}
se3 = {5}
print("Returns 'True' if the first set is a subset of the second set ::", se1.issubset(se2))
print("Returns 'True' if the first set is a subset of the second set ::", se1.issubset(se3))

#inverse of 'issubset' is 'issuperset'

print("\nIs Superset ::")
se1 = {1, 2}
se2 = {1, 2, 3, 4}
se3 = {5}
print("Returns 'True' if the second set is a subset of the first set ::", se2.issuperset(se1))
print("Returns 'True' if the second set is a subset of the first set ::", se3.issuperset(se1))

print("\nSymmetric Difference ::")
se1 = {1, 2}
se2 = {1, 2, 4}
se3 = {5}
print("Returns all the elements that are exactly in one of the sets ::", se1.symmetric_difference(se2))
print("Returns all the elements that are exactly in one of the sets ::", se1.symmetric_difference(se3))
#there is also a 'symmetric_difference_update'

print("\nUnion of two sets ::")
se1 = {1, 2}
se2 = {1, 2, 4}
se3 = {5}
print("Shows the union of two sets ::", se1.union(se2))
print("Shows the union of two sets ::", se1.union(se3))

print("\nUpdate of two sets ::")
se1 = {1, 2}
se2 = {1, 2, 4}
se3 = {5}

print("Example 1 - The first set before update is ::", se1)
print("Example 1 - The second set before update is ::", se2)
se1.update(se2)
print("Example 1 - The first set after update is ::", se1)
print("Example 1 - The second set after update is ::", se2)

print("\nExample 2 - The first set before update is ::", se1)
print("Example 2 - The second set before update is ::", se3)
se1.update(se3)
print("Example 2 - The first set after update is ::", se1)
print("Example 2 - The second set after update is ::", se3)