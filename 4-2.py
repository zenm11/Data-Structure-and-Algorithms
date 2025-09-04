class Queue:
    def __init__(self, value=None):
        self.Queue = value if value is not None else []

    def getqueue(self):
        return self.Queue.copy()
    

    def enqueue(self, value):
        self.Queue.append(value)

    def dequeue(self):
        if self.Queue:
            self.Queue = self.Queue[1:]
    
    def peek(self):
        
        return self.Queue[0] if self.Queue else None
    def isEmpty(self):
        return len(self.Queue) == 0
    def getcount(self):
        return len(self.Queue)
        
    




commands = input("Enter people : ")  

main = Queue(list(commands))
list1 = Queue()
list2 = Queue()

c1time = 0
c2time = 0

summation = 0
while not main.isEmpty():
    summation += 1


    if c1time == 0 and not list1.isEmpty():
        list1.dequeue()
        
        c1time = 3 if not list1.isEmpty() else 0

    if c2time == 0 and not list2.isEmpty():
        list2.dequeue()
        c2time = 2 if not list2.isEmpty() else 0


    if not main.isEmpty():
        person = main.peek()
        if list1.getcount() < 5:
            main.dequeue()
            list1.enqueue(person)
            if list1.getcount() == 1:
                c1time = 3
        elif list2.getcount() < 5:
            main.dequeue()
            list2.enqueue(person)
            if list2.getcount() == 1:
                c2time = 2

    if c1time > 0:
        c1time -= 1

    if c2time >0:
        c2time -= 1


    print(summation, main.getqueue(), list1.getqueue(), list2.getqueue())



        




















