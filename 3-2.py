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





  


open_excess = "({["
close_excess = ")}]"    
brackets = {')' : '(' , ']' : '[' , '}' : '{'}


def check(p):
    var = stack()
    for ch in p:  
        if ch in open_excess:
            var.push(ch)                   
        elif ch in close_excess:
            if var.is_empty():
                print(f"{p} close paren excess")
                return
            recent = var.pop()

            if brackets[ch] != recent:
                print(f"{p} Unmatch open-close")
                return
            
    if not var.is_empty():
        left = ''.join(var.get_stack())
        print(f"{p} open paren excess   {len(left)} : {left}")
    else:
        print(f"{p} MATCH")
p = input("Enter expresion : ")  
check(p)

            
            
                
           
           

        
        
    
    
