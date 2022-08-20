

#                           str exmaple
#                           -----------

#================================================================================================
#1. How would you confirm that 2 strings have the same identity?


##str1=input("enter first word:")
##str2=input("Enter second word:")
##
##if len(str1)==1 and len(str2)==1:
##    if id(str1)==id(str2):
##        print("same memory location:True",id(str1),id(str2))
##   
##else:
##    print("Not having same memory:False",id(str1),id(str2))
##
##enter first word:t
##Enter second word:t
##same memory location:True 2515375670576 2515375670576
##
##
##enter first word:python
##Enter second word:python
##Not having same memory:False 2431825636720 2431
##
##enter first word:python
##Enter second word:programming
##Not having same memory:False 2641089162608 2641124300912
#================================================================================================
#2. How would you check if each word in a string begins with a capital letter?


##word=input("Enter your word:")
##for i in word:
##    l=i.split()
##    for j in l:
##        if l[0].title:
##            print(l)
        

#================================================================================================
#3. Check if a string contains a specific substring?

##var1=input("Enter your sentence:")
##var2=input("enter your targeted word:")
##lst1=[]
##lst1=var1.split()
##for i in lst1:
##     if i==var2:
##        print("it contain substring ",i)
##        break
##else:
##    print("no substring")

##Enter your sentence:hi ramesh how are you
##enter your targeted word:jai
##    no substring

##Enter your sentence:hi ramesh how are you
##enter your targeted word:you
##   it contain substring  you

###================================================================================================
###4. Find the index of the first occurrence of a substring in a string?



##var1=input("Enter your sentence:")
##var2=input("enter your targeted word:")
##lst1=[]
##lst1=var1.split()
##for i in lst1:
##     if i==var2:
##        print("it contain substring {} and index {}".format(i,lst1.index(i)))
##        break
##else:
##    print("no substring")
##
##
##Enter your sentence:hi ramesh how are you ramesh
##enter your targeted word:ramesh
##it contain substring ramesh and index 1
##
##Enter your sentence:hi ramesh how are you hi
##enter your targeted word:hi
##it contain substring hi and index 0

#================================================================================================
#5. Count the total number of characters in a string?

##var1=input("Enter your sentence:")
##c=0
##for i in var1:
##    c=c+1
##print("total character is :",c)
##
##Enter your sentence:hi ramesh how are you
##total character is : 21

#================================================================================================

#6. Count the number of a specific character in a string?

##var1=input("Enter your string:")
##var2=input("enter your char:")
##c=0
##for i in var1:
##    if i == var2:
##        c=c+1
##print("total character is :",c)
##
##
##Enter your string:hi ramesh how are you 
##enter your char:h
##total character is : 3

#================================================================================================
#7. Capitalize the first character of a string?

##while True:
##    var1=input("Enter your string:")
##    if var1.istitle():
##        print("yes")
##    else:
##        print("no")
##
##Enter your string:Hai
##yes
##Enter your string:ramesh
##no
    


#================================================================================================
#8. What is an f-string and how do you use it?

##name = 'Tushar'
##age = 23
##print(f"Hello, My name is {name} and I'm {age} years old.")
##
##
##Hello, My name is Tushar and I'm 23 years old.

#================================================================================================
#9. Search a specific part of a string for a substring?

##var1=input("Enter your sentence:")
##var2=input("enter your targeted word:")
##lst1=[]
##lst1=var1.split()
##for i in lst1:
##     if i==var2:
##        print("it contain substring ",i)
##        break
##else:
##    print("no substring")

##Enter your sentence:hi ramesh how are you
##enter your targeted word:jai
##    no substring

##Enter your sentence:hi ramesh how are you
##enter your targeted word:you
##   it contain substring  you

#================================================================================================
#10. Interpolate a variable into a string using format()?

##name = 'Tushar'
##age = 23
##print("Hello, My name is {} and I'm {} years old.".format(name,age)

##Hello, My name is Tushar and I'm 23 years old.

#================================================================================================
#11. Check if a string contains only numbers?

##var1=input("Enter your sentence:")
##
##if var1.isdigit():
##    print("yes it is only digit\s:",var1)
##else:
##    print("no it is not digit\s:",var1)
##
##Enter your sentence:45436546
##yes it is only digit\s: 45436546
##
##Enter your sentence:gdft
##no it is not digit\s: gdft
##
##Enter your sentence:fgre546
##no it is not digit\s: fgre546


#================================================================================================
#12. Split a string on a specific character?

##var1=input("Enter your sentence:")
##lst=[]
##lst=var1.split('u')
##print(lst)
##
##Enter your sentence:gjhuytugsh
##['gjh', 'yt', 'gsh']




#================================================================================================
#13. Check if a string is composed of all lower case characters?

