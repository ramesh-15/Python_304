#1.basics on python
"""
1.who invented python?
2.what are the basic steps need to follow to write a program in python?
3. why pep-8 standard  are needed in python?
4.Does python support mobile application?
5. what are the flavours of python

.cpython
.jpython
.ironpython
.rubypython
.pypython  ect


6. disadvantages of python?

1.weak at mobile applicaion
2.


7.what are the companies follows python"""



#2.tokens
"""
1.diff b/w operator and operand

2.python supports constants?

3.what is importance of keywords in python?

4.what is print() statemet?

5.types of literals?

6.what is bitwise operator?

7.WAP to b/w two operands using and operator?


a=10
b=5
1010   and operator
0101
----
1111 ==>15


8.what are the total number of keywords?

35 current version 3.10.5


9.what are the type of operators?

arith
assign
bitwise
relation
logical
identity
membership

10.explain about garbage collector?

11.how memory manage in python?

12.WAP on comparision operator>
a=10
b=23
if a>b:
    print("a big")
else:
    print("b is big")"""
#===============================================================
#3. datatypes
#1. what are the datatpes?
    

#2. importance of datatypes in python?


#3. describe lsit datatypes with example?
""" lst=[1,1,2,3]
    lst.append(5)
    print(lst)"""

#4.what is intersection operation on two sets values?
"""  a={1,2,3}
    b={1,5,6}
    print(a&b) { 1}"""

#5.explain about deep and shallow copy?

#6. WAP to reverse the string of an elements in a given list?
"""
    lst=[1,2,3]
    lst.reverse()
    print(lst)"""
#7. WAP to print "welcome to pyton" by using string?
"""  st="welcome to python"
    print(st)"""
#8. what are the methods in tuple datatype?

#clear()
#count()

#9.can we acces a value in dictionary without a key?
#no

#10.WAP to delete a pair of value in dict?
"""
d={1:2,3:90,5:89}
d.pop(5)
print(d)"""

#11. what are the set methods?
"""
add()
remove()
discard()
pop()
clear()
union()
intersection()
isdisjoint()
issuperset()
issubset()
update()
difference()
symmetric_difference()
difference_update()
symmetric_difference_update()"""

#12. do we perform indexing and slicing on set?


#

#=========================================================================
#4.type conversion

#1. what is mean by type conversion?

#2. how explicit type conversion works?

#3.WAP for implicit type conversion?
"""
a=23
b=4.8
print(a+b) #27.8"""

#4. difference b/w implicit v/s explicit type conversion?


#=========================================================================

#5. flow control statements"
#--------------------------

#1. What do you mean by condition?

#2.what is the difference b/w for v/s while loop?

#3. does "else" statement supports with while?

#yes we can

#example:
"""
i=0
while i<10:
    print(i,end=' ')
    i+=1
else:
    print("program done....")"""

#result:
"""
    0,1,2,3,4,5,6,7,8,9
    program done...."""
    
#4.explain about nested loops?


#5. name any two control statements?
"""
1. if
2.if...else"""

#6.WAP for strong number?
"""
while True:
    number=int(input("enter your number:"))
    s=0
    while number:
        r=number%10
        f=1
        for i in range(1,r+1):
            f=f*i
        s=s+f
        number=number//10
    print(s)
        
enter your number:145
145
enter your number:147
5065
enter your number:143
31"""

#7. what is Enumerator?


#8.WAP to find number prime numbers in the given range(200-300)?

for i in range(200,300+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=' ')
#211 223 227 229 233 239 241 251 257 263 269 271 277 281 283 293


#9. what is placeholder?


#=========================================================================
#6. comprehension:


#1.Define comprehension?

#2. Syntax for list comprehension?

#obj=[expression for obj in iteration condition]

#3. Syntax for dict comprehension?
   

#obj={expression1,expression2 for obj in iteration condition}


#4. Advantages of comprehension?
        





















    
























