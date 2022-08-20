
#    5-Exercises-3





"""
1.write a python program to print the pattern
        * 
       * * 
      * * * 
     * * * * 
    * * * * * 
   * * * * * * 
    * * * * * 
     * * * * 
      * * * 
       * * 
        *"""
##s=6
##t=3
##for i in range(1,6):
##    print(s*" ",end=' ')
##
##    print("* "*i,end=' ')
##    s-=1
##    print()
##    if s==1 and t==3:
##        for i in range(4,0,-1):
##            print(t*" ",end=" ")
##            t+=1
##            print('* '*i,end=' ')
##            print()
##        else:
##            break
    
#================================================================================    
    
##2.How would you check if each word in a string begins with a capital letter?

##str1=input('enter your word:')
##if str1.istitle():
##    print("It\s capital:",str1)
##else:
##    print("It\s not capital:",str1)


##enter your word:program
##It\s not capital: program
##
##enter your word:Program
##It\s capital: Program

###================================================================================   
##3.Write a Python program that prints all the numbers from 0 to 6 except 4 and 5.



##for i in range(6+1):
##    if (i==4) or (i==5):
##        continue
##    else:
##        print(i)

##0
##1
##2
##3
##6



###================================================================================   
##4.Print list of elements and store in a another list and print  reverse order of list?


##lst1=[int(x) for x in input("enter elements:").split()]
##lst2=lst1
##for i in range(len(lst2),0,-1):
##    print(i,end=' ')
##
##enter elements:1 2 3 4 5
##5 4 3 2 1 




###================================================================================   
##5.write a python program to print the pattern
"""         A  
           B C  
          D E F  
         G H I J  
        K L M N O  
       P Q R S T U """

##s=6
##a=65
##for i in range(6):
##    print(s*" ",end=' ')
##    for j in range(i+1):
##        print(chr(a),end=' ')
##        a+=1
##    s-=1
##    print()
        


#          problem statement-team-4
"""
13. Write a Python program to find the strings in a given list, starting with a given prefix.
Input:

[( 'ca',(cat', 'car', 'fear', 'center'))]

Output:

['cat', 'car']

Input:

[(do,('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]

Output:

['dog', 'donut']"""

##while True:
##    lst=[( 'ca',('cat', 'car', 'fear', 'center'))]
##    px=input("enter your prefix character:")
##    def dam(lst):
##        for i in lst:
##            if type(i)==tuple:
##                return dam(i)
##            else:
##                if px in i:
##                    if len(i)>len(px):
##                        print(i)
##    dam(lst)

##enter your prefix character:ca
##cat
##car






       
#================================================================================   
