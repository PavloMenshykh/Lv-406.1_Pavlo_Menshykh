def count_positives_sum_negatives(arr):
    pos = []
    neg = []
    rslt = []
    
    if arr:
        for x in arr:
            if x>0:
                pos.append(x)
            else:
                neg.append(x)
        if pos.count(0) == len(pos):
            ps = 0
        else:
            ps = len(pos)
            
        rslt.append(ps)
        rslt.append(sum(neg))
        
    return rslt

#https://www.codewars.com/kata/576bb71bbbcf0951d5000044
#Given an array of integers.
#Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.
#If the input array is empty or null, return an empty array.