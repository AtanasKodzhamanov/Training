
s = "()(()()(()))"
s = input()
stack = []
maxcount = 0
count = 0
flag = False

for i in range(len(s)-1):
    if flag == True:
        flag = False
        continue
    if s[i] == "(" and s[i+1] == ")":
        count += 2
        if count > maxcount:
            maxcount = count
        flag = True
    else:
        count = 0
        flag = False
print(maxcount)
