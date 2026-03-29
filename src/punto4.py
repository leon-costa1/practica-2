def email_validation():
    email = input("Ingrese un mail: ")

    correct = False

    if email.count("@") == 1:
        if not email.startswith(("@", ".")) and not email.endswith(("@", ".")):
            parts = email.split("@")
            if len(parts[0]) >= 1 and "." in parts[1]:
                if len(parts[1].split(".")[-1]) >= 2:
                    correct = True

    if correct: 
        print("El email es valido")
    else:
        print("El email no es valido")