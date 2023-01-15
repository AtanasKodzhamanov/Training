class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        output = []
        num1 = 0
        num2 = 0
        for i in operations:
            if i == "C":
                output.pop()
            elif i == "+":
                output.append(num1+num2)
            elif i == "D":
                output.append(num2*2)
            elif i.isdigit():
                output.append(int(i))
                num1 = num2
                num2 = int(i)
        return sum(output)
