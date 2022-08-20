#        Python exercises
#        -----------------
#============================================================================================================================================

#1.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 2000 and 3200 (both included). 

#The numbers obtained should be printed in a comma-separated sequence on a single line.



#============================================================================================================================================
 

#2.Write a program which can compute the factorial of a given numbers. 
"""
The results should be printed in a comma-separated sequence on a single line. 

Suppose the following input is supplied to the program: 

8 

Then, the output should be: 

40320"""

"""
n=int(input("enter your number:"))
f=1
for i in range(1,n+1):
    f=f*i
print(f)

enter your number:8
40320"""



#============================================================================================================================================


#3.With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary. 
"""
Suppose the following input is supplied to the program: 

8 

Then, the output should be: 

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64} 

#main program
number=int(input("enter your number:"))
dict1={}
for i in range(1,number+1):
    dict1[i]=i**2
print(dict1)

#output:
##enter your number:8
##{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}"""


#============================================================================================================================================

#4.Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which
#contains every number. 

"""Suppose the following input is supplied to the program: 

34,67,55,33,12,98 

Then, the output should be: 

['34', '67', '55', '33', '12', '98'] 

('34', '67', '55', '33', '12', '98')

st=input("enter number:")
lst=st.split(',')
print(lst)
print(tuple(lst))

#ouput:
##enter number:34,67,55,33,12,98
##['34', '67', '55', '33', '12', '98']
##('34', '67', '55', '33', '12', '98')"""
#============================================================================================================================================


#5.Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after
#sorting them alphabetically. 
"""
Suppose the following input is supplied to the program: 

without,hello,bag,world 

Then, the output should be: 

bag,hello,without,world

#main program

st1='without,hello,bag,world'
lat=st1.split(',')
for i in sorted(lat):
    print(i,end=' ')

#output:
#bag hello without world"""

#============================================================================================================================================

#6.Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized. 
"""
Suppose the following input is supplied to the program: 

Hello world 

Practice makes perfect 

Then, the output should be: 

HELLO WORLD 

PRACTICE MAKES PERFECT

#main program

st1='Hello world'
st2='Practice makes perfect'
lst1=st1.split(',')
lst2=st2.split(',')
for i in lst1:
    print(i.upper(),end=' ')
print()
for i in lst2:
    print(i.upper(),end=' ')

#output:
HELLO WORLD 
PRACTICE MAKES PERFECT """

#============================================================================================================================================


#7.Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are
#divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence. 
"""
Example: 

0100,0011,1010,1001 

Then the output should be: 

1010 

Notes: Assume the data is input by console. 


st='0100,0011,1010,1001'
lst=st.split(',') #['0100', '0011', '1010', '1001']
for i in lst:
    c=1
    s=0
    for j in range(len(i)-1,-1,-1):
        if i[j]=='1':
            if c==1:
                s=s+1
                c+=1
            elif c==2:
                s=s+2
                c+=1
            elif c==3:
                s=s+4
                c+=1
            elif c==4:
                s=s+8
                c+=1
        else:
            c+=1
    if s%5==0:
        print(i,':',s)  #1010 : 10"""



#============================================================================================================================================

#8.Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. 
"""
Suppose the following input is supplied to the program: 

Hello world! 

Then, the output should be: 

UPPER CASE 1 

LOWER CASE 9 

#main program


st='Hello world!'
uc,lc=0,0
for i in st:
    if i.isupper():
        uc+=1
    elif i.islower():
        lc+=1
print("upper case:",uc)
print("lower case:",lc)

#output:
##upper case: 1
##lower case: 9"""


#============================================================================================================================================

#9.Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.  
"""
Suppose the following input is supplied to the program: 

New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3. 

Then, the output should be: 

2:2 

3.:1 

3?:1 

New:1 

Python:5 

Read:1 

and:1 

between:1 

choosing:1 

or:2 

to:1 """

#main program
"""
st="New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
lst=[]
lst=st.split()
sort=sorted(lst)  #['2', '2', '3.', '3?', 'New', 'Python', 'Python', 'Python', 'Python', 'Python', 'Read', 'and', 'between',  
                  #    'choosing', 'or', 'or', 'to']
st=set()
dic={}
st=sort
for i in st:
    dic[i]=sort.count(i)
for i,j in dic.items():
    print(i,":",j)


2 : 2
3. : 1
3? : 1
New : 1
Python : 5
Read : 1
and : 1
between : 1
choosing : 1
or : 2
to : 1"""    
    

##============================================================================================================================================
##
##10.Convert 2nd Part of String into Upper Case?
"""
lst=[x for x in input("enter your sentence:").split()]
mid=len(lst)//2
print("first half:")
for i in range(mid):
    print(lst[i].lower(),end=' ')
print()
print("second half:")
for i in range(mid,len(lst)):
    print(lst[i].upper(),end=' ')"""


#output
##enter your sentence:Hi Ramesh How Are YOu
##first half:hi ramesh 
##second half:HOW ARE YOU 

#============================================================================================================================================

#11. With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values
#in one line.\

"""
tpl=(1,2,3,4,5,6,7,8,9,10)
mid=len(tpl)//2
print(tpl[:mid])
print(tpl[mid:])"""

#output:
#------
##(1, 2, 3, 4, 5)
##(6, 7, 8, 9, 10)

#============================================================================================================================================
