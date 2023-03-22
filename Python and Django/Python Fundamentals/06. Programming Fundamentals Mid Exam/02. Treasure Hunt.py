initialLoot = input()
LootList = initialLoot.split("|")
command = ""
count=0

while True:
    count=count+1
    if count>100: break 
    command = input()
    if command == "Yohoho!":
        break

    commandList = command.split()
    CurrentCommand = commandList[0]

    if CurrentCommand == "Loot":
        for i in range(len(commandList)):
            if i == 0:
                continue
            item = commandList[i]
            if item not in LootList:
                LootList.insert(0, item)

    elif CurrentCommand == "Drop":
        index = int(commandList[1])
        if(index>=0 and index <= len(LootList)-1):
            item = LootList[index]
            LootList.remove(item)
            LootList.append(item)
        elif(index<0 and abs(index) <= len(LootList)):
            item = LootList[index]
            LootList.remove(item)
            LootList.append(item)

    elif CurrentCommand == "Steal":
        stolen = []
        n = int(command[1])
        if len(LootList) >= int(commandList[1]):
            for i in range(len(LootList)-int(commandList[1]), len(LootList)):
                stolen.append(LootList[i])
            del LootList[len(LootList)-int(commandList[1]):len(LootList)]
            print(', '.join(stolen))
        else:
            LootList = []


if len(LootList) == 0:
    print("Failed treasure hunt.")
else:
    totalLoot = len(''.join(LootList))
    averageLoot = "{:.2f}".format(totalLoot/len(LootList))
    print(f"Average treasure gain: {averageLoot} pirate credits.")
