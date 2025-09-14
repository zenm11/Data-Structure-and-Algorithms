class node:
    def __init__(self, data, next = None ):
        self.data = data
        
        self.next = next


    def __str__(self):
        return str(self.data)

def createList(l=[]):
    if not l:
        return None
    
    head = node(l[0])
    curr = head
    for i in l[1:]:
        curr.next = node(i)
        curr = curr.next
    return head


def printList(H):
    curr = H
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next    
    print()

def mergeOrderesList(p, q):
    dummy = node(0)
    tail = dummy
    while p and q:
        if p.data <= q.data:
            tail.next = p
            p = p.next
        else:
            tail.next = q
            q = q.next
        tail = tail.next

    if p:
        tail.next = p 
    if q:
        tail.next = q
    return dummy.next

#################### FIX comand ####################   
# input only a number save in L1,L2
if __name__ == "__main__":

    data = input("Enter 2 Lists : ")
    L1_str, L2_str = data.split()
    L1 = list(map(int, L1_str.split(",")))
    L2 = list(map(int, L2_str.split(",")))
    LL1 = createList(L1)
    LL2 = createList(L2)
    print(f'LL1 : ', end='')
    printList(LL1)
    print(f'LL2 : ', end='')
    printList(LL2)
    m = mergeOrderesList(LL1,LL2)
    print(f'Merge Result : ', end='')
    printList(m)