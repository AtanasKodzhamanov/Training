class Triathlon{

    constructor(competitionName){
        this.competitionName=competitionName
        this.participants={}
        this.listOfFinalists=[]
    }

    addParticipant (participantName, participantGender){

        if (this.participants[participantName]) {
            return (`${participantName} has already been added to the list`);
        }
        else {
            this.participants[participantName] = participantGender
            return `A new participant has been added - ${participantName}`
        }
    }
    completeness (participantName, condition){
        if (!this.participants[participantName]) {
            throw new Error (`${participantName} is not in the current participants list`);
        }
        if(Number(condition)<30){
            throw new Error (`${participantName} is not well prepared and cannot finish any discipline`);
        }
        let num=Number((Number(condition)/30).toFixed(0))
        if(num<=2){
           return `${participantName} could only complete ${num} of the disciplines`
        }
        let finalistGender=this.participants[participantName]
        this.listOfFinalists.push({participant: participantName, gender: finalistGender})
        delete this.participants[participantName]
        return `Congratulations, ${participantName} finished the whole competition`
    }
    rewarding (participantName){
        let exists=false
        for(let i in this.listOfFinalists){
            
            if(this.listOfFinalists[i].participant ==participantName){
               exists=true 
            }
        }
        if(exists==true){
            return `${participantName} was rewarded with a trophy for his performance`
        }
        return (`${participantName} is not in the current finalists list`);
    }

    showRecord (criteria){
        let returnArr=[]
        
        if(this.listOfFinalists.length==0){
            return `There are no finalists in this competition`
        }
        if(criteria=="all"){
            returnArr.push(`List of all ${this.competitionName} finalists:`)
            const allSorted = this.listOfFinalists.map(p=> p.participant).sort((a,b)=>a.localeCompare(b))
            for(let i in allSorted){
                returnArr.push(allSorted[i])
            }
            return returnArr.join("\n")
        }

        let filtered=[]
        filtered=this.listOfFinalists.filter(x=>x.gender===criteria)
        
        if(filtered.length==0){
           return `There are no ${criteria}'s that finished the competition`
        }
        return `${filtered[0].participant} is the first ${criteria} that finished the ${this.competitionName} triathlon`
        
    }
}

const contest = new Triathlon("Dynamos");
console.log(contest.addParticipant("Peter", "male"));
console.log(contest.addParticipant("Sasha", "female"));
console.log(contest.addParticipant("George", "male"));
console.log(contest.completeness("Peter", 100));
console.log(contest.completeness("Sasha", 90));
console.log(contest.completeness("George", 95));
console.log(contest.rewarding("Peter"));
console.log(contest.rewarding("Sasha"));
console.log(contest.rewarding("George"));
console.log(contest.showRecord("male"));

