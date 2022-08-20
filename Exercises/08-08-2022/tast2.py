
#           Exercises-2
#           -----------



#========================================================================================================================================

#1.WAP which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

##number1=7
##numer2=5
##for i in range(2000,3200+1):
##    if (i%7==0) and (i%5!=0):
##        print(i,end=',')

##2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,2086,2093,2107,2114,2121,2128,2142,2149,2156,2163,2177,
##2184,2191,2198,2212,2219,2226,2233,2247,2254,2261,2268,2282,2289,2296,2303,2317,2324,2331,2338,2352,2359,
##2366,2373,2387,2394,2401,2408,2422,2429,2436,2443,2457,2464,2471,2478,2492,2499,2506,2513,2527,2534,2541,2548,
##2562,2569,2576,2583,2597,2604,2611,2618,2632,2639,2646,2653,2667,2674,2681,2688,2702,2709,2716,2723,2737,2744,
##2751,2758,2772,2779,2786,2793,2807,2814,2821,2828,2842,2849,2856,2863,2877,2884,2891,2898,2912,2919,2926,2933,
##2947,2954,2961,2968,982,2989,2996,3003,3017,3024,3031,3038,3052,3059,3066,3073,3087,3094,3101,3108,3122,3129,
##3136,3143,3157,3164,3171,3178,3192,3199

#========================================================================================================================================

##2.WAP which can compute the factorial of a given numbers.
##The results should be printed in a comma-separated sequence on a single line.
##Suppose the following input is supplied to the program:
##8
##Then, the output should be:
##40320

##num=int(input('ente your number:'))
##f=1
##s=0
##for i in range(1,num+1):   
##    f=f*i
##print(f) #40320
    

#========================================================================================================================================

##3.With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
##Suppose the following input is supplied to the program:
##8
##Then, the output should be:
##{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

##num=int(input('ente your number:'))
##dict={}
##for i in range(1,num+1):
##    dict[i]=(i**2)
##print("result:",dict)

##ente your number:8
##result: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

#========================================================================================================================================

##4.WAP which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
##Suppose the following input is supplied to the program:
##34,67,55,33,12,98
##Then, the output should be:
##['34', '67', '55', '33', '12', '98']
##('34', '67', '55', '33', '12', '98')

##num=input('ente your number:').split(',')
##lst=[]
##tpl=()
##lst=list(num)
##tpl=tuple(num)
##print(lst)
##print(tpl)

##ente your number:34,67,55,33,12,98
##['34', '67', '55', '33', '12', '98']
##('34', '67', '55', '33', '12', '98')

#========================================================================================================================================

##5.Define a class which has at least two methods: getString: to get a string from console input
##printString: to print the string in upper case.Also please include simple test function to test the class methods.

##class Solution():
##    def getString(self):
##        self.a=input("enter your word:")
##    def printString(self):
##        print("Result is :",self.a.upper())
##r=Solution()
##r.getString()
##r.printString()

##enter your word:PythON is a PROGRAMIING langUAGE
##Result is : PYTHON IS A PROGRAMIING LANGUAGE

#========================================================================================================================================

##6.Wap that calculates and prints the value according to the given formula:
##Q = Square root of [(2 * C * D)/H]
##Following are the fixed values of C and H:
##C is 50. H is 30.
##D is the variable whose values should be input to your program in a comma-separated sequence.
##Example
##Let us assume the following comma separated input sequence is given to the program:
##100,150,180
##The output of the program should be:
##18,22,24

##import math

##C,H=50,30
##D=[int(x) for x in input("enter values:").split(',')]
##for i in D:
##    q=math.sqrt((2*C*i)/H)
##    print(int(q),end=',')
    
##enter values:100,150,180
##18,22,24

#========================================================================================================================================

##7.WAP which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
##Note: i=0,1.., X-1; j=0,1,¡­Y-1.
##Example
##Suppose the following inputs are given to the program:
##3,5
##Then, the output of the program should be:
##[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

##row=int(input("enter number of rows:"))
##col=int(input("enter number of cols:"))
##ot=[]  #oter list
##for i in range(row):
##    it=[]  #inner list
##    for j in range(col):
##        it.append(i*j)
##    ot.append(it)
##print(ot)
        
##enter number of rows:3
##enter number of cols:5
##[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

#========================================================================================================================================

##8.WAP that accepts a comma-separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
##Suppose the following input is supplied to the program:
##without,hello,bag,world
##Then, the output should be:
##bag,hello,without,world

##str1=input("enter your word with comma-separate:")
##lst=[]
##lst=str1.split(',')
##lst.sort()
##print(lst)

##enter your word with comma-separate:withour,hello,bag,world
##['bag', 'hello', 'withour', 'world'
                              
        


#========================================================================================================================================


##9.WAP that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
##Suppose the following input is supplied to the program:
##Hello world
##Practice makes perfect
##Then, the output should be:
##HELLO WORLD
##PRACTICE MAKES PERFECT


##while True:
##    str1=input("enter your word :")
##    print(str1.upper())

##enter your word :Hello world
##HELLO WORLD
##enter your word :Practice makes perfect
##PRACTICE MAKES PERFECT

#========================================================================================================================================

