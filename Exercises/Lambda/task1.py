#               Lambda Exercises
#               ----------------

#=============================================================================================================

#1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
#also create a lambda function that multiplies argument x with argument y and print the result.
#Sample Output:
#25
#48

#main progra
"""
a=lambda x:x+15
print(a(10))
b=lambda x,y=12:x*y
print(b(4))


#output
25
48"""

#=============================================================================================================

#2. Write a Python program to create a function that takes one argument, and that argument will be multiplied
# with an unknown given number. 
"""Sample Output:
Double the number of 15 = 30
Triple the number of 15 = 45
Quadruple the number of 15 = 60
Quintuple the number 15 = 75"""


#main program
"""
def unknown(number):
    print("Double the number of {} = {}".format(number,number*2))
    print("Trible the number of {} = {}".format(number,number*3))
    print("Quadruple the number of {} = {}".format(number,number*4))
    print("Quintuple the number of {} = {}".format(number,number*5))
unknown(15)

#ouput:
Double the number of 15 = 30
Trible the number of 15 = 45
Quadruple the number of 15 = 60
Quintuple the number of 15 = 75"""

#=============================================================================================================

#3. Write a Python program to sort a list of tuples using Lambda.
#Original list of tuples:
"""[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]"""

#Main Program
"""
lst=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        sort=lambda x=lst[i][-1],y=lst[j][-1]: x if x<y else y
    lst[i],lst[j]=lst[j],lst[i]
print(lst)"""

#output:
#[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

#=============================================================================================================

#4. WAP to sort a list of dictionaries using Lambda.?
#Original list of dictionaries :
#[{'make': 'Nokia', 'model': 216, 'color': 'Black'},
# {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
# {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
#Sorting the List of dictionaries :
#[{'make': 'Nokia', 'model': 216, 'color': 'Black'},
# {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
# {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]

#Main program
"""models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
print("Original list of dictionaries :")
print(models)
sorted_models = sorted(models, key = lambda x: x['color'])
print("\nSorting the List of dictionaries :")
print(sorted_models)"""

#=============================================================================================================

#5. Write a Python program to filter a list of integers using Lambda.?
"""Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]"""

#Main program
"""
lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even=list(filter((lambda i:i%2==0),lst))
print(Even)
Odd=list(filter((lambda i:i%2!=0),lst))
print(Odd)"""
    

#=============================================================================================================

#6. Write a Python program to square and cube every number in a given list of integers using Lambda.?
#Original list of integers:
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Square every number of the said list:
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#Cube every number of the said list:
#[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

#Main Program
"""
lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Square_list=[]
Cube_list=[]
Square=(lambda x:x**2)
Cube=(lambda x:x**3)

for i in lst:
    Square_list.append(Square(i))
    Cube_list.append(Cube(i))
print(Square_list)
print(Cube_list)  """ 

#=============================================================================================================

#7. WAP to find if a given string starts with a given character using Lambda.?
#Sample Output:
#True
#False

#Main Program
"""
str1=input("Enter your string:")
a=lambda x=str1[0]:"True" if x.isalpha() else "False"
print(a())"""

#=============================================================================================================

#8. WAP to extract year, month, date and time using Lambda.?
"""Sample Output:
2020-01-15 09:03:32.744178
2020
1
15
09:03:32.744178"""

#Main Program
"""
str1="2020-01-15 09:03:32.744178"
lst=list(str1.split())
a=lambda i: i
for i in lst[0]:
    if i=="-":
        print()
        continue
    print(a(i),end='')
print()
print(lst[1])"""


#or
"""
import datetime
now = datetime.datetime.now()
print(now)
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()
print(year(now))
print(month(now))
print(day(now))
print(t(now))"""



#=============================================================================================================

#9. WAP to check whether a given string is number or not using Lambda.
"""
Sample Output:
True
True
False
True
False
True
Print checking numbers:
True
True"""
#Main program
"""
str1=input("Enter your string:")
check=lambda x:True if x.isdigit() else False
print(check(str1))"""


#=============================================================================================================

#10. WAP program to create Fibonacci series upto n using Lambda.?

"""Fibonacci series upto 2:
[0, 1]
Fibonacci series upto 5:
[0, 1, 1, 2, 3]
Fibonacci series upto 6:
[0, 1, 1, 2, 3, 5]
Fibonacci series upto 9:
[0, 1, 1, 2, 3, 5, 8, 13, 21]"""

#Main Program
"""
number=int(input("Enter Fibonacci series:"))
t1=0
t2=1
print(t1,end=' ')
print(t2,end=' ')
fib=lambda t1,t2:t1+t2
for i in range(number-2):
    t3=fib(t1,t2)
    print(t3,end=' ')
    t1=t2
    t2=t3"""
    

#=============================================================================================================

#11. Write a Python program to find intersection of two given arrays using Lambda.?
#Original arrays:
#[1, 2, 3, 5, 7, 8, 9, 10]
#[1, 2, 4, 8, 9]
#Intersection of the said arrays: [1, 2, 8, 9]

