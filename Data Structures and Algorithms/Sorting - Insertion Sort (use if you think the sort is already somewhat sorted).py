unsorted=[100, 40, 60, 10, 0, -40, -200, -30, 1, 2, 3, 4, 5, 6, -5]
unsorted2=[2,0,-2,3]

def InsertionSort(list):
    for i in range(1,len(list)):
        num=list[i]

        j = i-1
        while j >=0 and num < list[j]:
                list[j+1] = list[j]
                j -= 1
        list[j+1] = num
    print(list)
        
InsertionSort(unsorted2)