#               3-Exercises
#               -----------
#======================================================================================================================

#1.WAP to find the senior citizens in the given list,list values should take dynamicaly (or) from the user only.
# suppose list=[23,67,45,89,65,12,15,19], and output:[65,67,89] final list should be in accending order.
# person age is 60 (or) more than 60 belongs to senior citizens.?

##lst=[int(x) for x in input("enter values:").split()]
##lst1=[]
##for i in lst:
##    if i>=60:
##        lst1.append(i)
##else:
##    for i in range(len(lst1)-1):
##        for j in range(i+1,len(lst1)):
##            if lst1[i]>lst1[j]:
##                lst1[i],lst1[j]=lst1[j],lst1[i]
##print(lst1)
##        
##enter values:23 67 45 89 65 12 15 18
##[65, 67, 89]
#======================================================================================================================

#2. WAP to find the diagonal matrix absolute difference?
# suppose  1   2  3
#          7   9  3
#         12   5  67
#result:=>53

#dynamic matrix reading from end user

##col=int(input("enter number of coloumn:"))
##row=int(input("enter number of rows:"))
##lst=[]

##for i in range(1,row+1):
##    lst_inner=[]
##    print("{} row's element's:".format(i))
##    for j in range(1,col+1):
##        ip=int(input("enter {} coloumn:".format(j)))
##        lst_inner.append(ip)
##    lst.append(lst_inner)


    
#first diagonal
##first_dia=list()
##for i in range(len(lst)):
##    for j in range(len(lst[i])):
##            if i==j:
##                first_dia.append(lst[i][j])
##print(first_dia) #[1, 9, 67]
            
#second diagonal
##second_dia=list()
##n=col-1
##for i in range(len(lst)):
##    for j in range(len(lst[i])):
##        if i==j:
##            second_dia.append(lst[i][n])
##            n=n-1
##print(second_dia) #[3, 9, 12]

##print("absolute difference:",abs(sum(first_dia)-sum(second_dia)))

#output:
#--------
##enter number of coloumn:3
##enter number of rows:3
##1 row's element's:
##enter 1 coloumn:1
##enter 2 coloumn:2
##enter 3 coloumn:3
##2 row's element's:
##enter 1 coloumn:7
##enter 2 coloumn:9
##enter 3 coloumn:3
##3 row's element's:
##enter 1 coloumn:12
##enter 2 coloumn:5
##enter 3 coloumn:67

##absolute difference:53


    
        
        

#======================================================================================================================

#3. WAP to solve this pattern
"""  A
     A B
     A B C
     A B C D
     A B C D E
     A B C D
     A B C
     A B
     A         """



##t=4
##for i in range(10):
##    r=65
##    if i<5:
##        for j in range(r,r+i+1):
##            print(chr(j),end=' ')
##        print()
##    elif i>5:
##        
##        for k in range(r,r+t):
##            print(chr(k),end=' ')
##        t-=1
##        print()



##A 
##A B 
##A B C 
##A B C D 
##A B C D E 
##A B C D 
##A B C 
##A B 
##A





