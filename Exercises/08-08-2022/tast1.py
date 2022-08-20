
#     SET EXERCISES
#     --------------


#==========================================================================================================

#1.  Add a list of elements to a given set?

##set1=set()
##number=int(input("enter range of number:"))
##for i in range(number):
##    ip=int(input("enter elements:"))   #takig values dynamically from the user
##    set1.add(ip)
##print(set1)


##enter range of number:5
##enter elements:3
##enter elements:5
##enter elements:77
##enter elements:8
##enter elements:0
##{0, 3, 5, 8, 77}

                 
#==========================================================================================================

#2. Return a set of identical items from a given two Python set values?

##A={1,2,3,4}
##B={1,4,5,7,9}

#print(A&B)  #{1,4}

# or

##for i in A:
##    if i in B:
##        print(i)

#{1,4}
#==========================================================================================================

#3.Returns a new set with all items from both sets by removing duplicates?

##A={1,2,3,4}
##B={1,4,5,7,9}

#symmetric_difference

#print(A^B)  #{2, 3, 5, 7, 9}



#==========================================================================================================

#4.Given two Python sets, update first set with items that exist only in the first set and not in the second set.?


##A={1,2,3,4}
##B={1,4,5,7,9}
##
##A.symmetric_difference_update(B)
##
##print(A)


#==========================================================================================================

#5.Remove 10, 20, 30 elements from a following set at once?

##A={10,20,30,40}
##
##B={10,20,30}
##
##print(A-B) #{40}

#==========================================================================================================

#6.Return a set of all elements in either A or B, but not both?

##A={1,2,3,4}
##B={1,4,5,7,9}

##print(A^B)
##{2, 3, 5, 7, 9}
#==========================================================================================================

#7.Determines whether or not the following two sets have any elements in common. If yes display the common elements?


##A={1,2,3,4}
##B={1,4,5,7,9}
##print(A&B)  #{1, 4}



#==========================================================================================================

#8. Update set1 by adding items from set2, except common items?

##A={1,2,3,4}
##B={1,4,5,7,9}

##A.symmetric_difference_update(B)
##print(A)  #{2, 3, 5, 7, 9}

#==========================================================================================================

#9. Remove items from set1 that are not common to both set1 and set2?




#==========================================================================================================

#10.Write a Python program to check if a given set is superset of itself and superset of another given set?

##A={1,2,3,4}
##B={1,4,5,7,9}
##print(A.issuperset(A)) #True
##print(A.issuperser(B)) #True



#==========================================================================================================

#11.Write a Python program to check a given set has no elements in common with other given set?

#==========================================================================================================

#12.Write a Python program to remove the intersection of a 2nd set from the 1st set.?

#==========================================================================================================

#13. Perform all sets methods by taking an example of your own.?



#==========================================================================================================
