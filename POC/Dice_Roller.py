"""d={"Front":1,"Up":2,"Down":3,"Left":4,"Right":5,"Back":6}
print("Original position of Roller Dice:")
print(d)
lst=[1,2,3,4,5,6]
while True:
    ch=int(input("enter your Dice Choice:"))  
    for i in lst:
        if i==ch:
            lst.remove(ch)
            lst.insert(0,ch)
    print(lst)
    i=0
    for j in d.keys():
        d[j]=lst[i]
        i+=1
    print("After position of Roller Dice:")
    print(d)
    temp=input("Do you want to continue(yes/no)::")
    if (temp=="no") or (temp=="NO"):
        break"""



d_origin={"Front":1,"Up":5,"Down":6,"Right":2,"Back":3,"Left":4,}
dict_horizontal_right={"Front":1,"Right":2,"Back":3,"Left":4}
#dict_horizontal_left={"Front":1,"Left":2,"Back":3,"Right":4}
dict_vertical={"Front":1,"Up":5,"Back":3,"Down":6}
#dict_vertical_down={"Front":1,"Down":5,"Back":3,"Up":6}
c=0
print("Original position of Roller Dice:")
print(d_origin)
#lst_1=[1,4,3,2]
#lst_2=[1,5,3,6]

while True:
    dice=input("Roll you dice:")
    if dice=="right":
        print(d_origin)
        up=d_origin['Up']
        down=d_origin['Down']
        d_origin.pop("Up")
        d_origin.pop("Down")
       

        lst_1=[]
        for i in d_origin.values():
            lst_1.append(i)
            
        if c==0:
            print(lst_1)
        else:
            last=lst_1[-1]
            lst_1.insert(1,last)
            lst_1.pop()
            print(lst_1)
        
        last=lst_1[-1]
        lst_1.insert(0,last)
        lst_1.pop(-1)

        print(lst_1)  #[4, 1, 2, 3]
       
        
        j=0
        for i in dict_horizontal_right.keys():
            dict_horizontal_right[i]=lst_1[j]
            j+=1
            
        #print(dict_horizontal_right)  #{'Front': 4, 'Left': 1, 'Back': 2, 'Right': 3}
       
        d_origin=dict_horizontal_right
        
        d_origin["Up"]=up
        d_origin['Down']=down
        lst_1=lst_1
        
        print(d_origin)

        
        ch=input("do you want to continue(yes/no):")
        if ch=="NO" or ch=="no":
            break
        
    elif dice=="left":
        up=d_origin['Up']
        down=d_origin['Down']
        d_origin.pop("Up")
        d_origin.pop("Down")

        lst_1=[]
        for i in d_origin.values():
            lst_1.append(i)
        print(lst_1)
        if c==0:
            print(lst_1)
        else:
            last=lst_1[-1]
            lst_1.insert(1,last)
            lst_1.pop(-1)
            print(lst_1)
            
        last=lst_1[0]
        lst_1.insert(len(lst_1),last)
        lst_1.pop(0)

        print(lst_1)  #[4, 1, 2, 3]
       
        
        j=0
        for i in dict_horizontal_right.keys():
            dict_horizontal_right[i]=lst_1[j]
            j+=1
            
        #print(dict_horizontal_right)  #{'Front': 4, 'Left': 1, 'Back': 2, 'Right': 3}
       
        d_origin=dict_horizontal_right
        
        d_origin["Up"]=up
        d_origin['Down']=down
        lst_1=lst_1
        
        print(d_origin)

        
        ch=input("do you want to continue(yes/no):")
        if ch=="NO" or ch=="no":
            break
    elif dice=="up":
        left=d_origin['Left']
        right=d_origin['Right']
        
       
        d_origin.pop("Left")
        d_origin.pop("Right")
        
        print(d_origin)
        lst_1=[]
        for i in d_origin.values():
            lst_1.append(i)
        #back swap to down at first occurence
        if c==0:
            lst_1[-1],lst_1[-2]=lst_1[-2],lst_1[-1]
            c+=1
        
           
        print(lst_1)
        
        last=lst_1[-1]
        lst_1.insert(0,last)
        lst_1.pop()

        print(lst_1)  #[4, 1, 2, 3]
       
        
        j=0
        for i in dict_vertical.keys():
            dict_vertical[i]=lst_1[j]
            j+=1
            
        #print(dict_horizontal_right)  #{'Front': 4, 'Left': 1, 'Back': 2, 'Right': 3}
       
        d_origin=dict_vertical
        
        d_origin["Left"]=left
        d_origin['Right']=right
        lst_1=lst_1
        
        print(d_origin)

        
        ch=input("do you want to continue(yes/no):")
        if ch=="NO" or ch=="no":
            break
    elif dice=="down":
        left=d_origin['Left']
        right=d_origin['Right']
        d_origin.pop("Left")
        d_origin.pop("Right")
        print(d_origin)

        #cross platform
        temp=[]
        for i in d_origin.keys():
            temp.append(i)
    
        lst_1=[]
        for i in d_origin.values():
            lst_1.append(i)
        #same reverse rotate
        if c==0:
            lst_1[-1],lst_1[-2]=lst_1[-2],lst_1[-1]
            c+=1
        elif temp[1]=="Back":
            lst_1[1],lst_1[2]=lst_1[2],lst_1[1]
            
        print(lst_1)
        
        last=lst_1[0]
        lst_1.insert(len(lst_1),last)
        lst_1.pop(0)

        print(lst_1)  #[4, 1, 2, 3]
       
        
        j=0
        for i in dict_vertical.keys():
            dict_vertical[i]=lst_1[j]
            j+=1
            
        print(dict_horizontal_right)  #{'Front': 4, 'Left': 1, 'Back': 2, 'Right': 3}
       
        d_origin=dict_vertical
        
        d_origin["Left"]=left
        d_origin['Right']=right
        lst_1=lst_1
        
        print(d_origin)

        
        ch=input("do you want to continue(yes/no):")
        if ch=="NO" or ch=="no":
            break

    














