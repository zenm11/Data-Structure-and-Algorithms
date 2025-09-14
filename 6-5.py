def staircase(n, j= 1):

    
    
    
    
    if n == 0:
        print("Not Draw!")
    
    
     
        
    if n > 0:
        if j > n:
            return

        print("_" * (n-j) + "#" * j)
        staircase(n, j+1)

    if n < 0:
        if j > abs(n):
            return
        print("_" * (j-1) + "#" * (abs(n) - j + 1))
        staircase(n, j+1)
     
            
        

    
        
        


            








print(" *** Stair case ***")
staircase(int(input("Enter Input : ")))

print("===== End of program =====")