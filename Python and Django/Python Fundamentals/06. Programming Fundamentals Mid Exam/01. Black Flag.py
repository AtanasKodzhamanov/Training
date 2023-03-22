
days=int(input())
plunderRate=int(input())
expectedPlunder=int(input())

plunder=0 

for day in range (1, days+1):
    #print(day)
    plunder+=plunderRate
    if day%3==0: 
        plunder+=plunderRate*0.5
    if day%5==0:
        plunder=plunder*0.7
    #print(plunder)

percentage=plunder/expectedPlunder
plunderf="{:.2f}".format(round(plunder,2))
percentagef="{:.2f}".format(round(percentage*100,2))

if plunder>=expectedPlunder:
    print (f"Ahoy! {plunderf} plunder gained.")
else:
    percentage=plunder/expectedPlunder
    print (f"Collected only {percentagef}% of the plunder.")
    