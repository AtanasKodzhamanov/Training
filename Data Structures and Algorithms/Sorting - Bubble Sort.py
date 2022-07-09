
unsorted=[100, 40, 60, 10, 0, -40, -200, -30]

def BubbleSort(list):
    for _ in range(len(list)-1):
        for j in range(0,len(list)-1):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    return print(list)

BubbleSort(unsorted)