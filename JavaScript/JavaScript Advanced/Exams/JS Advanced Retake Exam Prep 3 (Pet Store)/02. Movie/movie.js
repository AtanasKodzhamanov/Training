class Movie{

    constructor(name, price){
        this.movieName=name
        this.ticketPrice=Number(price)
        this.screenings=[]

        this._revenue=0
        this._ticketsSold=0
    }
    newScreening(date, hall, description){
        if (this.screenings.some(s=>s.date==date && s.hall==hall )){
            throw new Error
        }
        
        this.screenings.push({
            date,
            hall,
            description
        })
        return `New screening of ${this.movieName} is added.`
    }
    endScreening(date, hall, tickets){
        const screening=this.screenings.find(s=>s.date==date && s.hall==hall)
        if (screening == undefined){
            throw new Error
        }
        const index=this.screenings.indexOf(screening)
        this.screenings.splice(index,1)
    }
    toString(){
        this.screenings.sort((a,b)=>a.hall.localeCompare(b.hall)).forEach(s=>resultArr.push("afjafj"))
    }
}