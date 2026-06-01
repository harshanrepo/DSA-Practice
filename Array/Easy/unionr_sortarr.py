def union_arr(arrs1,arrs2,n,m):
    # union=set()

    # for i in range(n):
    #     union.add(arrs1[i])
    
    # for i in range(m):
    #     union.add(arrs2[i])
    # union=list(union)
    # return union

    union=[]

    i=0
    j=0
    while len(arrs1)>i and len(arrs2)>j:
        if arrs1[i] <=arrs2[j]:
            union.append(arrs1.pop(i)) 
            i+=1
            j+=1
    
    for i in arrs1:
        union.append(i)
    for j in arrs2:
        union.append(j)
    return union

arrs1=[1,2,3,4,5]
arrs2=[2,3,4,5,6]
n=5
m=5
print(union_arr(arrs1,arrs2,n,m))