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

    def insert(self, r, val):  
        if r is None:
            return Node(val)
        if val < r.data:
            r.left = self.insert(r.left, val)
        else:
            r.right = self.insert(r.right, val)
        return r
    def delete(self, r, data):
        if r is None:
            print("Error! Not Found DATA")
            return None
        if data < r.data:
            r.left = self.delete(r.left, data)
        elif data > r.data:
            r.right = self.delete(r.right, data)
        else:
            if r.left is None:
                return r.right
            elif r.right is None:
                return r.left
            else:
                successor = self.findmin(r.right)
                r.data = successor.data
                r.right = self.delete(r.right, successor.data)
        return r
    
    def findmin(self, r):
        while r.left is not None:
            r = r.left
        return r
                
def printTree90(node, level = 0):
    if node is not None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

if __name__ == "__main__":
    tree = BinarySearchTree()
    
    datas = input("Enter Input : ").split(",")
    for cmd in datas:
        command, num = cmd.split()
        num = int(num)
        if command == "i":
            print(f"insert {num}")
            tree.root = tree.insert(tree.root, num)
            printTree90(tree.root)

         
        elif command == "d":
            print(f"delete {num}")
            tree.root = tree.delete(tree.root, num)
            printTree90(tree.root)
        
