#diccionario Usuarios-Clave
users = { #crear un diccionario
            'sofia': 'srg123',
            'juan': 'jfk123',
            'ambar': 'arg123',
            'ramon': 'rco123',
           }
continuar = ""
while continuar != "SI":
    usuario=input("Digite su nombre de usuario: ")
    if usuario in users:
        password=input("Digite su contraseña: ")
        passwordOriginal = users[usuario]
        if passwordOriginal == password :
            print("Bienvenido a la red social...")
            print("1-Cambiar nombre de usuario")
            print("2-Cambiar contraseña")
            print("3-Salir")
            op = input("Digite una opción: ")
            if op == "1":
                    new_user = input("Digite su nuevo usuario: ")
                    users[new_user] = users.pop(usuario)
                    print(users)
            elif op == "2":
                    new_Password = input("Digite su nueva contraseña: ")
                    users[usuario]=new_Password
                    print(users)
            elif op == "3" :
                print("Hasta luego")
        else :
            resp=input("Contraseña incorrecta \n ¿Desea crear una nueva cuenta?(Si/No)").upper()
            if( resp == "SI"):
                key = input("Digite el nombre de usuario: ")
                value = input("Digite la contraseña: ")
                users[key] = value
                print(users)
    else :
        print("Usuario no registrado")
        resp=input("Contraseña incorrecta \n ¿Desea crear una nueva cuenta?(Si/No)").upper()
        if( resp == "SI"):
                key = input("Digite el nombre de usuario: ")
                value = input("Digite la contraseña: ")
                users[key] = value
                print(users)
    continuar=input("¿Desea salir?").upper()
    