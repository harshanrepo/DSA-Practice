
# Divide and Merge.

def merge_sort(a):
    if len(a)>1:
        mid=len(a)//2
        L=a[:mid]
        R=a[mid:]
        merge_sort(L)
        merge_sort(R)

        a.clear()
        while len(L)>0 and len(R)>0:
            if L[0]>=R[0]:
                a.append(R.pop(0))
            else:
                 a.append(L.pop(0))

        for i in L:
            a.append(i)
        for i in R:
            a.append(i)

    return a

a=[0,2,4,3,1]
print(merge_sort(a))