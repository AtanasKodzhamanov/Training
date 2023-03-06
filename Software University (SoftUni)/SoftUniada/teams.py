
n = 12
nums = [14, 15, 8, 9, 11, 13, 10, 12, 9, 8, 15, 14]

# n = int(input())
# nums = [int(x) for x in input().split()]
increasing_stack = []
stack = []
prev = None
# for num in nums:
#     if not increasing_stack:
#         increasing_stack.append(num)
#     else:
#         prev = None
#         for i in range(len(increasing_stack)-1, -1, -1):
#             if increasing_stack[i] < num:
#                 prev = increasing_stack[i]
#                 break
#         if prev is not None:
#             increasing_stack = increasing_stack[:i+1] + [num]
#         else:
#             increasing_stack.append(num)
# prev = None
stack = []


n = int(input())
nums = [int(x) for x in input().split()]
lis = [1] * n

for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            lis[i] = max(lis[i], lis[j] + 1)

max_lis_length = max(lis)
max_lis = []
for i in range(n-1, -1, -1):
    if lis[i] == max_lis_length:
        max_lis.append(nums[i])
        max_lis_length -= 1
        if max_lis_length == 0:
            break

max_lis.reverse()

n = len(nums)
lds = [1] * n

for i in range(1, n):
    for j in range(i):
        if nums[i] < nums[j]:
            lds[i] = max(lds[i], lds[j] + 1)

max_lds_length = max(lds)
max_lds = []
for i in range(n-1, -1, -1):
    if lds[i] == max_lds_length:
        max_lds.append(nums[i])
        max_lds_length -= 1
        if max_lds_length == 0:
            break

max_lds.reverse()

print(n - len(max_lis) - len(max_lds))
