statusP = input().split(">")
statusP = [int(i) for i in statusP]

statusW = input().split(">")
statusW = [int(i) for i in statusW]

health = int(input())
loop=True
end=False
while loop==True:
    command = input().split()
    if command[0] == "Retire":
        loop=False

    if command[0] == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if index > len(statusW)-1:
            continue
        else:
            statusW[index] = statusW[index]-damage
        if statusW[index] <= 0:
            print("You won! The enemy ship has sunken.")
            loop=False
            end=True
            break

    elif command[0] == "Defend":
        index1 = int(command[1])
        index2 = int(command[2])
        damage = int(command[3])

        if index1 > len(statusP)-1 or index2 < index1 or index2>len(statusP)-1:
            continue
        for i in range(index1, index2+1):
            statusP[i] = statusP[i]-damage
            if statusP[i] <= 0:
                print("You lost! The pirate ship has sunken.")
                loop=False
                end=True
                break

    elif command[0] == "Repair":
        index = int(command[1])
        repair = int(command[2])
        if index > len(statusP)-1:
            continue
        else:
            statusP[index] = statusP[index]+repair
            if statusP[index] > health:
                statusP[index] = health

    elif command[0] == "Status":
        count = 0
        for i in range(0, len(statusP)):
            if statusP[i] < health*0.2:
                count = count+1
        print(f"{count} sections need repair.")

if end==False:
    pirateShipSum = 0
    warshipSum = 0

    for i in range(0, len(statusP)):
        pirateShipSum += statusP[i]

    for i in range(0, len(statusW)):
        warshipSum += statusW[i]

    print(f"Pirate ship status: {pirateShipSum}")
    print(f"Warship status: {warshipSum}")
