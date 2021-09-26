a = input("enter (register = r/login = l): ")
if a == "r":
    # stage 1 registration
    import re
    regex = r'\b[A-Za-z]+[A-Za-z0-9._%+-]+@[A-Za-z]+\.[A-Z|a-z]{2,}\b'
    while True:
        email = input("enter email/username: ")
        valid = False
        if re.fullmatch(regex, email):
            valid = True
            break
        else:
            print("invalid")
    if True:
        print("valid")
    
    import re 
    while True:
        password = input("Enter password : ") 
        is_valid = False 
        if (len(password)<6 or len(password)>16): 
            print("Not valid ! Total characters should be between 6 and 16") 
            continue 
        elif not re.search("[A-Z]",password):
            print("Not valid ! It should contain one letter between [A-Z]")
            continue 
        elif not re.search("[a-z]",password):
            print("Not valid ! It should contain one letter between [a-z]") 
            continue
        elif not re.search("[1-9]",password): 
            print("Not valid ! It should contain one letter between [1-9]") 
            continue 
        elif not re.search("[~!@#$%^&*]",password): 
            print("Not valid ! It should contain at least one letter in [~!@#$%^&*]") 
            continue 
        elif re.search("[\s]",password): 
            print("Not valid ! It should not contain any space") 
            continue
        else:
            is_valid = True
            break
    if(True):
        print("Password is valid")

    # stage 2
    with open(f"{email}", "w") as f:
        f.write(f"{password}")

# stage 3 login
elif a == "l":
    email = input("enter email/username: ")
    password = input("enter password: ")
    try:
        with open(f"{email}") as f:
            b = f.read()
            if b == password:
                print("valid")
    except FileNotFoundError:
        print("not valid")
        d = input("enter (register = r / forgot password = fp): ")
        if d == "fp":
            email = input("enter email/username: ")
            try:
                with open(f"{email}") as f:
                    c = f.read()
                    print(c)
            except FileNotFoundError:
                print("register")
        if d == "r":
            import re
            regex = r'\b[A-Za-z]+[A-Za-z0-9._%+-]+@[A-Za-z]+\.[A-Z|a-z]{2,}\b'
            while True:
                email = input("enter email/username: ")
                valid = False
                if re.fullmatch(regex, email):
                    valid = True
                    break
                else:
                    print("invalid")
            if True:
                print("valid")
    
            import re 
            while True:
                password = input("Enter a password : ") 
                is_valid = False 
                if (len(password)<6 or len(password)>16): 
                    print("Not valid ! Total characters should be between 6 and 16") 
                    continue 
                elif not re.search("[A-Z]",password):
                    print("Not valid ! It should contain one letter between [A-Z]")
                    continue 
                elif not re.search("[a-z]",password):
                    print("Not valid ! It should contain one letter between [a-z]") 
                    continue
                elif not re.search("[1-9]",password): 
                    print("Not valid ! It should contain one letter between [1-9]") 
                    continue 
                elif not re.search("[~!@#$%^&*]",password): 
                    print("Not valid ! It should contain at least one letter in [~!@#$%^&*]") 
                    continue 
                elif re.search("[\s]",password): 
                    print("Not valid ! It should not contain any space") 
                    continue
                else:
                    is_valid = True
                    break
            if(True):
                print("Password is valid")
        
            # stage 2
            with open(f"{email}", "w") as f:
                f.write(f"{password}")