class Garden{
    constructor(spaceAvailable){
        this.spaceAvailable=spaceAvailable
        this.plants=[]
        this.storage=[]
    }
    addPlant (plantName, spaceRequired){
        if(spaceRequired>this.spaceAvailable){
            throw new Error("Not enough space in the garden.")
        }
        this.plants.push({plantName,spaceRequired,ripe: false,quantity:0})
        this.spaceAvailable-=spaceRequired
        return `The ${plantName} has been successfully planted in the garden.`
    }
    ripenPlant(plantName, quantity){
        let plantExists=false

        if(quantity<=0){
            throw new Error("The quantity cannot be zero or negative.")
        }

        for(let plant in this.plants){
            if(this.plants[plant].plantName===plantName){
                plantExists=true
                if(this.plants[plant].ripe===true){
                    throw new Error(`The ${plantName} is already ripe.`)
                }
                this.plants[plant].ripe=true
                this.plants[plant].quantity+=quantity

                if(quantity==1){
                    return `${quantity} ${plantName} has successfully ripened.`
                }
                else{
                    return `${quantity} ${plantName}s have successfully ripened.`
                }
            }
        }
        if(plantExists===false){
            throw new Error(`There is no ${plantName} in the garden.`)
        }



    }
    harvestPlant(plantName){
        let plantExists=false
        for(let i in this.plants){
            if(this.plants[i].plantName===plantName){
                plantExists=true        
                if(this.plants[i].ripe===false){
                    throw new Error(`The ${plantName} cannot be harvested before it is ripe.`)
                }
                this.spaceAvailable+=this.plants[i].spaceRequired
                let quantity=this.plants[i].quantity
                this.storage.push({plantName,quantity})
                this.plants.splice(i,1)
                return `The ${plantName} has been successfully harvested.`
            }
        }
        if(plantExists===false){
            throw new Error(`There is no ${plantName} in the garden.`)
        }
    }
    generateReport(){
        const plantAsString = this.plants.map(p=> p.plantName).sort((a,b)=>a.localeCompare(b))
        const plantsRow =`Plants in the garden: ${plantAsString.join(", ")}`
        
        let storageRow="Plants in storage: The storage is empty."
        if(this.storage.length>0){
            const storageAsString=this.storage.map(p=> `${p.plantName} (${p.quantity})`)
            storageRow=`Plants in storage: ${storageAsString.join(`, `)}`
        }
        
        return [
            `The garden has ${ this.spaceAvailable } free space left.`,
            plantsRow,
            storageRow,

        ].join(`\n`)
    }
}

let myGarden = new Garden(250);

myGarden.addPlant("apple", 20)
myGarden.addPlant("orange", 200)
myGarden.addPlant("raspberry", 10)
myGarden.ripenPlant("apple", 10)
myGarden.ripenPlant("orange", 1)
myGarden.harvestPlant("orange")
console.log(myGarden.generateReport())

"The garden has 220 free space left."
"Plants in the garden: apple, raspberry"
"Plants in storage: orange (1)."

"The garden has 220 free space left."
"Plants in the garden: apple, raspberry"
"Plants in storage: orange (1)"