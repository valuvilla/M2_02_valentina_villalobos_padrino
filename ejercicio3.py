#creamos dos variables
username = "Valentina"
password = "Tokio"
#Comprobamos que el nombre de usuario tiene igual o más de 3 caracteres y menos de 10
n_1 = len(username)>=3 and len(username)<10
print("Username:" + " " + str(n_1))
#Comprobamos que la contraseña es igual a "Python" o "Tokio"
n_2 = (password == "Tokio" or password == "Python")
print("Password:" + " " + str(n_2))