#Job 0
class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print(f"Je m'appelle {self.prenom} {self.nom}")

    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    def get_prenom(self):
        return self.prenom

    def set_prenom(self, prenom):
        self.prenom = prenom


p1 = Personne("Che", "Aiche")
p1.SePresenter()

p2 = Personne("Ma", "Chai")
p2.SePresenter()

p1.set_nom("Toto")
p1.SePresenter()

print(p1.get_nom())
print(p2.get_prenom())

#Job 1
class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def print(self):
        print(self.titre)


class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom


class Auteur(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.oeuvre = []

    def listerOeuvre(self):
        print("Oeuvre de :", self.nom, self.prenom)
        for livre in self.oeuvre:
            print(livre.titre)

    def ecrireUnLivre(self, titre):
        livre = Livre(titre, self)
        self.oeuvre.append(livre)
        return livre


auteur = Auteur("Moliére", "Jean-Baptiste")
livre1 = auteur.ecrireUnLivre("Le Malade imaginaire")
livre2 = auteur.ecrireUnLivre("Les Femmes savantes")

livre1.print()
livre2.print()

auteur.listerOeuvre()

#Job 02.718
class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom


class Auteur(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.oeuvre = []

    def listerOeuvre(self):
        print(f"Liste des livres écrits par {self.nom} {self.prenom}:")
        for livre in self.oeuvre:
            print(livre.titre)

    def ecrireUnLivre(self, titre):
        livre = Livre(titre, self)
        self.oeuvre.append(livre)
        return livre


class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def __str__(self):
        return self.titre

class Client(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.collection = []

    def inventaire(self):
        print(f"Liste des livres en possession de {self.nom} {self.prenom}:")
        for livre in self.collection:
            print(livre.titre)

class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.catalogue = {}

    def acheterLivre(self, auteur, titre, quantite):
        for livre in auteur.oeuvre:
            if livre.titre == titre:
                if titre in self.catalogue:
                    self.catalogue[titre] += quantite
                else:
                    self.catalogue[titre] = quantite
                print(
                    f"{quantite} exemplaire(s) du livre '{titre}' de l'auteur {auteur.nom} ont été ajouté(s) au catalogue de la bibliothèque.")
                return
        print(
            f"Le livre '{titre}' de l'auteur {auteur.nom} n'existe pas dans son oeuvre.")

    def inventaire(self):
        print(f"Catalogue de la bibliothèque '{self.nom}':")
        for livre, quantite in self.catalogue.items():
            print(f"{livre}: {quantite} exemplaires")

    def louer(self, client, titre):
        if titre in self.catalogue and self.catalogue[titre] > 0:
            self.catalogue[titre] -= 1
            livre = Livre(titre, None)
            client.collection.append(livre)
            print(f"{client.nom} {client.prenom} a loué le livre '{titre}'.")
        else:
            print(f"Le livre '{titre}' n'est pas disponible en ce moment.")

    def rendreLivres(self, client):
        for livre in client.collection:
            if livre.titre in self.catalogue:
                self.catalogue[livre.titre] += 1
            else:
                self.catalogue[livre.titre] = 1
        print(f"{client.nom} {client.prenom} a rendu tous ses livres.")


class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom


class Auteur(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.oeuvre = []

    def listerOeuvre(self):
        for livre in self.oeuvre:
            print(livre.titre)

    def ecrireUnLivre(self, titre):
        livre = Livre(titre, self)
        self.oeuvre.append(livre)
        return livre

class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def print(self):
        print(self.titre)


class Client(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.collection = []

    def inventaire(self):
        for livre in self.collection:
            print(livre.titre)

class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.catalogue = {}

    def acheterLivre(self, auteur, titre, quantite):
        for livre in auteur.oeuvre:
            if livre.titre == titre:
                if titre in self.catalogue:
                    self.catalogue[titre] += quantite
                else:
                    self.catalogue[titre] = quantite
                return True
        return False

    def inventaire(self):
        for titre, quantite in self.catalogue.items():
            print(titre, quantite)

    def louer(self, client, titre):
        if titre in self.catalogue and self.catalogue[titre] > 0:
            livre = Livre(titre, self)
            self.catalogue[titre] -= 1
            client.collection.append(livre)
            return True
        else:
            return False

    def rendreLivres(self, client):
        for livre in client.collection:
            if livre.titre in self.catalogue:
                self.catalogue[livre.titre] += 1
            else:
                self.catalogue[livre.titre] = 1
        client.collection.clear()

# Auteurs 
auteur1 = Auteur("Test", "Test")
livre1 = auteur1.ecrireUnLivre("Test1")
livre2 = auteur1.ecrireUnLivre("Test2")

auteur2 = Auteur("To", "Toto")
livre3 = auteur2.ecrireUnLivre("Toto1")
livre4 = auteur2.ecrireUnLivre("Toto2")

# Bibliothèques
biblio1 = Bibliotheque("Bibliothèque 1")
biblio2 = Bibliotheque("Bibliothèque Alcazar")

# Achat
biblio1.acheterLivre(auteur1, "Test1", 10)
biblio1.acheterLivre(auteur1, "Test2", 5)
biblio2.acheterLivre(auteur2, "Toto1", 7)
biblio2.acheterLivre(auteur2, "Toto2", 4)

# Clients
client1 = Client("Aicheche", "Chaima")
client2 = Client("Z", "Sofiane")

# Location 
biblio1.louer(client1, "Test1")
biblio1.louer(client1, "Test2")
biblio2.louer(client2, "Toto1")
biblio2.louer(client2, "Toto2")

print("nombre de livre à rendre", len(
    client1.collection) + len(client2.collection))
biblio1.rendreLivres(client1)
biblio2.rendreLivres(client2)

print("nombre de livres total dans les bibliothèques", biblio1.catalogue["Test1"] + biblio1.catalogue["Test2"] +
      biblio2.catalogue["Toto1"] + biblio2.catalogue["Toto2"])
biblio1.inventaire()
biblio2.inventaire()


client1.inventaire()
client2.inventaire()


# Job 07.389

class Board:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.board = [['O' for _ in range(j)] for _ in range(i)]

    def play(self, col, color):
        if col < 0 or col >= self.j:
            print("Invalide, veuillez choisir une colonne entre 0 et 6")
            return False
        for row in range(self.i-1, -1, -1):
            if self.board[row][col] == 'O':
                self.board[row][col] = color[0]
                return True
        print("Colonne pleine !")
        return False

    def print(self):
        for row in self.board:
            print(" ".join(row))

    def check_win(self, color):
       
        for row in range(self.i):
            for col in range(self.j-3):
                if self.board[row][col] == color[0] and self.board[row][col+1] == color[0] and self.board[row][col+2] == color[0] and self.board[row][col+3] == color[0]:
                    return True

        for row in range(self.i-3):
            for col in range(self.j):
                if self.board[row][col] == color[0] and self.board[row+1][col] == color[0] and self.board[row+2][col] == color[0] and self.board[row+3][col] == color[0]:
                    return True

        for row in range(self.i-3):
            for col in range(self.j-3):
                if self.board[row][col] == color[0] and self.board[row+1][col+1] == color[0] and self.board[row+2][col+2] == color[0] and self.board[row+3][col+3] == color[0]:
                    return True
                if self.board[row+3][col] == color[0] and self.board[row+2][col+1] == color[0] and self.board[row+1][col+2] == color[0] and self.board[row][col+3] == color[0]:
                    return True

        return False


board = Board(6, 7)  
current_player = 'rouge' 
winner = None  

while not winner:
    col = int(input(
        f"{current_player}, dans quelle colonne voulez-vous insérer votre jeton ? de 0 à 6 "))

    if board.play(col, current_player):
        if board.check_win(current_player):
            winner = current_player
        current_player = 'jaune' if current_player == 'rouge' else 'rouge'

print(
    f"Félicitations, {winner} a gagné la partie !")
