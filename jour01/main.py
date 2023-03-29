# Job 03
print(10 + 3)

# Job 05
print("10 + 3 =", 10 + 3)
print("10 * 3 =", 10 * 3)
print("10 % 3 =", 10 % 3)
print("10 - 3 =", 10 - 3)
print("10 / 3 =", 10 / 3)
print("10 // 3 =", 10 // 3)

#  Job 07
def Add(a, b):
    somme = a + b
    return somme


print(Add(2, 3))
print(Add(5, 7))
print(Add(11, 20))

# Job 11
prenom = input("Rensegnez votre prénom : ")
print("Hello", prenom + " !")


# Job 13
nombres = []

for i in range(5):
    nombre = int(input("Entrez un nombre entier : "))
    nombres.append(nombre)

nombres.sort()

print("Les nombres triés par ordre croissant sont : ")
for nombre in nombres:
    print(nombre)

# Job 17
def draw_rectangle(width, height):
    print("-" * (width + 4))

    for i in range(height - 2):
        print("|   " + " " * (width - 2) + "   |")

    print("-" * (width + 4))

draw_rectangle(10, 3)


#  Job 23
def draw_triangle(height):
    print(" " * (height - 1) + "/")

    for i in range(height - 2):
        print(" " * (height - i - 2) + "/" + " " * (2*i+1) + "\\")

    print("/" + "_" * (2*height-3) + "\\")

draw_triangle(5)

#  Job 29
def arrondir_notes(notes):
    notes_arrondies = []
    for note in notes:
        if note < 40:
            notes_arrondies.append(note)
        elif note % 5 >= 3 and note >= 38:
            notes_arrondies.append(note + 5 - note % 5)
        else:
            notes_arrondies.append(note)
    return notes_arrondies

liste_notes = [38, 42, 67, 81, 77, 89]
notes_arrondies = arrondir_notes(liste_notes)
print(notes_arrondies)
