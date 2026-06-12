def count_frequency(arr):
    freq={}
    for ch in arr:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    return freq

arr=[10,5,10,15,10,5]
print(count_frequency(arr))