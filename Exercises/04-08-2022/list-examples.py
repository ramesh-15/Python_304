#            list examples
#            --------------


#=====================================================================================================

#1.Take 10 integer inputs from user and store them in a list and print them on screen.


##lst=[]
##i=1
##while i<=10:
##    element=int(input("enter {} element:".format(i)))
##    lst.append(element)
##    i+=1
##print(lst)
   
###output:
#--------

##enter 1 element:34
##enter 2 element:56
##enter 3 element:15
##enter 4 element:36
##enter 5 element:25
##enter 6 element:15
##enter 7 element:02
##enter 8 element:15
##enter 9 element:89
##enter 10 element:41
##[34, 56, 15, 36, 25, 15, 2, 15, 89, 41]

#=====================================================================================================

##2.Take 10 integer inputs from user and store them in a list. Again ask user to give a number.
##Now, tell user whether that number is present in list or not.
##( Iterate over list using while loop ).


##lst=[]
##i=1
##while i<=10:
##    element=int(input("enter {} element:".format(i)))
##    lst.append(element)
##    i+=1
##number=int(input("enter number:"))
##t=0
##while t<len(lst):
##    if number==lst[t]:
##        print("present")
##        break
##    t+=1
##else:
##    print("Not present")

###output:
#--------
    
##enter 1 element:1
##enter 2 element:2
##enter 3 element:3
##enter 4 element:6
##enter 5 element:5
##enter 6 element:4
##enter 7 element:9
##enter 8 element:8
##enter 9 element:7
##enter 10 element:10
##enter number:5
##present


##enter 1 element:5
##enter 2 element:6
##enter 3 element:32
##enter 4 element:6
##enter 5 element:5
##enter 6 element:24
##enter 7 element:56
##enter 8 element:98
##enter 9 element:74
##enter 10 element:569
##enter number:100
##Not present

#=====================================================================================================

##3.Take 20 integer inputs from user and print the following:
##number of positive numbers.
##number of negative numbers.
##number of odd numbers.
##number of even numbers.
##number of 0s.

##lst=[int(x) for x in input("enter number:").split()]
##p,n,e,o,z=[],[],[],[],[]
##for i in lst:
##    if i>0:
##        if i%2!=0:
##            o.append(i)
##        elif i%2==0:
##            e.append(i)
##        p.append(i)
##    elif i<0:
##        n.append(i)
##    
##    else:
##        z.append(i)
##print(p,n,e,o,z)

###output:
#--------

##enter number:0 1 2 3 4 5 -6 -9 
##[1, 2, 3, 4, 5] [-6, -9] [2, 4] [1, 3, 5] [0]

#=====================================================================================================

##4.Take 10 integer inputs from user and store them in a list. Now,
##copy all the elements in another list but in reverse order.


##lst1=[int(x) for x in input("enter number:").split()]
##lst2=lst1
##print("reverse:")
##for i in range(len(lst2)-1,-1,-1):
##    print(lst2[i],end=' ')
##
##enter number:5 4 2 9 1 6 3 7
## reverse:           7 3 6 1 9 2 4 5

#=====================================================================================================

#5.Write a program to find the sum of all elements of a list.

##lst1=[int(x) for x in input("enter number:").split()]
##sum1=0
##for i in lst1:
##    sum1+=i
##print("sum of all elements in list:{0}".format(sum1))
##
##
##enter number:1 2 3
##sum of all elements in list:6

#=====================================================================================================

#6.Write a program to find the product of all elements of a list.

##product1=1
##lst1=[int(x) for x in input("enter number:").split()]
##for i in lst1:
##    product1*=i
##print("product1 of all elements in list:{0}".format(product1))
##
##enter number:1 2 3 4
##product1 of all elements in list:24

#=====================================================================================================

#7.Initialize and print each element in new line of a list inside list.

##n=5
##lst=[1,2,[3,[4,[5,6],7],9,34],100]


""" reading nested list dynamically
for i in range(n):
    ip=input("enter inner:")
    if ' ' in ip:
        lt=[]
        j=ip.split()
        for k in j:
            lt.append(int(k))
        lst.append(lt)
        
    else:
        
        lst.append(int(ip))
    
"""
#print(lst)
##def sample(lst):
##    for i in lst:
##        if type(i)==list:
##            sample(i)
##        else:
##            print(i)
##sample(lst)
    
##enter inner:100 200
##enter inner:1
##enter inner:100
##enter inner:2 3 5
##enter inner:7
##[[100, 200], 1, 100, [2, 3, 5], 7]
##100
##200
##1
##100
##2
##3
##5
##7

#=====================================================================================================

#8.Find largest and smallest elements of a list.

##lst1=[int(x) for x in input("enter number:").split()]
##for i in range(len(lst1)-1):
##    for j in range(i+1,len(lst1)):
##        if lst1[i]>lst1[j]:
##            lst1[i],lst1[j]=lst1[j],lst1[i]
##print("max:{} and min: {}".format(lst1[-1],lst1[0]))
##
##
##enter number:4 7 9 3 56 7 9
##max:56 and min: 3

#=====================================================================================================

#9.Write a program to print sum, average of all numbers, smallest and largest element of a list.

##lst1=[int(x) for x in input("enter number:").split()]
##for i in range(len(lst1)-1):
##    for j in range(i+1,len(lst1)):
##        if lst1[i]>lst1[j]:
##            lst1[i],lst1[j]=lst1[j],lst1[i]
###
##sum1=0
##for i in lst1:
##    sum1+=i
##print("sum: {}, avg: {}, smallest:{}, and largest:{}".format(sum1,(sum1//len(lst1)),lst1[-1],lst1[0]))
##
##enter number:5 2 7 9 4
##sum: 27, avg: 5, smallest:9, and largest:2

#=====================================================================================================

##10.Write a program to check if elements of a list are same or not it read from front or back.
##E.g.-  2	3	15	15	3	2

##lst=[int(x) for x in input("enter number:").split()]
##length=len(lst)//2
##lst1=lst[:length] 
##lst2=lst[length:]
##lst2.reverse()
##i=0
##while i<len(lst1):
##    if lst1[i]!=lst2[i]:
##        print('difference...')
##        break
##    i+=1
##else:
##    print(lst)

            
##enter number:2 3 15 15 3 2
##[2, 3, 15, 15, 3, 2]
##            
##enter number:1 2 3 3 2 5
##difference...
#=====================================================================================================


##11.Take a list of 10 elements. Split it into middle and store the elements in two dfferent lists. E.g.-
##INITIAL list :
##58	24	13	15	63	9	8	81	1	78

##After spliting :
##58	24	13	15	63
##9	8	81	1	78


##lst=[int(x) for x in input("enter number:").split()]
##print("before:",lst)
##length=len(lst)//2
##lst1=lst[:length]
##lst2=lst[length:]
##print("first half spliting:")
##for i in lst1:
##    print(i,end=' ')
##print()
##print("second half spliting:")
##for i in lst2:
##    print(i,end=' ')


    
##enter number:1 5 7 89 4 3 6 7 9
##before: [1, 5, 7, 89, 4, 3, 6, 7, 9]
##first half spliting:
##                    1 5 7 89
##second half spliting:
##                    4 3 6 7 9

#=====================================================================================================

#12. Ask user to give integer inputs to make a list. Store only even values given and print the list.

##lst=[int( x) for x in input("enter number's:").split() ]
##print(lst)
##print("even values :")
##for i in lst:
##    if i%2==0:
##        print(i,end=' ')
##
##enter number's:1 2 3 4 5 6 7 8 9 10
##[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##even values : 2 4 6 8 10 







#=====================================================================================================
