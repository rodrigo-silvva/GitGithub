from random import randint
from time import sleep

n= randint(1,10)
j=int(input("Tentativa"))

print("Analisando...")
sleep(.3)
print(".")
sleep(.3)
print(".")
sleep(.3)
print(".")

contador=1
while j != n:
    if j<n:
        print(f"O número é maior do que {j}")
    else:
        print(f"O número é menor que {j}")
    j= int(input("Tentativa: "))
    contador+=1

    print("Analisando...")
    sleep(.3)
    print(".")
    sleep(.3)
    print(".")
    sleep(.3)
    print(".")

print(f"Parabéns! Acertaste, após {contador} tentativas.")