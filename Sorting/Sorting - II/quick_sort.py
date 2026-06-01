def quick_sort(a):
    if len(a)<=1:
        return a
    pivot=a[0]
    left=[i for i in a if i < pivot]
    middle=[i for i in a if i == pivot]
    right=[i for i in a if i > pivot]

    return quick_sort(left)+middle+quick_sort(right)

a=[4,6,2,5,7,9,1,3]
print(quick_sort(a))