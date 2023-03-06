input = input().split()
sorted = sorted(input, key=lambda x: x*2, reverse=True)
output = ''.join(sorted)
print(output)
