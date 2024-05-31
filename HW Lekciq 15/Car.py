class Car: 
    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year 

    def start_engine(self):
        print(f'Engine started for: {self.make}, {self.model} {self.year}')

    def stop_engine(self):
        print(f'Engine stopped for: {self.make}, {self.model} {self.year}')



car1 = Car("Toyota", "Camry", 2022)
car1.start_engine()
car1.stop_engine()