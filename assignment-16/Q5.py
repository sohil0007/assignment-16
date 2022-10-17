t1 = tuple([eval(x) for x in input("Enter items :").split(',')])

i=0
e=0
while e<(len(t1)-1):
    if t1[i]!=t1[i+1]:
        print("items are not same")
        break
    e+=1
    i+=1

else:
    print("items are same")    