#Main Program
"""
lst1=[1, 2, 3, 5, 7, 8, 9, 10]
lst2=[1, 2, 4, 8, 9]
for i in lst1:
    for j in lst2:
        a=lambda i,j: i==j
        if a(i,j)==True:
            print(i,end=' ')"""



#=============================================================================================================

#12. WAP to rearrange positive and negative numbers in a given array using Lambda.?
#Original arrays:
#[-1, 2, -3, 5, 7, 8, 9, -10]
#Rearrange positive and negative numbers of the said array:
#[2, 5, 7, 8, 9, -10, -3, -1]

#Main program
"""
lst=[-1, 2, -3, 5, 7, 8, 9, -10]
temp=[]
lst1=list(filter((lambda x:x<0),lst))
lst2=list(filter((lambda x:x>0),lst))
lst1.reverse()
lst2.extend(lst1)
print(lst2)"""

#=============================================================================================================

#13. WAP program to count the even, odd numbers in a given array of integers using Lambda.?
#Original arrays:
#[1, 2, 3, 5, 7, 8, 9, 10]
#Number of even numbers in the above array: 3
#Number of odd numbers in the above array: 5

#Main Program
"""
lst=[1, 2, 3, 5, 7, 8, 9, 10]
Odd_lst=list(filter((lambda x:x if x%2!=0 else False),lst))
Even_lst=list(filter((lambda x:x if x%2==0 else False),lst))
print("count of odd",len(Odd_lst))
print("count of even",len(Even_lst))"""

#=============================================================================================================

#14. WAP to find the values of length six in a given list using Lambda.?
#Sample Output:
#Monday
#Friday
#Sunday

#Main Program
"""
day=input("Enter your day:")
length=lambda x:x if len(x)==6 else False
print(length(day))"""

#=============================================================================================================

#15. WAP to add two given lists using map and lambda.?
#Original list:
#[1, 2, 3]
#[4, 5, 6]
#Result: after adding two list
#[5, 7, 9]

#main program
"""
lst1=[1,2,3]
lst2=[4,5,6]
lst3=[]
merge=lambda x,y:x+y
for i in range(len(lst1)):
    lst3.append(merge(lst1[i],lst2[i]))
print(lst3)"""

#=============================================================================================================

#16. WAP to find the second lowest grade of any student(s) from the given names and grades of each
#student using lists and lambda. Input number of students, names and grades of each student.?
"""
Input number of students: 5
Name: S ROY
Grade: 1
Name: B BOSE
Grade: 3
Name: N KAR
Grade: 2
Name: C DUTTA
Grade: 1
Name: G GHOSH
Grade: 1
Names and Grades of all students:
[['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]
Second lowest grade: 2.0
Names:
N KAR"""

#Main Program
"""
lst=[['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]
Grade=lambda x: x if int(x[1])==2 else False
lst1=[]
for i in range(len(lst)):
    if Grade(lst[i])!=False:
        print(Grade(lst[i]))"""

#=============================================================================================================

#17. WAP to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda. ?
#Orginal list:
#[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
#divisible by nineteen or thirteen:
#[19, 65, 57, 39, 152, 190]

#Main Program
"""
lst=[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
div=lambda x:x if x%19==0 or x%13==0 else False
for i in lst:
    if div(i)!=False:
        print(div(i),end=' ')"""



#=============================================================================================================

#18. WAP to find palindromes in a given list of strings using Lambda.?
#Orginal list of strings:
#['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
#List of palindromes:
#['php', 'aaa']


#Main Program
"""
lst=['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
palin=list(filter((lambda x:x if x==x[::-1] else False),lst))
print(palin)"""

#=============================================================================================================

#19. WAP to find all anagrams of a string in a given list of strings using lambda.?
#Orginal list of strings:
#['bcda', 'abce', 'cbda', 'cbea', 'adcb']
#Anagrams of 'abcd' in the above string:
#['bcda', 'cbda', 'adcb']

#Main Program
"""
lst=['bcda', 'abce', 'cbda', 'cbea', 'adcb']
anagrams=list(filter((lambda x:set(x).issubset("abcd")),lst))
print(anagrams)"""


#=============================================================================================================

#20.WAP to find the numbers of a given string and store them in a list,
#display the numbers which are bigger than the length of the list in sorted
#form. Use lambda function to solve the problem.?

#Original string: sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5
#Numbers in sorted form: 20 23 56

#Main Program
"""
str1="sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
lst=str1.split()
l=len(lst)
sort=list(filter((lambda x:x if x.isdigit() else False),lst))
for i in sort:
    if int(i)>l:
        print(i,end=' ')"""

#=============================================================================================================

#21.WAP that multiply each number of given list with a given number usinglambda function.?

"""Original list: [2, 4, 6, 9, 11]
Given number: 2
Result:
4 8 12 18 22"""

#Main Program
"""
lst=[2, 4, 6, 9, 11]
number=int(input("enter your number:"))
multiply=lambda i:i*number
for i in lst:
    print(multiply(i),end=' ')"""

#=============================================================================================================

#22. WAP that sum the length of the names of a given list of names
# after removing the names that starts with an lowercase letter.Use lambda function.?

