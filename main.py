def jarvis():
    print("Jarvis Online.")
    
    while True:
        command = input("What do you want to design? ")

        if "grappling hook" in command:
            print("Design: Use compressed air + hook + strong cable.")
            print("Physics: Needs high force and tension strength.")
        
        elif "web shooter" in command:
            print("Design: Pressurized canister with strong thread.")
            print("Warning: Real web fluid does not exist.")
        
        elif "exit" in command:
            print("Shutting down Jarvis...")
            break
        
        else:
            print("Analyzing... Try a different idea.")

jarvis()
