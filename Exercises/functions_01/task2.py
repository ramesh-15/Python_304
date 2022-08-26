
#  Exercise on function


#================================================================================
"""
1.Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9"""


#Mian program
"""
lst=[int(x) for x in input("enter your elements:").split(',')]
#Function_Definition
def List_Comprehension(lst):
    temp=[x for x in lst if x%2!=0]
    return temp
#Function_Calling
print(List_Comprehension(lst))


#ouptut:
enter your elements:1,5,8,23,2,5
[1, 5, 23, 5]"""

#================================================================================
"""
#2.Write a program that computes the net amount of a bank account based a transaction log from console input.
The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500"""

#Main program
"""
amount=0
#Function_Definition
def Bank_Balance(amount):
    while True:
        print("Menu for Bank services")
        print("=======================")
        print("1.Deposit \n2.withdraw \n3.Balance")
        choice=int(input("Please select your option:"))
        #Deposit
        if choice==1:
            Deposit=int(input("Enter your deposit amount:"))
            amount+=Deposit
            print("RS:{} Credited".format(Deposit))
            ch=input("Do you want to continue(yes/no):")
            if ch=="yes" or ch=="YES":
                Bank_Balance(amount)
            elif ch=="no" or ch=="NO":
                print("Thank you visit again...")
                break
        #withdraw
        elif choice==2:
            Withdraw=int(input("Enter your withdraw amount:"))
            if Withdraw<=amount:
                amount-=Withdraw
                print("RS:{}  Debeted".format(Withdraw))
                ch=input("Do you want to continue(yes/no):")
                if ch=="yes" or ch=="YES":
                    Bank_Balance(amount)
                elif ch=="no" or ch=="NO":
                    print("Thank you visit again...")
                    break
                    
            else:
                print("You don't have sufficient funds to withdraw")
                break
        #Balance
        elif choice==3:
            print("Current balance:",amount)
            ch=input("Do you want to continue(yes/no):")
            if ch=="yes" or ch=="YES":
                Bank_Balance(amount)
            elif ch=="no" or ch=="NO":
                print("Thank you visit again...")
                break
            
#Funcion_Calling
Bank_Balance(amount)
"""

#output:
"""
Menu for Bank services
=======================
1.Deposit 
2.withdraw 
3.Balance
Please select your option:1
Enter your deposit amount:100
RS:100 Credited
Do you want to continue(yes/no):yes
Menu for Bank services
=======================
1.Deposit 
2.withdraw 
3.Balance
Please select your option:2
Enter your withdraw amount:100
RS:100  Debeted
Do you want to continue(yes/no):yes
Menu for Bank services
=======================
1.Deposit 
2.withdraw 
3.Balance
Please select your option:3
Current balance: 0"""
    
        

#================================================================================

#3.You are required to write a program to sort the (name, age, height) tuples by ascending order
# where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
"""
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
"""




#================================================================================

#4.Define a function that can receive two integral numbers in string form and
#compute their sum and then print it in console.

#main program
"""
first_number=input("Enter first number:")
second_number=input("Enter second number:")
#Function_Definition

def Sum_of_string_integral(first_number,second_number):
    return int(first_number)+int(second_number)
print(Sum_of_string_integral(first_number,second_number))

#output:
Enter first number:3
Enter second number:5
8"""

#================================================================================

#5.Define a function that can convert a integer into a string and print it in console.

#main program
"""
first_number=int(input("Enter first number:"))
#Function_Definition

def Sum_of_string_integral(first_number):
    return str(first_number)
#Function-Calling
print(Sum_of_string_integral(first_number))"""

#output:100
#100

#================================================================================

#6.Define a function that can accept two strings as input and print the string
# with maximum length in console. If two strings have the same length, then the function should
# print al l strings line by line.

#main program
"""
first_word=input("Enter first word:")
second_word=input("Enter second word:")
#Function_Definition

def Max-string(first_word,second_word):
    if len(first_word)>len(second_word):
        print("Max :",first_word)
    elif len(first_word)<len(second_word):
        print("Max :",second_word)
    elif len(first_word)==len(second_word):
        print(first_word,"\n",second_word)
#Function_Calling
Max-string(first_word,second_word)"""

#output:
"""
Enter first word:Ramesh
Enter second word:Python
Ramesh 
Python

Enter first word:Ramesh
Enter second word:Naik
Max : Ramesh

Enter first word:Python 
Enter second word:Programming
Max : Programming"""

#================================================================================

#7.Define a function that can accept an integer number as input and print the
# "It is an even number" if the number is even, otherwise print "It is an odd number".?

#main program
"""
Number=int(input("Enter Number:"))

#Function_Definition

def Even_Odd(Number):
    if Number%2==0:
        return 'Even'
    else:
        return 'Odd'
#Function_Calling
print(Even_Odd(Number))

#output:
Enter Number:4
Even
Enter Number:5
odd"""

#================================================================================


#8.Define a function which can print a dictionary where the keys are numbers
# between 1 and 20 (both included) and the values are square of keys.?

#main program
"""
dictionary=dict()
#Function_Definition
def Dictionary_Square(dictionary):
    for i in range(1,20+1):
        dictionary[i]=i**2
    return dictionary
#Function_Calling
print(Dictionary_Square(dictionary))

#output:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100,
 11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 256, 17: 289, 18: 324, 19: 361, 20: 400}"""

#================================================================================

#9.Define a function which can generate a dictionary where the keys are numbers
# between 1 and 20 (both included) and the values are square of keys.
# The function should just print the values only.?


#main program
"""
dictionary=dict()
#Function_Definition
def Dictionary_Values(dictionary):
    for i in range(1,20+1):
        dictionary[i]=i**2
    for i in dictionary.values():
        print(i,end=' ')
#Function_Calling
Dictionary_Values(dictionary)"""

#output:
#1 4 9 16 25 36 49 64 81 100 121 144 169 196 225 256 289 324 361 400
#================================================================================

#10.Define a function which can generate a dictionary where the keys are numbers
#between 1 and 20 (both included) and the values are square of keys. The function should
#just print the keys only.

#main program
"""
dictionary=dict()
#Function_Definition
def Dictionary_keys(dictionary):
    for i in range(1,20+1):
        dictionary[i]=i**2
    for i in dictionary.keys():
        print(i,end=' ')
#Function_Calling
Dictionary_Keys(dictionary)"""

#output:1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 

#================================================================================
#11.Define a function which can generate and print a list where the values are square
# of numbers between 1 and 20 (both included).

#main program
"""
lst=list()
#Function_Definition
def List_Square(lst):
    for i in range(1,20+1):
        lst.append(i**2)
    return lst
#Function_Calling
print(List_Square(lst))"""

#output:
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]

#================================================================================
#12.Define a function which can generate a list where the values are square of numbers
# between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

#main program
"""
lst=list()
#Function_Definition
def List_Square(lst):
    for i in range(1,20+1):
        lst.append(i**2)
    for i in range(5):
        print(lst[i],end=' ')
#Function_Calling
List_Square(lst)"""

#output:
#1 4 9 16 25

#================================================================================

#13.Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included). 

#14.With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line. 

#================================================================================
#15.Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 
#================================================================================

#16.Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 
#================================================================================

#17.Write a program to solve a classic ancient Chinese puzzle: 
#We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

#================================================================================
