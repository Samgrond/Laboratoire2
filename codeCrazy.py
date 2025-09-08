#Code super génial
import random

variable1 = ""
variable2 = ""


variable1 = input("T'es qui toé? Tu vas me donner ton prénom : ")

print (f"Votre prénom est : {variable1}")

variable2 = input("T'es qui toé? Tu vas me donner ton nom : ")

print (f"Votre prénom est : {variable2}")

variable3 = random.randint(1, 110)

print(f"Votre nom complet est {variable1} {variable2} et j'assume que tu as {variable3} ans")

variable4 = ""

variable4 = input("Est-ce que c'est le bon age? ")

if variable4 == "oui" or variable4 == "Oui":
    print("Je le savais")
else:
    print("Kk je m'en fiche")