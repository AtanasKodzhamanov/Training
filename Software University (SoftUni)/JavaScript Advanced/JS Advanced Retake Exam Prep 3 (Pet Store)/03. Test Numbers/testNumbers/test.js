const testNumbers = require("./testNumbers");
const { expect } = require("chai");

describe("testNumbers", () => {
  describe("sumNumber", () => {
    it("test 1", () => {
      expect(testNumbers.sumNumbers("text", "text")).to.equal(undefined);
    });
    it("test a", () => {
      expect(testNumbers.sumNumbers("text", 1)).to.equal(undefined);
    });
    it("test b", () => {
      expect(testNumbers.sumNumbers(2, "text")).to.equal(undefined);
    });
    it("test c", () => {
      expect(testNumbers.sumNumbers(2, [])).to.equal(undefined);
    });
    it("test c", () => {
      expect(testNumbers.sumNumbers()).to.equal(undefined);
    });
    it("test ", () => {
      expect(testNumbers.sumNumbers([], [])).to.equal(undefined);
    });
    it("test ", () => {
      expect(testNumbers.sumNumbers({}, [])).to.equal(undefined);
    });
    it("test 2", () => {
      expect(testNumbers.sumNumbers(1, 1)).to.equal("2.00");
      expect(testNumbers.sumNumbers(-1, -1)).to.equal("-2.00");
      expect(testNumbers.sumNumbers(-1, 1)).to.equal("0.00");
      expect(testNumbers.sumNumbers(1.2, 1.2)).to.equal("2.40");
      expect(testNumbers.sumNumbers(2.0, 0.222)).to.equal("2.22");
      expect(testNumbers.sumNumbers(1.5555, 0.3333)).to.equal("1.89");
    });
  });
  describe("numberChecker", () => {
    it("test 3", () => {
      expect(() =>
        testNumbers.numberChecker("text").to.throw("The input is not a number!")
      );
      expect(() =>
        testNumbers.numberChecker([]).to.throw("The input is not a number!")
      );
      expect(() =>
        testNumbers.numberChecker(true).to.throw("The input is not a number!")
      );
      expect(() =>
        testNumbers.numberChecker("").to.throw("The input is not a number!")
      );
      expect(() =>
        testNumbers.numberChecker().to.throw("The input is not a number!")
      );
      expect(() =>
        testNumbers.numberChecker({}).to.throw("The input is not a number!")
      );
      expect(() =>
        testNumbers.numberChecker("a").to.throw("The input is not a number!")
      );
      expect(() =>
        testNumbers
          .numberChecker(undefined)
          .to.throw("The input is not a number!")
      );
      expect(() =>
        testNumbers.numberChecker(2.141).to.throw("The input is not a number!")
      );
      expect(() =>
        testNumbers
          .numberChecker("2.141")
          .to.throw("The input is not a number!")
      );
    });
    it("test 4", () => {
      expect(testNumbers.numberChecker(2)).to.equal("The number is even!");
      expect(testNumbers.numberChecker("2")).to.equal("The number is even!");
      expect(testNumbers.numberChecker(-2)).to.equal("The number is even!");
      expect(testNumbers.numberChecker(0)).to.equal("The number is even!");
      expect(testNumbers.numberChecker("")).to.equal("The number is even!");
    });
    it("test 5", () => {
      expect(testNumbers.numberChecker(3)).to.equal("The number is odd!");
      expect(testNumbers.numberChecker(-3)).to.equal("The number is odd!");
      expect(testNumbers.numberChecker("3")).to.equal("The number is odd!");
      expect(testNumbers.numberChecker(1)).to.equal("The number is odd!");
    });  
    it("test 52", () => {  
    expect(() =>
        testNumbers.numberChecker("a").to.throw()
      );
    });  
    
  });
  describe("averageSumArray", () => {
    it("test 5", () => {
      expect(testNumbers.averageSumArray([2, 2])).to.equal(2);
      expect(testNumbers.averageSumArray([3, 3, 3])).to.equal(3);
      expect(testNumbers.averageSumArray([1])).to.equal(1);
      expect(testNumbers.averageSumArray([2])).to.equal(2);
      expect(testNumbers.averageSumArray([0])).to.equal(0);
    });
  });
});
