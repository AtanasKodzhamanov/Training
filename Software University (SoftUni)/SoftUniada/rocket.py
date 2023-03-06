n = int(input())
side_size = (n+5)//2
line = ""
# body
body_sides = ((n+5)-3)//2*"_"
body = body_sides + "|||" + body_sides

# tailstart
tail_start_1 = body_sides + "~~~" + body_sides
tail_start_2 = body_sides + "   " + body_sides
top = side_size*"_" + "^" + side_size*"_"
print(top)
second = (side_size-1)*"_" + "/|\\" + (side_size-1)*"_"
print(second)

for i in range(0, n//2+1):
    line = "_" * (side_size-i-2) + "/" + "."*i + "|||" + \
        "."*i + "\\" + "_" * (side_size-i-2)
    if i == n//2-1:
        extra = line
    print(line)
    line = ""

print(extra)
for i in range(0, n):
    print(body)
print(tail_start_1)
for i in range(0, n//2):
    line = "_" * (side_size-i-2) + "//" + "."*i + "!" + \
        "."*i + '\\\\' + "_" * (side_size-i-2)
    print(line)
    line = ""
