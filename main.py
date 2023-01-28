import random

#creer une liste pour trouver la valeur du "dice" et enlever le plus bas
d_list = []
for i in range (4):
    d_list.append(random.randint(1,6))
d_list.sort()
d_list.pop(0)
dice = sum(d_list)

#creer la classe NPC
class NPC:
    def __init__(self):
        self.Force = dice
        self.Agilite = dice
        self.Constitution = dice
        self.intelligence = dice
        self.Sagesse = dice
        self.Charisme = dice
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
#creer kobold
class kobold(NPC):
    #initializer
    def __init__(self):
        super().__init__()
        #attaquer
    def attaquer(self, cible):
        attaque = random.randint(1, 20)
        #attaque critique
        if attaque == 20:
            cible.recevoir_dommage(random.randint(1, 8))
            #attaque rate
        elif attaque == 1:
            cible.recevoir_dommage(0)
        else:
            if attaque >= cible.classe_darmure:
                cible.recevoir_dommage(random.randint(1, 6))
            else:
                cible.recevoir_dommage(0)
    def recevoir_dommage(self, dommage_subis):
        pdv -= dommage_subis
class hero(NPC):
    #initializer
    def __init__(self):
        super().__init__()
        #attaquer
    def attaquer(self, cible):
        attaque = random.randint(1, 20)
        #attaque critique
        if attaque == 20:
            cible.recevoir_dommage(random.randint(1, 8))
            #attaque rate
        elif attaque == 1:
            cible.recevoir_dommage(0)
        else:
            if attaque >= cible.classe_darmure:
                cible.recevoir_dommage(random.randint(1, 6))
            else:
                cible.recevoir_dommage(0)
    def recevoir_dommage(self, dommage_subis):
        pdv -= dommage_subis
