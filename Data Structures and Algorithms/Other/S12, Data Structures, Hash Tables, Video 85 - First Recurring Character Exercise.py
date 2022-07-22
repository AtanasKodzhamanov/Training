# Given an array of ints, return the first recurring character. Else return undefined.

def recurring(listofints):
    dict={}
    for num in listofints:
        if num in dict:
            return print(num)
        else:
            dict[num]=num
    return print("Undefined")

recurring([2,5,5,6,2,1,0])