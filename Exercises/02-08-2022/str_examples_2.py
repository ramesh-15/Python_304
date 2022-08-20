"""    Solve without using builtin methods:
"""
#==============================================================================
#1. WAP to print middle charactor of the string?



##str1=input("Enter your word:")
##length=len(str1)//2
##print("Middle of the character is :",str1[length])
##
##
##Enter your word:Ramesh
##Middle of the character is : e
##
##Enter your word:ram
##Middle of the character is : a

#============================================================================="""

#2. WAP to print half reverse of the string?


##str1=input("Enter your word:")
##length=len(str1)//2
##reverse=str1[length-1::-1]
##actual=str1[length::]
##result=reverse+actual
##print("reverse of string is :",result)
##
##Enter your word:Ramesh
##reverse of string is : maResh


#=============================================================================

#3. WAP to remove all the vowels from the given string?

##str1=input("enter your word:")
##lst=list(str1)
##for i in lst:
##    if i in ('aeiou'):
##        lst.remove(i)
##
##temp=''
##for i in lst:
##    temp=temp+i
##print("The result is:",temp)
##        
##enter your word:python is a programming language
##The result is: pythn s  prgrmmng lngag

#=============================================================================

#4. WAP to insert * in front of every vouels in the string.
#Input: BANANA
#Output: B*AN*AN*A


##str1=input("enter your word:")
##lst=list(str1)
##t=[]
##for i in range(0,len(lst)):
##    if lst[i]=="a":
##       
##        t.append('*')
##        t.append(lst[i])
##    else:
##        t.append(lst[i])
##temp=''
##for i in t:
##    temp=temp+i
##print(temp)
##
##
##
##enter your word:banana
##            b*an*an*a
#=============================================================================

#5. WAP to count number of words in the string?

##str1=input("enter your word:")
##lst=str1.split()
##c=0
##for i in lst:
##    c=c+1
##print("total number of words:",c)
##
##
##enter your word:python is a programming language
##total number of words: 5

#=============================================================================

#6. WAP to remove extra space from the given string ?

##str1=input("enter your sentence:")
##print(str1.strip())
##
##enter your sentence:    fjdskjf dfds     
##fjdskjf dfds

#=============================================================================

#7. WAP to insert string in between the given string?


##str1="ojas technology"
##length=len(str1)//2
##str2="innovative"
##lst1=str1.split()
##lst2=str2.split()
##length=len(lst1)//2
##
##lst1.insert(length,lst2)
##
##for i in lst1:
##    if i == []:
##        for j in i:
##            print(j,end=" ")
##    else:
##        print(i,end=' ')


#Input: Ojas technologies 
#Output: Ojas innovative technologies
#=============================================================================

#8. WAP to find the ascci value of given char?

##str1=input("enter word:")
##for i in str1:
##    if i==' ':
##        continue
##    else:
##        print(ord(i),end=' ')

##enter word:a
##97
        
##enter word:abc
##97 98 99 

#=============================================================================

#9. insert ojas in front of every string ?

##str1=input("enter your sentence:")
##lst=[]
##lst=str1.split()
##
##for i in range(0,len(lst),2):
##    #print(i)
##    lst.insert(i,'ojas')
##print(lst)




#=============================================================================

"""
10. insert ojas in every extra space in the string """
