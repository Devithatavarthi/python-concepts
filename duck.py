class vehicle:
    def start(self):
        print("vehicle start")
class car(vehicle):
    def start(self):
        print("car start")
class bike(vehicle):
    def start(self):
        print("bike start")
class generator(vehicle):
    def start(self):
        print("start")
class machine(vehicle):
    def start(self):
        print("start")
vehicles=[vehicle(),car(),bike(),generator(),machine()]
for v in vehicles:
    v.start()