#=========================================================================================
#1.Calculate income tax for the given income by adhering to the below rules
""" Taxable Income    Rate (in %)
    First $10,000     0
    Next $10,000      10
    The remaining     20
    
Expected Output:

For example, suppose the taxable income is 45000 the income tax payable is

10000*0% + 10000*10%  + 25000*20% = $6000. ? """


##while True:
##    n=int(input("Enter amount:"))
##    if (n>0) and (n<=10000):
##        print("not tax to pay:0")
##    elif (n>10000) and (n<=20000):
##        r=(n-10000)
##        print("your tax will be :",int((10/100)*r))
##    elif (n>20000):
##        r=(n-10000)
##        p=10000
##        t=(r-10000)
##        t1=int((10/100)*p)
##        
##        t2=int((20/100)*t)
##        
##        print("tax will be:",t1+t2)
##    
##Enter amount:10000
##not tax to pay:0
##
##Enter amount:20000
##your tax will be : 1000
##
##Enter amount:35000
##tax will be: 4000
##
##Enter amount:45000
##tax will be: 6000



#=========================================================================================

#2.Count the length of list with out using any inbuilt function.?

##l=[int(x) for x in input().split()]
##c=0
##for i in l:
##    c=c+1
##print("length:",c)
    

#=========================================================================================


#3.Write a Python program to create a histogram from a given list of integers.?




#=========================================================================================

#4. Take input from user and if input is string print String
#if input is integer/float print integer
#if input is mix of string and integer print Error
#HINT Can be done using ASCII code?


##ip=input("enter your word:")
##if type(ip) is str:
##    print("string only")
##elif type(ip) is int:
##    print("Integers only")
##elif typt(ip) is float:
##    print("Float only")
##else:
##    for i  in ip:
##        if 

#=========================================================================================

#5.Python program to check if a string is palindrome or not?

##ip=input("enter word:")
##r=ip[-1::-1]
##if r==ip:
##    print("palindrome")
##else:
##    print("not palindrome")
##
##enter word:Ramesh
##not palindrome

#=========================================================================================
