eggs=input().split(", ")
eggs= [int(i) for i in eggs]

numbers=input().split(", ")
numbers= [int(i) for i in numbers]

eggs=list(filter(lambda x: x>0, eggs))
box=0

while True:
    if len(eggs)==0 or len(numbers)==0:
        break
    if eggs[0]==13:
        eggs.pop(0)
        front=numbers[0]
        numbers[0]=numbers[len(numbers)-1]
        numbers[len(numbers)-1]=front 
        continue

    if eggs[0]+numbers[len(numbers)-1]<=50: 
        box+=1
    eggs.pop(0)
    numbers.pop(len(numbers)-1)

if box>0:
    print(f"Great! You filled {box} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if len(eggs)>0:
    eggs = [str(digit) for digit in eggs]
    print(f'Eggs left: {", ".join(eggs)}')
if len(numbers)>0:
    numbers = [str(digit) for digit in numbers]
    print(f'Pieces of paper left: {", ".join(numbers)}')

#alternatively
# use deque (from collections import deque)
# eggs = deque(int(x) for x in input().split(", "))
# popleft(), appendleft()