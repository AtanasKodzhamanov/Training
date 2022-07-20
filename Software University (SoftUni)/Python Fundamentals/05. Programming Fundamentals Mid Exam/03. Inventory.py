items=input().split(", ")

while True:
    commands=input().split(" - ")
    if commands[0]=="Craft!": 
        print(", ".join(items))
        break 
    
    command=commands[0]
    item=commands[1]

    if command=="Collect":
        if item not in items:
            items.append(item)
        
    elif command=="Drop":
        if item in items:
            items.remove(item)

    elif command=="Combine Items":
        combineditems=item.split(":")
        if combineditems[0] in items:
            index = items.index(combineditems[0])
            items.insert(index+1,combineditems[1])
            #items[index]="".join(items[index]+":"+combineditems[1])

    elif command=="Renew":
        if item in items:
            items.remove(item)
            items.append(item) 

