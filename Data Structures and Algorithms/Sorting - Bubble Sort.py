
unsorted=[100, 40, 60, 10, 0, -40, -200, -30, 1, 2, 3, 4, 5, 6, -5]

def BubbleSort(list):
    for i in range(0,len(list)):
        for j in range(0,len(list)-1):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    return print(list)

BubbleSort(unsorted)