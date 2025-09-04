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
    


    




print(" ***Cafe*** ")

commands = input("Log : ").split('/')




main = Queue()
for i, entry in enumerate(commands):
    
    parts = entry.split(',')
    arrival = int(parts[0])
    service = int(parts[1])

    
    main.enqueue({
        'id': i + 1,
        'arrival': arrival,
        'service': service,
        'start': None,
        'end': None,
        'wait': 0
    })
event = []
max_wait = 0
wait_id = None
baristas = [0,0]
    
    
   
    

while not main.isEmpty():

    customer = main.peek()
    main.dequeue()
    index = 0 if baristas[0] <= baristas[1] else 1
    barista_free = baristas[index]
     
    if barista_free <= customer['arrival']:
        start_time = customer['arrival']
        wait = 0
    else:
        start_time = barista_free
        wait = start_time - customer['arrival']

    end_Time = start_time + customer['service']
    baristas[index] = end_Time #Set the new free time for the barista; END time equals baristas new free time

    customer['start'] = start_time
    customer['end'] = end_Time
    customer['wait'] = wait

    event.append((end_Time, customer['id']))

    if wait > max_wait:
        max_wait = wait
        wait_id = customer['id']

event.sort()

for time, customer_id in event:
    print(f"Time {time} customer {customer_id} get coffee")


if max_wait > 0:
    print(f"The customer who waited the longest is : {wait_id}")
    print(f"The customer waited for {max_wait} minutes")
else:
    print(f"No waiting")
