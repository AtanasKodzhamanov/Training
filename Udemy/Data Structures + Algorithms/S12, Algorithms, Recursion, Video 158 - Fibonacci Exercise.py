def Recursive(n): #O(2^N) exponential time
    if n<2: return n
    return Recursive(n-1)+Recursive(n-2)

def Iterative(n): #O(n)
    seq=[0,1]
    for i in range(1,n+1):
        seq.append(seq[i]+seq[i-1])
    return seq[n]

print(Recursive(42))
print(Iterative(69))