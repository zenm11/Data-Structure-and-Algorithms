p = input("Enter Input : ")

stack = []
brackets = {')' : '(' , ']' : '['}
missing = 0

for ch in p:
    if ch in "([":
        stack.append(ch)
    elif ch in ")]":
        if stack and stack[-1] == brackets[ch]:
            stack.pop()
        else:
            missing += 1
           

        
        
    
    

missing += len(stack)

print(missing)
if missing == 0:
    print("Perfect ! ! !")