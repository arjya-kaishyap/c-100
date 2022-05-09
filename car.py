class Car(object) :
    def __init__(self, model, color, company, speed_limit):
        self.model = model
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
    
    def start(self):
        print("started")
    
    def stop(self):
        print("stoped")
    
    def accelerate(self):
        print("accelerating...")
    
    def change_gear(self,gear_type):
        print("gear changed")

lamborghini = Car("sian","green","lamborghini","450")
print(lamborghini.color)
lamborghini.change_gear(2)
lamborghini.start()
print(lamborghini.speed_limit)