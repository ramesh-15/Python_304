#                                   Excercise

#=======================================================================================================

#1.With a given integral number n, write a program to generate a dictionary that contains (i, i**3) such that is an integral number between 1 and n (both included).
# and then the program should print the dictionary.
"""output: 1:1  2:8 3:27... depends on the given number"""

#main program
"""
number=int(input("Enter your number:"))
dictionary=dict()
for i in range(1,number+1):
    dictionary[i]=i**3
print(dictionary)

#output
Enter your number:5
{1: 1, 2: 8, 3: 27, 4: 64, 5: 125}"""


#=======================================================================================================

#2. WAP to find hexa format of decimal number, the decimal number is taken from the user
""" ex:- input: 25
        output: 19
          and
          input:5
          output: 5"""

#main program
"""
number=int(input("Enter your number:"))
lst=list(hex(number))
for i in range(2,len(lst)):
    print(lst[i],end='')
#ouput:
Enter your number:25
19"""

#=======================================================================================================

#3.Write a program to merge two string, two string elements taken from the user?
""" input: str1=abr
           str2=ka
    output: akbar    """

#main program
"""
str1=input("Enter your firsr word:")
str2=input("Enter your second word:")
res=''
i,j=0,0
while i<len(str1) and j<len(str2):
    res+=str1[i]
    res+=str2[j]
    i+=1
    j+=1
while i<len(str1):
    res+=str1[i]
    i+=1
while j <len(str2):
    res+=str2[j]
    j+=1
print("Result:{}".format(res))"""

#output:
##Enter your firsr word:abr
##Enter your second word:ka
##Result:akbar
##
##Enter your firsr word:rms
##Enter your second word:aeh
##Result:ramesh
#=======================================================================================================
