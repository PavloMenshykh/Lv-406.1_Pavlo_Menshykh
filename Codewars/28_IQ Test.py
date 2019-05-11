def iq_test(numbers):
    nmodd = []
    nmeven = []
    nums = numbers.split(" ")

    for nn in nums:
        if int(nn)%2 == 0:
            nmeven.append(nn)
        else:
            nmodd.append(nn)
    if nmodd == [] or nmeven == []:
        return nmodd
    else:
        if len(nmodd)>len(nmeven):
            return(nums.index(nmeven[0])+1)
        else:
            return(nums.index(nmodd[0])+1)

#https://www.codewars.com/kata/552c028c030765286c00007d