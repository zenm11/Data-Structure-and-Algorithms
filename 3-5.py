class stack:
    def __init__(self, values=[]):
        self.stack = values
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None
    def is_empty(self):
        return len(self.stack) == 0
    def get_stack(self):
        return self.stack
print("******** Parking Lot ********")
inp = input("Enter max of car / car in soi / operation : ")

max_car, car_in, instruction = inp.split("/")
com, value = instruction.split()
max_car, value = int(max_car), int(value)

car1 = stack()

for car in car_in.split(","):
    car1.push(int(car))


if com == "arrive":
    if value in car1.get_stack():
        print(f"car {value} already in soi")
    else:
        
        if len(car1.get_stack()) +1 <= max_car:

            print(f"car {value} arrive! : Add Car {value}")
            car1.push(value)
        else:
            print(f"car {value} cannot arrive : Soi Full")
elif com == "depart":
    if value in car1.get_stack():
        car1.stack.remove(value)
        print(f"car {value} depart ! : Car {value} was remove")
    else:
        print(f"car {value} cannot depart : Dont Have Car {value}")

print(car1.get_stack())

    

