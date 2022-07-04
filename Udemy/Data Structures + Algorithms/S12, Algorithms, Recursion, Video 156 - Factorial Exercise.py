def Recursive (number): #O (n)
    if number==1: # base case
        return 1
    return number*Recursive(number-1)
    
def Iterative (number): #O (n)
    answer=1
    for i in range(2,number+1):
        answer=answer*i
    print(answer)

print(Recursive(5))
Iterative(5)