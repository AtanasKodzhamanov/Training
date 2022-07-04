class SummerCamp{
    constructor(organizer, location){
        this.organizer=organizer
        this.location=location
        this.priceForTheCamp = {"child": 150, "student": 300, "collegian": 500}
        this.listOfParticipants=[]
    }

        registerParticipant(name, condition, money) {
        if (!this.priceForTheCamp[condition]){
            throw "Unsuccessful registration at the camp."
        }
        if (name in this.listOfParticipants){
            return `The ${name} is already registered at the camp`
        }
        if (money<this.priceForTheCamp[condition]){
            return `The money is not enough to pay the stay at the camp.`
        }
        else{
            this.listOfParticipants.push({name, condition, power: 100, wins: 0})
            return `The ${name} was successfully registered.`
        }
    }
    unregisterParticipant (name){
        if (!name in this.listOfParticipants){
            return `The ${name} is not registered in the camp.`
        }
        else{
            this.listOfParticipants.pop(name)
            return `The ${name} removed successfully.`
        }
    }
    timeToPlay (typeOfGame, participant1, participant2){
        
    }
}

