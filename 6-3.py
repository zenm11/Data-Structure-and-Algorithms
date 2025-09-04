


def check(a, b):
    
    a, b = abs(a), abs(b)
    
    
    if b == 0:
        return a
    return check(b, a % b)

    

    


inp = input("Enter Input : ")
a, b = map(int, inp.split())
if a == 0 and b == 0:
    print("Error! must be not all zero.")
else:
    a, b = max(a, b), min(a,b)
    print(f"The gcd of {a} and {b} is : {check(a,b)}")
