
#                               functions 22-08-2022
#                               ---------------------

#=========================================================================================

#1. What about two asterisks (**)?

"""
* two asterisks (**) is a keyword variable length argument in functions.
* keyword variable length is always taken in the form of dict dataytype.
"""
#examples:

#main program
"""
def simple(**t):
    for i,j in t.items():
        print(i,j**2)
simple(a=12,b=3,c=5)"""

#a 144
#b 9
#c 25

#=========================================================================================

#2.Write a function called fizz_buzz that takes a number.
"""
-If the number is divisible by 3, it should return “Fizz”.
-If it is divisible by 5, it should return “Buzz”.
-If it is divisible by both 3 and 5, it should return “FizzBuzz”.
-Otherwise, it should return the same number.
"""
#main program
"""
number=int(input("enter your number:"))

#function definition
def fizz_buzz(number):
    if (number%3)==0:
        print("Fizz")
    if (number%5)==0:
        print("Buzz")
    if ((number%3)==0 and (number%5)==0):
        print("FizzBuzz")
    else:
        print(number)
#function calling
fizz_buzz(number)

#output:
enter your number:15
Fizz
Buzz
FizzBuzz"""




#=========================================================================================

#3.Write a function called show_Numbers that takes a parameter called limit. It should print all the numbers between 0 and limit
# with a label to identify the even and odd numbers. For example, if the limit is 3, it should print:
"""
-0 EVEN
-1 ODD
-2 EVEN
-3 ODD"""

#main program
"""
limit=int(input("enter your number:"))

#function definition

def Show_Numbers(limit):
    for i in range(limit+1):
        if i%2==0:
            print("{} Even".format(i))
        else:
            print("{} Odd".format(i))
#function calling
Show_Numbers(limit)

#output:
enter your number:3
0 Even
1 Odd
2 Even
3 Odd   """

#=========================================================================================

#4.Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
# For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.

#main program
"""
limit=int(input("enter your number:"))
lst=list()
#function definition

def Sum_Of_multiples(limit):
    for i in range(limit+1):
        if (i%3==0) or (i%5==0):
            lst.append(i)
    return lst
#function calling

for i in Sum_Of_multiples(limit):
    print(i,end=' ')
#output:
enter your number:20
0 3 5 6 9 10 12 15 18 20 """

#=========================================================================================

#5.Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.

#main program
"""
limit=int(input("enter your number:"))
#function definition

def Prime_Numbers(limit):
    for i in range(2,limit):
        for j in range(2,i):
            if i%2==0:
                break
        else:
            print(i,end=' ')
            
#Fucntion calling
Prime_Numbers(limit)

#output:
enter your number:20
2 3 5 7 9 11 13 15 17 19 """

#=========================================================================================

#6.Write a function for checking the speed of drivers. This function should have one parameter: speed.
"""
1.If speed is less than 70, it should print “Ok”.
2.Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the
#total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
3.If the driver gets more than 12 points, the function should print: “License suspended”
"""

##Speed=int(input("enter your number:"))
###function definition
##
##def Prime_Numbers(Speed):
##    if Speed<70:
##        print("Okay")
##    else:
##        if Speed>70:
    


#=========================================================================================

#7. What is the result of “bag” > “apple”?

#=========================================================================================

#8.What is the result of f“{2+2}+{10%3}”?
#=========================================================================================

#9.Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it.
# And also it must return both addition and subtraction in a single return 
#=========================================================================================

#10. Create an inner function to calculate the addition in the following way

"""Create an outer function that will accept two parameters a and b
Create an inner function inside an outer function that will calculate the addition of a and b
At last, an outer function will add 5 into addition and return it.
"""
#=========================================================================================

#11.Write a recursive function to calculate the sum of numbers from 0 to 10

#=========================================================================================

#12. Assign a different name to function and call it through the new name

#=========================================================================================

#13.Generate a Python list of all the even numbers between 4 to 30

#=========================================================================================

#14.Return the largest item from the given list
#=========================================================================================

#15.Create a function showEmployee() in such a way that it should accept employee name, and it’s salary and display both, and if the salary is missing in function call it should show it as 9000


#=========================================================================================
