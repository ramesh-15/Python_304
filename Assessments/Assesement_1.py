##Python Programs 
##
##================================================================================================================
#1. Write a program to swap given two numbers without temporary variable?

##first=int(input("enter first number:"))
##second=int(input("Enter second number:"))
##print("before swap:",first,second)
##
##first,second=second,first
##print("after swap:",first,second)

##================================================================================================================

#2. Write a program to accept 4 numbers from command prompt add them using two variables?

##first=int(input("enter first number:"))
##second=int(input("Enter second number:"))
##third=int(input("enter third number:"))
##fourth=int(input("Enter fourth number:"))
##
##add1=first+second+third
##add2=add1+fourth
##print("result:",add2)
##
##
##enter first number:1
##Enter second number:2
##enter third number:3
##Enter fourth number:4
##result: 10

##================================================================================================================
#3. Write a program which accepts an int values as command line argument and    print the next multiple of 100. 

"""
    Ex: Input: 35 

    Output: 100 

    Input: 435 

    Output: 500"""

##n=int(input("enter number:"))
##if len(str(n))==2:
##    print(100)
##else:
##    l=[]
##    while n>0:
##        r=n%10
##        l.append(r)   
##        n=n//10    
##    print((l[len(l)-1]+1)*100)
        
    
##enter number:25
##100
##enter number:435
##500
##enter number:123
##200
    
##================================================================================================================

#4. Write a program ThreeDPalindrome In this program accept a 3 digit integer as a command line argument and return
    #the String true    if the integer is a Palindrome or the String false otherwise?

##n=int(input("enter your number:"))
##t=n
##s=0
##while n>0:
##    r=n%10
##    s=(s*10)+r
##    n=n//10
##if t==s:
##    print("palindrome:",s)
##else:
##    print("Not palindrome:",s)
##
##
##enter your number:121
##palindrome: 121
##
##enter your number:157
##Not palindrome: 751
##================================================================================================================
#5. Write a python program for printing Fibonacci series?


##n=int(input("enter your number:"))
##
##t1=0
##t2=1
##print(t1,end=' ')
##print(t2,end=' ')
##i=0
##n=n-2
##while n>i:
##    t3=t1+t2
##    print(t3,end=' ')
##    t1=t2
##    t2=t3
##    i=i+1
##
##
##enter your number:5
##                0 1 1 2 3
##================================================================================================================

#6. Python Program to Find Armstrong Number in an Interval ?


##n=int(input("enter your number:"))
##
##for i in range(1,n+1):
##    t=0
##    temp=i
##    while i>0:
##
##        r=i%10
##        t=t+(r)**3   #3**3 = 27  5**3=125 1**3=1  27+125+1=153
##        i=i//10
##    if temp==t:
##        print(t,end=' ')
##
##
##enter your number:1000
##1 153 370 371 407 
 
##================================================================================================================

#7. Write a python  program on SumOfDigits, which accepts a two digit number as command line argument and prints the sum of its digits.  

"""
Ex: Input: 35  

Output: 8  

Input: 88  

Output: 16  

  

Note: Do not use Conditional or Looping statements while solving the problem.  """


##n=int(input("Enter your number:"))
##
##s=0
##while n>0:
##    r=n%10
##    s=s+r
##    n=n//10
##print("sum of digit:",s)
##
##Enter your number:66
##sum of digit: 12



##================================================================================================================ 

#8. Write a python program EvenOrOdd, which accepts a whole number as command line argument and prints “Even Number” if the number is Even and 
#prints “Odd Number” if the number is Odd. If the input is not a number, print “Error”.  


##n=int(input("enter number:"))
##
##if n<=0:
##    print("Error")
##elif n%2==0:
##    print("Even:",n)
##else:
##    print("odd :",n)
##
##
##enter number:2
##Even: 2
##enter number:5
##odd : 5
##enter number:0
##Error
##================================================================================================================ 

#9. Write a python program Rounder, which accepts a whole number as command line argument and prints the same number if the input is Odd.
#If the input is even, it should print the next multiple of ten. If the input is not a number or is negative, print the string:“Error”.  

"""
Input: 44, output: 50  

Input: 45, output: 45 """


##n=int(input("enter number:"))
##
##if n<0:
##    print("Error")
##elif  n%2!=0:
##    print("same only :",n)
##elif n%2==0:
##    l=[]
##    while n>0:
##        r=n%10
##        l.append(r)   
##        n=n//10    
##    print((l[len(l)-1]+1)*10)
    
##enter number:44
##    50
##enter number:65
##same only : 65
##enter number:66
##70


##================================================================================================================ 

#10. Write a python program DigitChecker, which accepts a two digit number as command line argument and prints Zero if the digits are same
#and if the two digits are different, it prints their difference.  
"""
Ex: Input: 52  

Output: 3  

Input: 88  

Output: 0  """

##a=int(input("enter first number:"))
##t=a
##l=[]
##while a>0:
##    r=a%10
##    l.append(r)
##    a=a//10
##if l[0]==l[1]:
##    print("same: ",abs(l[0]-l[1]))
##else:
##    print("not same:",abs(l[0]-l[1]))
##
##
##enter first number:55
##same:  0
##
##enter first number:53
##not same: 2

