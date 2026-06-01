def frequency_counting(s):
    freq={}
    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    return freq

s=[1,2,3,4,1,3]
print(frequency_counting(s))