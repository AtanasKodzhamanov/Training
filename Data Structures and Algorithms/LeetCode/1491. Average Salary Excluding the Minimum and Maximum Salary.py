class Solution:
    def average(self, salary: List[int]) -> float:
        maxsal = 0
        minsal = 1000000
        cumsum = 0
        for i in range(len(salary)):
            cumsum += salary[i]
            if salary[i] > maxsal:
                maxsal = salary[i]
            if salary[i] < minsal:
                minsal = salary[i]

        return (cumsum-maxsal-minsal)/(len(salary)-2)