##================================================================================================================
#11. Write a python  program Box, which accepts 2 numbers as command line argument and prints the following output:  
"""
Input: 4 5  

Output:  

 *  *  *  *  *  

 *              *  

 *              *  

 *  *  *  *  *  

NOTE: Output stars must also be separated by a single space.
The first argument is the number of rows and the second argument is the number of columns.
Negative numbers or 0 should print “Error” and come out. Numbers up to 30 must be handled.  """

##n=int(input("enter number:"))
##if n<0:
##    print("Error")
##else:
##    
##    for i in range(1,n+1):
##        for j in range(1,n+1):
##            if (i==1 or i==n) or (j==1 or j==n):
##                print("*",end=' ')
##            else:
##                print(" ",end=' ')
##        print()
##
##
##enter number:5
##
##* * * * * 
##*       * 
##*       * 
##*       * 
##* * * * * 



##================================================================================================================ 

#12.  Write a python program StarPattern, which accepts a number as command line argument and prints the following output:  
"""
Input: 4  

Output:  

*   

*  *   

*  *  *   

*  *  *  *  

NOTE: Output stars must also be separated by a single space. The number of lines must equal the number passed as argument.
Negative numbers or zero should print “Error” and exit. Numbers up to 10 must be handled.  """



##n=int(input("enter number:"))
##if n<0:
##    print("Error")
##else:
##    
##    for i in range(1,n+1):
##        for j in range(1,i+1):
##            print("*",end=' ')
##        print()
##enter number:4
##* 
##* * 
##* * * 
##* * * *     


##================================================================================================================ 

#13. Write a python program NumberPattern4, which accepts a number as command line argument and prints the following output:  


"""
Input: 5  

Output:  

1  

2 4  

3 6 9  

4 8 12 16  

5 10 15 20 25  
  

NOTE: Output numbers must be separated by a single space. The number of lines must equal the number passed as argument.
Negative numbers or zero as input should print “Error” and exit. Numbers up to 10 must be handled.  """


##n=int(input("enter number:"))
##if n<0:
##    print("Error")
##else:
##    
##    for i in range(1,n+1):
##        t=i
##        for j in range(1,i+1):
##            print(i,end=' ')
##            i=t+i
##        print()
##    
##
##enter number:5
##1 
##2 4 
##3 6 9 
##4 8 12 16 
##5 10 15 20 25 



##================================================================================================================
 

#14. Write a python  program on Prime numbers?

##a=int(input("enter  number:"))
##if a>1:
##    
##    for i in range(2,a):
##        if a%i==0:
##            print("not prime:",a)
##            break
##    else:
##        print("prime:",a)
##else:
##    print("number should be more than 1")
##
##
##enter  number:2
##prime: 2
 
##================================================================================================================
#15. Write a python  program on LeastNumber, which accepts two numbers as command line arguments and prints the least number of the two. 
#If the input is not a number, print “Error”.  



a=input("enter first number:")
b=input("Enter second number:")

if (int(a)<int(b)): 
    print("This is least number:",a)
elif (int(b)<int(a)):
    print("This is least number:",b)
else:
    print("Error ")



##enter first number:2
##Enter second number:6
##This is least number: 2
##================================================================================================================
#16. write a python program on finding a Strong number?


##number=int(input("enter a number:"))
##
##t=number
##s=0
##while 0<number:
##
##    rem=number%10
##    f=1
##    for i in range(1,rem+1):
##        f=f*i
##    s=s+f
##    number=number//10
##if (t==s):
##    print("This is strong number:",s)
##else:
##    print("this is not strong number:",s)
##
##
##enter a number:145     5!=120  4!= 24 1!=1  120+24+1=145
##This is strong number: 145
##
##enter a number:124    4!=24 2!=2 1!=1 24+2+1 = 27
##this is not strong number: 27 

##================================================================================================================ 

#17. Python Program to Convert Kilometres to Miles?

""" one km = 0.621 miles"""

##km=int(input("enter  Kilometres:"))
##
##miles=km*(0.621)
##
##print("miles:",miles)


##enter  Kilometres:1
##miles: 0.621


##enter  Kilometres:4
##miles: 2.484
##================================================================================================================
#18. .Problem Statement: Little Robert likes mathematics. Today his teacher has given him two integers and asked to find out how many
#integers can divide both the numbers. Would you like to help him in completing his school assignment? 

"""
Input Formatting: There is two integers, a and b as input to the program. 

Output Formatting: Print the number of common factors of a and b. Both the input value should be in a range of 1 to 10^12. 

Example: 

Input: 10 15 

Output: 2 

Explanation: The common factors of 10 and 15 are 1 and 5. So the answer will be 2"""


##a=int(input("enter first number:"))
##b=int(input("Enter second number:"))
##if a>b:
##    m=a
##else:
##    m=b
##c=0
##for i in range(1,m+1):
##    if (a%i==0) and (b%i==0):
##        c=c+1
##        print(i,end=' ')
##print("The common factors :",c)
##    
##    
##enter first number:10
##Enter second number:15
##The common factors : 2



##================================================================================================================
