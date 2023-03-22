let { assert, expect } = require("chai");
let flowerShop = require("./flowerShop");

describe("flowerShop", () => {
    describe("calcPriceOfFlowers", () => {
        it("wrongPath", () => {
            expect(() => flowerShop.calcPriceOfFlowers(2, 2, 2)).to.throw("Invalid input!");
            expect(() => flowerShop.calcPriceOfFlowers("2", 2.2, 2)).to.throw("Invalid input!");
            expect(() => flowerShop.calcPriceOfFlowers("2", 2, 2.2)).to.throw("Invalid input!");
            expect(() => flowerShop.calcPriceOfFlowers("2", "2", "2")).to.throw("Invalid input!");
        });
        it("rightPath", () => {
            expect(flowerShop.calcPriceOfFlowers("Flower", 2, 2)).to.equal(`You need $4.00 to buy Flower!`);
           
        });
    });
    describe("checkFlowersAvailable", () => {
        it("available", () => {
            expect(flowerShop.checkFlowersAvailable("Flower", ["Flower","p"])).to.equal(`The Flower are available!`);
            expect(flowerShop.checkFlowersAvailable("Flower",["Flower"])).to.equal(`The Flower are available!`);
        });
        it("unavailable", () => {
            expect(flowerShop.checkFlowersAvailable("Flower", ["Flowesr","p"])).to.equal(`The Flower are sold! You need to purchase more!`);
        });


     });
    describe("sellFlowers", () => { 
        it("invalidPath", () => {
            expect(() => flowerShop.sellFlowers(2, 1)).to.throw("Invalid input!");
            expect(() => flowerShop.sellFlowers(["Flower"], "2f")).to.throw("Invalid input!");
            expect(() => flowerShop.sellFlowers(["Flower"], -2)).to.throw("Invalid input!");
            expect(() => flowerShop.sellFlowers(["Flower"], 1)).to.throw("Invalid input!");
            expect(() => flowerShop.sellFlowers(["Flower"], 2)).to.throw("Invalid input!");
        });
        it("valid", () => {
            expect(flowerShop.sellFlowers(["Flower","p","a"],1)).to.deep.equal(`Flower / a`);
        });
    });
});