##10.WAP that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and
##sorting them alphanumerically.
##Suppose the following input is supplied to the program:
##hello world and practice makes perfect and hello world again
##Then, the output should be:
##again and hello makes perfect practice world.


##string = input("enter your word with comma-separate:")
##lst=[]
##set1=set()
##for i in string.split():
##    if i not in set1:
##        lst.append(i)
##        set1.add(i)
##print(sorted(lst))

"""

   (or)
   
string = input("enter your word with comma-separate:")

lst=[]
lst=string.split()
lst2=[]
for i in lst:
    if i not in lst2:
        lst2.append(i)


print(lst2)

##enter your word with comma-separate:hello world and practice makes perfect and hello world again
##['hello', 'world', 'and', 'practice', 'makes', 'perfect', 'again']"""

##enter your word with comma-separate:hello world and practice makes perfect and hello world again
##['again', 'and', 'hello', 'makes', 'perfect', 'practice', 'world']

#========================================================================================================================================

##11.WAP which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not.
##The numbers that are divisible by 5 are to be printed in a comma separated sequence.
##Example:
##0100,0011,1010,1001
##Then the output should be:
##1010
##Notes: Assume the data is input by console.

##num=input("enter binary  number with comma-seperated:")
##lst=[]
##lst=num.split(',')
##print(lst)  #['0100', '0011', '1010', '1001']
##lst1=[]
##for i in lst:  #['0100', '0011', '1010', '1001']
##    d,c=0,1
##    for j in range(len(i)-1,-1,-1):  #'0100' ==> '0011'  ==>'1010'  ==>'1001'
##        if i[j]=='1':
##            if c==1:
##                d=d+1
##                c+=1
##            elif c==2:
##                d=d+2
##                c=c+1
##            elif c==3:
##                d=d+4
##                c=c+1
##            elif c==4:
##                d=d+8
##                c+=1
##                
##        else:
##            c=c+1
##    else:
##        if d%5==0:
##            print(i)
       
##enter binary  number with comma-seperated:0100,0011,1010,1001
##1010


#========================================================================================================================================


#12.WAP, which will find all such numbers between 1000 and 3000(both included)such that each digit of the number is an even number.
#The numbers obtained should be printed in a comma-separated sequence on a single line.


##for i in range(1000,3000+1):
##    ip=str(i)
##    lt=[]
##    for i in ip:
##        if int(i)%2==0:
##            lt.append(i)
##    else:
##        if len(ip)==len(lt):
##            print(ip,end=',')


##2000,2002,2004,2006,2008,2020,2022,2024,2026,2028,2040,2042,2044,2046,2048,2060,2062,2064,2066,2068,2080,2082,2084,2086,2088,2200,
##2202,2204,2206,2208,2220,2222,2224,2226,2228,2240,2242,2244,2246,2248,2260,2262,2264,2266,2268,2280,2282,2284,2286,2288,2400,2402,
##2404,2406,2408,2420,2422,2424,2426,2428,2440,2442,2444,2446,2448,2460,2462,2464,2466,2468,2480,2482,2484,2486,2488,2600,2602,2604,
##2606,2608,2620,2622,2624,2626,2628,2640,2642,2644,2646,2648,2660,2662,2664,2666,2668,2680,2682,2684,2686,2688,2800,2802,2804,2806,
##2808,2820,2822,2824,2826,2828,2840,2842,2844,2846,2848,2860,2862,2864,2866,2868,2880,2882,2884,2886,2888,

#========================================================================================================================================


##13.WAP that accepts a sentence and calculate the number of letters and digits.
##Suppose the following input is supplied to the program:
##hello world! 123
##Then, the output should be:
##LETTERS 10
##DIGITS 3

##num=input("enter your sentence:")
##lst=[]
##lst=num.split()
##print(lst) #['hello', 'world!', '123']
##al=0
##d=0
##for i in lst:
##    for j in i:
##        if j.isalpha():
##            al+=1
##        elif j.isdigit():
##            d+=1
##print("letter's: {} and digits: {}".format(al,d))

##enter your sentence:hello world! 123
##letter's: 10 and digits: 3

#========================================================================================================================================

##14.WAP that accepts a sentence and calculate the number of upper case letters and lower case letters.
##Suppose the following input is supplied to the program:
##Hello world!
##Then, the output should be:
##UPPER CASE 1
##LOWER CASE 9

##num=input("enter your sentence:")
##lst=[]
##lst=num.split()
##print(lst) #['Hello', 'world!']
##up=0
##lw=0
##for i in lst:
##    for j in i:
##        if j.isupper():
##            up+=1
##        elif j.islower():
##            lw+=1
##print("upper's: {} and lower's: {}".format(up,lw))


##enter your sentence:Hello world!
##['Hello', 'world!']
##upper's: 1 and lower's: 9

#========================================================================================================================================

##15.WAP that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
##Suppose the following input is supplied to the program:
##9
##Then, the output should be:
##11106

##num=int(input("enter your desired  number:"))
##dit=int(input("enter your compute values:"))
##sum1=0
##for i in range(1,dit+1):
##    sum1=sum1+int(str(num)*i)
##print(sum1)
##   


##enter your desired  number:9
##enter your compute values:4
##11106

#========================================================================================================================================

