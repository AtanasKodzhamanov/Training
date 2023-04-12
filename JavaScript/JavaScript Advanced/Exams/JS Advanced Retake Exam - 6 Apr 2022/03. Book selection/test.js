
let {bookSelection} = require("./bookSelection.js")
let {expect} = requre("chai")

describe("bookSelection",()=>{
    describe("isGenreSuitable", ()=>{
        it("correctInputs",()=>{
                expect(bookSelection.isGenreSuitable("Thriller",12)).to.equal(`Books with ${genre} genre are not suitable for kids at ${age} age`)
                expect(bookSelection.isGenreSuitable("Horror",12)).to.equal(`Books with ${genre} genre are not suitable for kids at ${age} age`)
                })
        })
        it("correctInputs2",()=>{
                expect(bookSelection.isGenreSuitable("Thriller",11)).to.equal(`Books with ${genre} genre are not suitable for kids at ${age} age`) 
                expect(bookSelection.isGenreSuitable("Horror",11)).to.equal(`Books with ${genre} genre are not suitable for kids at ${age} age`)
                })
        it("correctInputs3",()=>{
                expect(bookSelection.isGenreSuitable("Thriller",13)).to.equal(`Those books are suitable`)
                expect(bookSelection.isGenreSuitable("Horror",13)).to.equal(`Those books are suitable`)
                expect(bookSelection.isGenreSuitable("a",13)).to.equal(`Those books are suitable`)
        })
    describe("isItAffordable", ()=>{
        it("invalidInput",()=>{
                expect(()=>bookSelection.isItAffordable("text","text")).to.throw("Invalid input")
                expect(()=>bookSelection.isItAffordable("text",1)).to.throw("Invalid input")
                expect(()=>bookSelection.isItAffordable(1,"text")).to.throw("Invalid input")
                expect(()=>bookSelection.isItAffordable([],1)).to.throw("Invalid input")
                expect(()=>bookSelection.isItAffordable([],[])).to.throw("Invalid input")
                expect(()=>bookSelection.isItAffordable(1,[])).to.throw("Invalid input")
                expect(()=>bookSelection.isItAffordable({},1)).to.throw("Invalid input")
                expect(()=>bookSelection.isItAffordable({},{})).to.throw("Invalid input")
                expect(()=>bookSelection.isItAffordable(1,{})).to.throw("Invalid input")
                expect(()=>bookSelection.isItAffordable(1,undefined)).to.throw("Invalid input")
                expect(()=>bookSelection.isItAffordable(undefined,1)).to.throw("Invalid input")
                expect(()=>bookSelection.isItAffordable(undefined,undefined)).to.throw("Invalid input")
                })
        it("budgetTest",()=>{
                expect(bookSelection.isItAffordable(10,20)).to.equal(`Book bought. You have ${result}$ left`)
                expect(bookSelection.isItAffordable(0,0)).to.equal(`Book bought. You have ${result}$ left`)
                expect(bookSelection.isItAffordable(1,1)).to.equal(`Book bought. You have ${result}$ left`)
                })
        it("budgetTest2",()=>{
                expect(bookSelection.isItAffordable(10.1,10)).to.equal("You don't have enough money")
                expect(bookSelection.isItAffordable(20,10)).to.equal("You don't have enough money")
                })
        })
    describe("suitableTitles", ()=>{
        it("inputError",()=>{
                expect(()=>bookSelection.suitableTitles("text","text")).to.throw("Invalid input")
                expect(()=>bookSelection.suitableTitles("text",1)).to.throw("Invalid input")
                expect(()=>bookSelection.suitableTitles(1,"text")).to.throw("Invalid input")
                expect(()=>bookSelection.suitableTitles([],1)).to.throw("Invalid input")
                expect(()=>bookSelection.suitableTitles([],[])).to.throw("Invalid input")
                expect(()=>bookSelection.suitableTitles("text",[])).to.throw("Invalid input")
                expect(()=>bookSelection.suitableTitles(1,[])).to.throw("Invalid input")
                expect(()=>bookSelection.suitableTitles({},1)).to.throw("Invalid input")
                expect(()=>bookSelection.suitableTitles({},{})).to.throw("Invalid input")
                expect(()=>bookSelection.suitableTitles(1,{})).to.throw("Invalid input")
                expect(()=>bookSelection.suitableTitles(1,undefined)).to.throw("Invalid input")
                expect(()=>bookSelection.suitableTitles(undefined,1)).to.throw("Invalid input")
                expect(()=>bookSelection.suitableTitles(undefined,undefined)).to.throw("Invalid input")
            })

        it("inputError",()=>{
                expect(bookSelection.suitableTitles([{title: "aa", genre:"a"}],"a")).to.deep.equal(["aa"])
        })
        })
        
})