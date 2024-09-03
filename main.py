import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("que tan larga quieres que sea tu contraseña"))
contraseña = ""

for i in range(longitud):
    contraseña += random.choice(caracteres)

print (contraseña)
