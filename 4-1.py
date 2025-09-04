def queue(cmd):
    que = []


    for command in cmd:
        parts = command.strip().split()
        


        if parts[0] == "E" and len(parts) == 2:
            integer = parts[1]
            que.append(integer)
            print(f"Add {parts[1]} index is {len(que)-1}")

        elif parts[0] == "D":
            i = 0
            i = i - 1

            if que:
                remove = que.pop(0)
                print(f"Pop {remove} size in queue is {len(que)}")
            else:
                print(f"{i}")


    
    if que:
        print(f"Number in Queue is : {que}")
    else:
        print(f"Empty")




    


        






cmd = input("Input list : ").split(",")
queue(cmd)