#Main Program
"""
str1=input("Enter your sentence:")
lst=str1.split()
s=0
lower=list(filter((lambda x:x if x.istitle() else False),lst))
for i in lower:
    s+=len(i)
print(s)

#output:
Enter your sentence:hi this is Ramesh from Hyderabad
15"""



#=============================================================================================================

#23. WAP to calculate the sum of the positive and negative numbers of a given
# list of numbers using lambda function.?


"""
Original list: [2, 4, -6, -9, 11, -12, 14, -5, 17]
Sum of the positive numbers: -32
Sum of the negative numbers: 48"""

#Main Program
"""
lst=[2, 4, -6, -9, 11, -12, 14, -5, 17]
neg=list(filter((lambda x:x if x<0 else False),lst))
pos=list(filter((lambda x:x if x>0 else False),lst))
print("positive:",sum(pos))
print("negative:",sum(neg))"""


#=============================================================================================================

#24. WAP to find numbers within a given range where every number
# is divisible by every digit it contains.?


"""
Sample Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Click me to see the sample solution"""


"""
def divisible_by_digits(start_num, end_num):
    return [n for n in range(start_num, end_num+1) \
                if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, str(n)))]
print(divisible_by_digits(1,22))"""
#=============================================================================================================

#25. Write a Python program to create the next bigger number by rearranging the digits of a given number. Go to the editor
"""
Original number: 12
Next bigger number: 21
Original number: 10
Next bigger number: False
Original number: 201
Next bigger number: 210
Original number: 102
Next bigger number: 120
Original number: 445
Next bigger number: 454
Click me to see the sample solution"""
#main

"""
def rearrange_bigger(n):
    #Break the number into digits and store in a list
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
n = 12
print("Original number:",n)
print("Next bigger number:",rearrange_bigger(n))

n = 10
print("\nOriginal number:",n)
print("Next bigger number:",rearrange_bigger(n))
      
n = 201
print("\nOriginal number:",n)
print("Next bigger number:",rearrange_bigger(n))
n = 102
print("\nOriginal number:",n)
print("Next bigger number:",rearrange_bigger(n))
n = 445
print("\nOriginal number:",n)
print("Next bigger number:",rearrange_bigger(n))"""
#=============================================================================================================

#26. Write a Python program to find the list with maximum and minimum length using lambda. Go to the editor
"""
Original list:
[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
List with maximum length of lists:
(3, [13, 15, 17])
List with minimum length of lists:
(1, [0])
Click me to see the sample solution

def rearrange_bigger(n):
    #Break the number into digits and store in a list
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
n = 12
print("Original number:",n)
print("Next bigger number:",rearrange_bigger(n))

n = 10
print("\nOriginal number:",n)
print("Next bigger number:",rearrange_bigger(n))
      
n = 201
print("\nOriginal number:",n)
print("Next bigger number:",rearrange_bigger(n))
n = 102
print("\nOriginal number:",n)
print("Next bigger number:",rearrange_bigger(n))
n = 445
print("\nOriginal number:",n)
print("Next bigger number:",rearrange_bigger(n))"""
#=============================================================================================================

#27. Write a Python program to sort each sublist of strings in a given list of lists using lambda. Go to the editor
"""
lst=[['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
a=lambda x : x

for i in lst:
    i.sort()
    print(a(i),end=' ')
#o/p: 
['green', 'orange'] ['black', 'white'] ['black', 'orange', 'white'] 
"""
#=============================================================================================================

#28. Write a Python program to sort a given list of lists by length and value using lambda. Go to the editor
"""
Original list:
[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
Sort the list of lists by length and value:
[[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]
Click me to see the sample solution

def sort_sublists(input_list):
    result = sorted(input_list, key=lambda l: (len(l), l))
    return result
list1 = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
print("Original list:")
print(list1)
print("\nSort the list of lists by length and value:")
print(sort_sublists(list1))"""

#=============================================================================================================

#29. Write a Python program to find the maximum value in a given heterogeneous list using lambda. Go to the editor
"""
Original list:
['Python', 3, 2, 4, 5, 'version']
Maximum values in the said list using lambda:
5

def max_val(list_val):
     max_val = max(list_val, key = lambda i: (isinstance(i, int), i))  
     return(max_val)

list_val = ['Python', 3, 2, 4, 5, 'version'] 
print("Original list:")
print(list_val)
print("\nMaximum values in the said list using lambda:")
print(max_val(list_val))"""

#=============================================================================================================

#30. Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda. Go to the editor
"""
Original Matrix:
[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
Sort the said matrix in ascending order according to the sum of its rows
[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
Original Matrix:
[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
Sort the said matrix in ascending order according to the sum of its rows
[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]


def max_val(list_val):
     max_val = max(list_val, key = lambda i: (isinstance(i, int), i))  
     return(max_val)

list_val = ['Python', 3, 2, 4, 5, 'version'] 
print("Original list:")
print(list_val)
print("\nMaximum values in the said list using lambda:")
print(max_val(list_val))"""

#=============================================================================================================

















