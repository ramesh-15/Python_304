#List Comprehension:

#===================================================================

#1. Find all of the numbers from 1-1000 that are divisible by 7?
"""
lst=[x for x in range(1,1000+1) if x%7==0]
print(lst)

[7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161, 168, 175, 182, 189,
 196, 203, 210, 217, 224, 231, 238, 245, 252, 259, 266, 273, 280, 287, 294, 301, 308, 315, 322, 329, 336, 343, 350, 357,
 364, 371, 378, 385, 392, 399, 406, 413, 420, 427, 434, 441, 448, 455, 462, 469, 476, 483, 490, 497, 504, 511, 518, 525,
 532, 539, 546, 553, 560, 567, 574, 581, 588, 595, 602, 609, 616, 623, 630, 637, 644, 651, 658, 665, 672, 679, 686, 693,
 700, 707, 714, 721, 728, 735, 742, 749, 756, 763, 770, 777, 784, 791, 798,805, 812, 819, 826, 833, 840, 847, 854, 861,
 868, 875, 882, 889, 896, 903, 910, 917, 924, 931, 938, 945, 952, 959, 966, 973, 980, 987, 994]"""
#===================================================================

#2. Find all of the numbers from 1-1000 that have a 3 in them ?

"""
lst=[x for x in range(1,1000+1) if '3' in str(x)]
print(lst)

[3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53, 63, 73, 83, 93, 103, 113, 123, 130, 131, 132, 133, 134, 135, 136,
 137, 138, 139, 143, 153, 163, 173, 183, 193, 203, 213, 223, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 243, 253, 263,
 273, 283, 293, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321,
 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346,
 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371
 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396,
 397, 398, 399, 403, 413, 423, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 443, 453, 463, 473, 483, 493, 503, 513, 523,
 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 543, 553, 563, 573, 583, 593, 603, 613, 623, 630, 631, 632, 633, 634, 635,
 636, 637, 638, 639, 643, 653, 663, 673, 683, 693, 703, 713, 723, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 743, 753,
 763, 773, 783, 793, 803, 813, 823, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 843, 853, 863, 873, 883, 893, 903, 913,
 923, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 943, 953, 963, 973, 983, 993]"""


#===================================================================

#3. Count the number of spaces in a string ?
"""
lst=[x for x in input("enter your sentence:") if ' '==x]
print(len(lst))


enter your sentence:hello hi ramesh how are you there
6

enter your sentence:hello hi ramesh
2"""

#===================================================================

#4. Create a list of all the consonants in the string “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”? 
"""
lst=[x   for x in input("enter your sentence:") if x not in "aeiouAEIOU " ]
print(lst)


['Y', 'l', 'l', 'w', 'Y', 'k', 's', 'l', 'k', 'y', 'l', 'l', 'n', 'g', 'n', 'd', 'y', 'w', 'n',
 'n', 'g', 'n', 'd', 'y', 's', 't', 'r', 'd', 'y', 't', 'h', 'y', 'y', 'd', 'l', 'd', 'w', 'h',
 'l', 't', 'n', 'g', 'y', 'k', 'y', 'y', 'm', 's']  """

#==========================================================================================================================

#5. Get the index and the value as a tuple for items in the list “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’).
#Result would look like (index, value), (index, value) ?



#==============================================================================================================================

#6. Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5? 
"""
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
lst=[x   for x in list_a if x in list_b ]
print(lst)#[2, 3, 4]"""

#==============================================================================================================================

#7. Get only the numbers in a sentence like ‘In 1984 there were 13 instances of a protest with over 1000 people attending’ ?
"""
lst=[x   for x in input("enter your sentence:").split() if x.isdigit() ]
print(lst)
enter your sentence:In 1984 there were 13 instances of a protest with over 1000 people attending
['1984', '13', '1000']"""

#================================================================================================================================


#8. Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even
#and the word ‘odd’ if the number is odd. Result would look like ‘odd’,’odd’, ‘even’ 
"""
number=range(20)
lst=["even" if x%2==0 else "odd" for x in number  ]
print(lst)

['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd',
 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']"""
#==============================================================================================================================


#9 Produce a list of tuples consisting of only the matching numbers in these lists list_a = 1, 2, 3,4,5,6,7,8,9, list_b = 2, 7, 1, 12.
#Result would look like (4,4), (12,12) ?
"""
list_a = [1, 2, 3,4,5,6,7,8,9]
list_b =[ 2, 7, 1, 12]
lst=[(x,x) for x in list_a if x in list_b  ]
print(lst)#[(1, 1), (2, 2), (7, 7)]"""

#================================================================================================================================

#10. Find all of the words in a string that are less than 4 letters?
"""
lst=[x for x in input("enter your sentence:").split() if len(x)<4  ]
print(lst)

enter your sentence:python is a  language how are you there
['is', 'a', 'how', 'are', 'you']"""

#=================================================================================================================================


#11.Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9) ?




#=================================================================================================================================


#12.
#a. Turn every item of a list into its square?
"""
list_a = [1, 2, 3, 4]
lst=[x**2 for x in list_a]
print(lst)#[1, 4, 9, 16]"""


#b. Concatenate two lists index-wise list1 = ["M", "na", "i", "Ke"] & list2 = ["y", "me", "s", "lly"]
#Expected output: ['My', 'name', 'is', 'Kelly'] ?
"""
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
lst=[str(list1[x])+str(list2[x]) for x  in range(len(list1)) ]
print(lst)#['My', 'name', 'is', 'Kelly']"""

#c.list1 = ["Hello ", "take "] & list2 = ["Dear", "Sir"] 
##Expected output: ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

"""
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

lst=[str(list1[i])+str(list2[x]) for x  in range(len(list1))  for i in range(len(list2))]
print(lst)

#output:
    ['Hello Dear', 'take Dear', 'Hello Sir', 'take Sir']"""

#================================================================================================================================

#13.Extend nested list by adding the sublist 

##list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"] 
# sub list to add 

##sub_list = ["h", "i", "j"] 

##Expected Output: 

##['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']



##list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
##sub_list = ["h", "i", "j"]

##lst=list1[2][1][2].extend(sub_list)  
##print(lst)


#================================================================================================================================


#14. Finding Transpose of a Matrix using List Comprehension matrix = [[1, 2], [3,4], [5,6], [7,8]] o/p: [[1, 3, 5, 7], [2, 4, 6, 8]]?

matrix = [[1, 2], [3,4], [5,6], [7,8]]
lt1,lt2=[],[]
lst=[[lt1.append(x) if i.index(x)==0 else lt2.append(x) for x in i] for i in matrix ]
print(lst)


#===================================================================

#15.Reverse each String in a Tuple?
"""
lst=[x for x in input("enter your sentence:").split()]
print(tuple(lst))

enter your sentence:hi ramesh hi
('hi', 'ramesh', 'hi')"""
#===================================================================
