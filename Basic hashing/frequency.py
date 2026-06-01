def frequency_counting(s,num):
    freq={}
    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    if num in freq:
        return freq[num]
    else:
        return 0

s=[1,2,3,4,1]
print(frequency_counting(s,num=2))