##var1=input("Enter your sentence:")
##if var1.islower():
##    print("yes is lower:",var1)
##else:
##    print("no it  is not lower:",var1)
##
##    
##Enter your sentence:dffsfs
##yes is lower: dffsfs
##
##Enter your sentence:Tsdf
##no it  is not lower: Tsdf

#================================================================================================
#14. Check if the first character in a string is lowercase?

##while True:
##    var1=input("Enter your sentence:")
##    lst=[]
##    lst=var1.split()
##    for i in lst:
##        for j in i:
##            if i[0].islower():
##                print("this is lower of first character:",i)
##                break
##            else:
##                print("this is not lower:",i)
##                break
            

##Enter your sentence:Hi
##this is not lower: Hi
##
##Enter your sentence:hi
##this is lower of first character: hi
##
##Enter your sentence:hi Ramesh how are You NOW
##
##this is lower of first character: hi
##this is not lower: Ramesh
##this is lower of first character: how
##this is lower of first character: are
##this is not lower: You
##this is not lower: NOW

#================================================================================================
#15. Can an integer be added to a string in Python?

# No integer can not add to the strin,because int datatype and string datatype can not cancatinate.
# but we can cancatinate while int datatype convert into str,then only we can cancatinate.


##var1=input("Enter word1:")
##var2=input("enter word2:")
##temp=var1+var2
##print(temp)
##var3=int(input("enter number:"))
##print(temp+(str(var3)))
##
##
##Enter word1:pyt
##enter word2:hon
##python
##enter number:3
##python3

#================================================================================================
#16. Reverse the string “hello world”?

##var=input("enter sentence:")
##for i in range(len(var)-1,-1,-1):
##    print(var[i],end='')
##
##enter sentence:hello world
##   dlrow olleh

#================================================================================================
#17. Join a list of strings into a single string, delimited by hyphens?

##var=input("enter sentence:")
##temp=var.replace(' ','-')
##print(temp)
##
##enter sentence:hi ramesh how are you
##hi-ramesh-how-are-you


#================================================================================================
#18. Check if all characters in a string confirm to ASCI?

##var=input("enter your sentence:")
##for i in var:
##    if i.isalpha():
##        print(ord(i),end=' ')

##enter your sentence:hi ramesh
##104 105 32 114 97 109 101 115 104 

#================================================================================================
#19. Uppercase or lowercase an entire string?

##var=input("enter your word:")
##if var.isupper():
##    print("yes is it upper:",var)
##elif var.islower():
##    print("yes is it lower:",var)
##else:
##    print("combination of both upper and lower:",var)
    

#================================================================================================
#20. Uppercase first and last character of a string?

##var=input("enter your word:")
##l=list(var)
##for i in range(len(var)):
##    if i==0 :
##        l[0]=l[i].upper()
##    elif i==len(var)-1:
##        l[len(var)-1]=l[i].upper()
##for i in l:
##    print(i,end='')
##
##enter your word:ramesh
##RamesH

#================================================================================================
#21. Check if a string is all uppercase?

##var=input("enter your word:")
##if var.isupper():
##    print("yes upper:",var)
##else:
##    print("not upper:",var)
##
##
####enter your word:RAMESH
####yes upper: RAMESH
##
##enter your word:ramesh
##not upper: ramesh

#================================================================================================
#22. When would you use splitlines()?


##var1=input("Enter your sentence:")
##lst=[]
##lst=var1.split('u')
##print(lst)
##
##Enter your sentence:gjhuytugsh
##['gjh', 'yt', 'gsh']


#================================================================================================
#23. Give an example of string slicing?
#var1[ben:end-1:step]

##var1=input("Enter your sentence:")
##print(var1[:3:])
##
##Enter your sentence:ramesh
##ram


#================================================================================================
#24. Convert an integer to a string?

##var1=int(input("Enter your something:"))
##print(str(var1))



#================================================================================================
#25. Check if a string contains only characters of the alphabet?

##var=input("enter your word:")
##if var.isdigit():
##    print("yes is it digit:",var)
##elif var.isalpha():
##    print("yes is it alpha:",var)
##else:
##    print("alphanum:",var)


##enter your word:fsdf454
##yes is it alphanum: fsdf454
    
##enter your word:dsfdg
##yes is it alpha: dsfdg

##enter your word:55565
##yes is it digit: 55565

#================================================================================================
#26. Replace all instances of a substring in a string?



#================================================================================================
#27. Return the minimum character in a string?

#================================================================================================
#28. Check if all characters in a string are alphanumeric?

##var=input("enter your word:")
##if var.isdigit():
##    print("yes is it digit:",var)
##elif var.isalpha():
##    print("yes is it alpha:",var)
##else:
##    print("alphanum:",var)

#================================================================================================
#29. Remove whitespace from the left, right or both sides of a string?

##var=input("enter your word:")
##print(var.strip())
##
##
##enter your word:    ramesh   
##ramesh

#================================================================================================
#30. Check if a string begins with or ends with a specific character?

