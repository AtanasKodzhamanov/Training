# Selection sort works by iterating through a list and replacing each value with 
# the smallest value it finds in the rest of the list

unsorted=[100, 40, 60, 10, 0, -40, -200, -30, 1, 2, 3, 4, 5, 6, -5]
unsorted2=[2,0,-2,3]

def SelectionSort(list):
    for i in range(len(list)):
        minValue=list[i]
        minIndex=i
        for j in range (i+1, len(list)):
            if minValue>list[j]:
                minValue=list[j]
                minIndex=j
        # moved=list[i]
        # list[i]=list[temp]
        # list[temp]=moved 
        list[i], list[minIndex] = list[minIndex], list[i]

    print(list)
        
SelectionSort(unsorted)
        