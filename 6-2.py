def length(txt, index=0):
    
    if txt == "":
        
        
        return 0
    else:

    
    
        print(txt[0], end="")
        
    
        if index % 2 == 0:

            print("*", end="")
        else: 
            if index % 2 == 1:
                print("~", end="")
        return 1 + length(txt[1:], index+1)
     


    


    

print(" *** Length of string (Recursion) *** ")    
s = input("Enter Input : ")
n = length(s)
print(f"\nlength of '{s}' is {n}")
