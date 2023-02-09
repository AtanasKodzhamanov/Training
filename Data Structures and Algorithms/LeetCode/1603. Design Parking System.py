class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

        self.bcur = 0
        self.mcur = 0
        self.scur = 0

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.bcur < self.big:
                self.bcur += 1
                return True
            else:
                return False
        if carType == 2:
            if self.mcur < self.medium:
                self.mcur += 1
                return True
            else:
                return False
        if carType == 3:
            if self.scur < self.small:
                self.scur += 1
                return True
            else:
                return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
