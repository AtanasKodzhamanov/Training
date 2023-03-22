let expect = requre("chai").expect
let companyAdministration=require("./companyAdministration")

describe("companyAdministration",()=>{
    describe("hiringEmployee", ()=>{
        it("test 1",()=>{
            expect(()=>companyAdministration.hiringEmployee("Alex","Programmer",1)).to.throw("We are not looking for workers for this position.")
            expect(companyAdministration.hiringEmployee("Alex","Programmer",3)).to.equal("expected message")
            expect(companyAdministration.hiringEmployee("Alex","Programmer",5)).to.equal("expected message")
            expect(companyAdministration.hiringEmployee("Alex","Programmer",2)).to.equal("expected message")
        })
    })
    describe("calculateSalary", ()=>{
        it("test 2",()=>{
            expect(companyAdministration.calculateSalary(2)).to.equal(30)
            expect(companyAdministration.calculateSalary(161)).to.equal(3415)
            expect(()=>companyAdministration.calculateSalary(-1)).to.throw("error")
            //the above with "text", [], null
        })
    })
    describe("firedEmployee", ()=>{
        it("test 3 ",()=>{
            expect(()=>companyAdministration.firedEmployee({},1)).to.throw("error")
            //the above with:
                // [],1
                // {},{}
                // ["text","text"],-1
                // ["text","text"], null 
                // ["text","text"], 3 
            expect(companyAdministration.firedEmployee(["4fa","ca","ga"],1)).to.equal(["4fa","ga"])
        })
    })
})