#    team-3


#==============================================================================================================================================
"""
1.Python Program to Return the Length of the Longest Word from the List of Words

Problem Description:

The program takes a list of words and returns the word with the longest length.

Runtime Test Cases:

Case 1:
Enter the number of elements in list:4
Enter element1:"Apple"
Enter element2:"Ball"
Enter element3:"Cat"
Enter element4:"Dinosaur"
The word with the longest length is:
Dinosaur
 
Case 2:
Enter the number of elements in list:3
Enter element1:"Bangalore"
Enter element2:"Mumbai"
Enter element3:"Delhi"
The word with the longest length is:
Bangalore

#main program

temp=0
lst=[]
number=int(input("enter your list of elements:"))
for i in range(1,number+1):
    ip=input("enter element{}:".format(i))
    lst.append(ip)
lst1=[]
for i in lst:
    if len(i)>temp:
        temp=len(i)
        lst1.append(i)
print(lst1[-1])"""


 #output:
##enter your list of elements:5
##enter element1:boot
##enter element2:ba
##enter element3:bibal
##enter element4:banana
##enter element5:bun
##banana
##enter your list of elements:3
##enter element1:arun
##enter element2:anjaneya
##enter element3:ram
##anjaneya
    
#==============================================================================================================================================
