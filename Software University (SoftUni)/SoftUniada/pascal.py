numRows = int(input())+1

output = []
new = []
last = []

for i in range(0, numRows):
    new = []
    if i == 0:
        output.append([1])
    else:
        last = output[-1]
        new.append(1)
        for j in range(0, len(last)-1):
            new.append(last[j]+last[j+1])
        new.append(1)
        output.append(new)

print(" ".join(str(num) for num in new))
