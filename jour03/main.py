# Job 0
input_string = input("Veuillez saisir une chaîne de caractères : ")

file = open("output.txt", "w")
file.write(input_string)
file.close()

print("La chaîne de caractères a été écrite dans le fichier 'output.txt'.")

# Job 0.1
with open("output.txt", "r") as file:
    content = file.read()
print(content)

# Job 01
import re
with open("domains.xml", "r") as file:
    content = file.read()

extensions = {
    ".com": r"\.com\b",
    ".net": r"\.net\b",
    ".org": r"\.org\b",
    ".edu": r"\.edu\b",
    ".gov": r"\.gov\b"
}

extension_counts = {ext: 0 for ext in extensions}

for ext, pattern in extensions.items():
    ext_count = len(re.findall(pattern, content))
    extension_counts[ext] = ext_count

for ext, count in extension_counts.items():
    print(f"{ext}: {count}")

# Job 01
import re
with open("data.txt", "r") as file:
    content = file.read()
    words = re.findall(r'\b\w+\b', content)

    print("Le fichier contient", len(words), "mots.")

# Job 02
import re
n = int(input("Entrez un nombre entier : "))

with open("data.txt", "r") as file:
    content = file.read()
    content = re.sub(r"[^\w\s]", "", content)

    words = content.split()
    count = sum(1 for word in words if len(word) == n)

    print("Le fichier contient", count, "mots de taille", n, ".")

# Job 03
import string
import matplotlib.pyplot as plt

letters = {}
for letter in string.ascii_lowercase:
    letters[letter] = 0

with open("data.txt", "r") as file:
    content = file.read()
    for char in content.lower():
        if char in string.ascii_lowercase:
            letters[char] += 1

total_letters = sum(letters.values())
percentages = {}
for letter, count in letters.items():
    percentages[letter] = count / total_letters * 100
plt.bar(percentages.keys(), percentages.values())
plt.xlabel("Lettres")
plt.ylabel("Pourcentage d'apparition")
plt.title("Pourcentage d'apparition de chaque lettre dans le fichier 'data.txt'")
plt.show()

# Job 05
import matplotlib.pyplot as plt
word_counts = {}

with open("data.txt", "r") as file:
    for line in file:
        words = line.split()
        for word in words:
            size = len(word)
            if size in word_counts:
                word_counts[size] += 1
            else:
                word_counts[size] = 1

total_words = sum(word_counts.values())
word_percentages = {}
for size, count in word_counts.items():
    word_percentages[size] = count / total_words * 100

plt.bar(word_percentages.keys(), word_percentages.values())
plt.xlabel("Taille des mots")
plt.ylabel("% d'apparition")
plt.show()

# Job 08
import matplotlib.pyplot as plt
letter_counts = {}

with open("data.txt", "r") as file:
    for line in file:
        words = line.split()
        for word in words:
            first_letter = word[0].lower()
            if first_letter in letter_counts:
                letter_counts[first_letter] += 1
            else:
                letter_counts[first_letter] = 1

total_letters = sum(letter_counts.values())
letter_percentages = {}
for letter, count in letter_counts.items():
    letter_percentages[letter] = count / total_letters * 100

plt.bar(letter_percentages.keys(), letter_percentages.values())
plt.xlabel("Lettres")
plt.ylabel("% de présence")
plt.show()



