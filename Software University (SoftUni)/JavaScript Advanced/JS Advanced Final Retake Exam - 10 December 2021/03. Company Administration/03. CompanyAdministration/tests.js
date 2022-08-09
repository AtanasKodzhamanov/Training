let expect = requre("chai").expect
let companyAdministration=require("./companyAdministration")

describe("companyAdministration",()=>{
    describe("hiringEmployee", ()=>{
        it("test 1",()=>{
            expect(()=>companyAdministration.hiringEmployee("Alex","Programmer",1)).to.throw("We are not looking for workers for this position.")
        })
    })
    describe("calculateSalary", ()=>{
        
    })
    describe("firedEmployee", ()=>{
        
    })
})