
print("{:.2f}".format((365/12)*12.7))
import string
a_1 = 10
a_2 = 4
a_3 = 6
a_4 = 5
a_5 = 5

nota_media = (a_1+a_2+a_3+a_4+a_5)/5
b = "La nota media es"
resultado = str(nota_media) + b
print(resultado)

username = "Valentinita"
password = "Python"
n_1 =  len(username)>=3 and len(username)<10
n_2 = (password == "Python" or password == "Tokio")
print("username:" + " " + str(n_1))
print("password:" + " " + str(n_2))

num1 = 4
num2 = 100

a1 = num1 + 1
a2 = num2 - 2

b1 = a1 * 3
b2 = a2 / 2

num1 = b1
num2 = b2

print(num1)
print(num2)

num1 = (365/12)*14.7
print(num1)
print("{:.02f}".format((num1)))

nota_media = 12
b = "La nota media es"
#Para concadenar ambos resultados hace falta introducir el comando str para que el programa acepte la concadenación de números con letras
print(b + " " + str(nota_media))