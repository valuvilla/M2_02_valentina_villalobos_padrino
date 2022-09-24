
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

print(len(username)>=3 and len(username)<10)
print(password == "Python" or password == "Tokio")