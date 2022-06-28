students = int(input())
lectures = int(input())
bonus = int(input())

maxbonus = 0
maxattendance = 0

for i in range(0, students):
    attendance = int(input())
    totalBonus = attendance / lectures * (5 + bonus)
    if totalBonus > maxbonus:
        maxbonus = totalBonus
        maxattendance = attendance

print(f"Max Bonus: {maxbonus.__ceil__}.")
print(f"The student has attended {maxattendance} lectures.")