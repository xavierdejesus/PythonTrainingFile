class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]

ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')
ford.cars.append('Siera')
ford.cars.append('Bakie')
ford.cars.append('Bakie1')
ford.cars.append('Bakie2')


for car in ford:
    print(car)
