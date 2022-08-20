"""                      Problem statement
                        ------------------

You are required to enter a word that consists of x and y 
that denote the number of Zs and Os respectively. The input word is considered similar to word zoo if 2 * x = y


Determine if the entered word is similar to word zoo.

For example, words such as zzoooo and zzzoooooo are similar to word zoo but not the words such as zzooo and zzzooooo.

Input format

    First line: A word that starts with several Zs and continues by several Os.
    Note: The maximum length of this word must be 20.

    

Output format

Print Yes if the input word can be considered as the string zoo otherwise, print No.

instruction
-----------
if input = zzzoooooo then print "yes".
if input = zzooo print "no". """

while True:
    l=[]
    lt=[]
    x=input("enter  word:")
    if len(x)<20:
        for i in x:
            if 'z'==i:
                l.append(i)
            elif 'o'==i:
                lt.append(i)
        if (len(l)>0) and len(lt)>0:
            if len(l)*2==len(lt):
                print("yes")
            elif len(l)*2!=len(lt):
                print("no")
        else:
            print("no")
    else:
        print("length out of range")
##
##enter  word:zoo
##yes
##enter  word:zzoo
##no
##enter  word:zzzoooooo
##yes
##enter  word:dfdsf
##no
##enter  word:zss
##no










yes
