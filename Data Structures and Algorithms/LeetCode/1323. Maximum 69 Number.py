class Solution:
    def maximum69Number(self, num: int) -> int:
        number = str(num)
        output = ""
        for i in range(len(number)):
            if number[i] == "6":
                output += "9" + number[i+1:]
                break
            output += number[i]
        return int(output)
