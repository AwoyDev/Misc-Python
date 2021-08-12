nom = input("Tu es qui :\n")
print("Tu as enregistré : ", nom)
ville = input("Quelle est ta ville :\n")
print("Tu as enregistré : ", ville)

while True:
    try:
        age = int(input("Quel est ton âge  :\n"))
        print("Tu as enregistré :", age)
        break

    except ValueError:
        print("🛑 Vous devez spécifier obligatoirement un chiffre")




print(f"\nVoici le questionnaire rempli :\n\nNom : {nom}\nVille {ville}\nAge : {age}")