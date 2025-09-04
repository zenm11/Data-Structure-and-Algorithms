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
    


close = ")}]"
open = "([{"
parenthesis = {')' : '(' , ']' : '[' , '}' : '{'}


def check(expression):
    variable = stack()
    for ch in expression:
        if ch in open:
            variable.push(ch)
        elif ch in close:
            if variable.is_empty():
                print(f"{expression} close paren excess")
                return
            recent = variable.pop()
            
            if parenthesis[ch] != recent:
                print(f"{expression} unmatched open-close")
                return

    if not variable.is_empty():
        latest = ''.join(variable.get_stack())
        print(f"{expression} open paren excess {len(latest)} : {latest}")
    else:
        print(f"{expression} MATCH")
expression = input("Enter expression : ")
check(expression)


            

                

        
            

            