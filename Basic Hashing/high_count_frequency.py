def count_frequency(arr):
    freq={}
    for ch in arr:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    for ch in freq:
        if freq[ch]>1:
            return ch
    
arr=[10,1,1,5,1]
print(count_frequency(arr))