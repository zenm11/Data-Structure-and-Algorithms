class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, root, data):  
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root

    
    def build(self, values):
        for v in values:
            self.root = self.insert(self.root, v)

    
    def lessthan_k(self, node, k):
        if node is None:
            return 0
        if node.data <= k:
            return 1 + self.lessthan_k(node.left, k) + self.lessthan_k(node.right, k)
        else:
            return self.lessthan_k(node.left, k)



def printTree90(node, level = 0):
    if node is not None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)



    
                

if __name__ == "__main__":
    tree = BinarySearchTree()
    data = input("Enter Input : ")
    number, k = data.split("/")
    k = int(k)
    number = list(map(int, number.split()))

    
    bst = BinarySearchTree()
    bst.build(number)

    printTree90(bst.root)
    print("--------------------------------------------------")
    print(bst.lessthan_k(bst.root, k))
    





