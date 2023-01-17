import random

d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
d3 = random.randint(1, 6)
d4 = random.randint(1, 6)
class NPC:
    def __init__(self):
        self.Force = 1
        self.Agilite = 1
        self.Constitution = 1
        self.intelligence = 1
        self.Sagesse = 1
        self.Charisme = 1
        self.classe_darmure = random.randint(1, 12)
        self.nom = ""
        self.race = ""
        self.espece = ""
        self.pdv = random.randint(1, 20)
        self.profession = ""

    def AfficherCharacteristiques(self):
        print(self.nom)
        print(self.race)
        print(self.espece)
        print(self.pdv)
        print(self.profession)
        print(self.classe_darmure)
        print(self.Force)
        print(self.Agilite)
        print(self.Constitution)
        print(self.Sagesse)
        print(self.Charisme)
        print(self.intelligence)
class kobold(NPC):
    def attaquer(cible):
        return
    def recevoir_dommage(dommage_subis):
        return
class hero(NPC):
    def attaquer(cible):
        return
    def recevoir_dommage(dommage_subis):
        return
