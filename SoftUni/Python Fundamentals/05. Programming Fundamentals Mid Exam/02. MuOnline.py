health=100
bitcoin=0

rooms=input().split("|")
count=0 

for room in rooms:
    room=room.split()
    item = room[0]
    value = int(room[1])
    count=count+1

    if item=="potion":
        maxheal=100-health
        health=health+value 
        if health>100: 
            health=100
            print(f"You healed for {maxheal} hp.")
        else: 
            print(f"You healed for {value} hp.")
        print(f"Current health: {health} hp.")
    
    elif item=="chest":
        print(f"You found {value} bitcoins.")
        bitcoin+=value

    else:
        health=health-value 
        if health<=0:
            print(f"You died! Killed by {item}.")
            print(f"Best room: {count}")
            break 
        else:
            print(f"You slayed {item}.")
        
if health>0:
    print("You've made it!")
    print(f"Bitcoins: {bitcoin}")
    print(f"Health: {health}")

