let {expect} = require("chai")
let movieTheater=require("./movieTheater.js")

describe("movieTheater",()=>{
    describe("ageRestrictions", ()=>{
	    it("test 1",()=>{
            expect(movieTheater.ageRestrictions("G")).to.equal("All ages admitted to watch the movie") 
            expect(movieTheater.ageRestrictions("PG")).to.equal("Parental guidance suggested! Some material may not be suitable for pre-teenagers") 
            expect(movieTheater.ageRestrictions("R")).to.equal("Restricted! Under 17 requires accompanying parent or adult guardian") 
            expect(movieTheater.ageRestrictions("NC-17")).to.equal("No one under 17 admitted to watch the movie") 
            expect(movieTheater.ageRestrictions("Gaffad")).to.equal("There are no age restrictions for this movie") 

        })
    })

    describe("moneySpent", ()=>{
        it("test 2",()=>{
            expect(()=>movieTheater.moneySpent("2",[],[])).to.throw("Invalid input") 
            expect(()=>movieTheater.moneySpent(2,"2",[])).to.throw("Invalid input") 
            expect(()=>movieTheater.moneySpent(2,[],"2")).to.throw("Invalid input") 
        })

        it("test 3",()=>{
            expect(movieTheater.moneySpent(100,["N"],["N"])).to.equal(`The total cost for the purchase with applied discount is 1200.00`)
            expect(movieTheater.moneySpent(4,["Nachos"],["Soda"])).to.equal(`The total cost for the purchase with applied discount is 54.80`)
            expect(movieTheater.moneySpent(4,["Popcorn"],["Soda"])).to.equal(`The total cost for the purchase with applied discount is 53.60`)  
            expect(movieTheater.moneySpent(4,["Popcorn"],["Water"])).to.equal(`The total cost for the purchase with applied discount is 52.80`)  
            expect(movieTheater.moneySpent(4,["Nachos"],["Water"])).to.equal(`The total cost for the purchase with applied discount is 54.00`)  
        })
        it("test 4",()=>{
            expect(movieTheater.moneySpent(0,["N"],["N"])).to.equal(`The total cost for the purchase is 0.00`)
            expect(movieTheater.moneySpent(0,["Nachos"],["Soda"])).to.equal(`The total cost for the purchase is 8.50`)
            expect(movieTheater.moneySpent(0,["Popcorn"],["Soda"])).to.equal(`The total cost for the purchase is 7.00`)  
            expect(movieTheater.moneySpent(0,["Popcorn"],["Water"])).to.equal(`The total cost for the purchase is 6.00`)  
            expect(movieTheater.moneySpent(0,["Nachos"],["Water"])).to.equal(`The total cost for the purchase is 7.50`)  
        })        
    })


    describe("reservation", ()=>{
        it("test 5",()=>{
            expect(()=>movieTheater.reservation("text",2)).to.throw("Invalid input") 
            expect(()=>movieTheater.reservation([{rowNumber: 2, freeSeats:5}],"text")).to.throw("Invalid input") 
            expect(()=>movieTheater.reservation({rowNumber: "2", freeSeats:5},15)).to.throw("Invalid input") 
        })
        
        it("test 6",()=>{
            expect(movieTheater.reservation([{rowNumber: 2, freeSeats:5}],2)).to.deep.equal(2) 
        })        
    })
})