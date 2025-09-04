def queue(commands):
    que = []

    for command in commands:
        parts = command.strip().split()
        if not parts:
            continue
        action = parts[0]

        if action == "ARRIVE":
            names = parts[1]
            roles = parts[2] if len(parts) > 2 else "REGULAR"
            if roles == "VIP":
                index = 0
                while index < len(que) and que[index][1] == "VIP":
                    index += 1
                que.insert(index, (names, roles))
            else:
                que.append((names, roles))
        elif action == "SERVE":
            if que:
                served = que.pop(0)
                print(f"Served: {served[0]}")
            else:
                print("No customers.")

        elif action == "VIEW":
            print(f"Queue:", [person[0] for person in que])
            
        elif action == "EXIT":
            print("Exiting.")
            break













inp = input("Input: ")
commands = [command.strip() for command in inp.split(";") if command.strip()]
queue(commands)








