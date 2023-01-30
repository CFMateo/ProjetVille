
#creation de la classe ville
class Ville :
    """classe définissant une ville de France. Chaque ville a 4 attributs :
        - nom
        - numero de departement
        - population (hab)
        - superficie (km^2)
        - rang au niveau national (place)"""

    def __init__(self,liste) :
        self.nom = liste[0]
        self.departement = int(liste[1])
        self.population = int(liste[2])
        self.superficie = float(liste[3])
        self.rang = int(liste[4])
        
    def getRang(self) :
        return self.rang
        

    def getSuperficie(self) :
        return self.superficie

    def afficherVille(self) :
        print("Nom :" ,self.nom)
        print("Département :" ,self.departement)
        print("Population :" ,self.population)
        print("Superficie :" ,self.superficie, " km²")
        print("Rang :" ,self.rang)

    def afficherNom(self) :
        print(self.nom)
        


#creation de classe noeud
class Noeud:
    # Le constructeur
    def __init__(self, liste, left=None, right=None):
        self.ville = Ville(liste)
        self.left = left
        self.right = right

    def __str__(self): # pour l'utilisation de print
        self.ville.afficherVille()
    
    def getValeur(self):
        self.ville.afficherVille()

    def estFeuille(self):
        if not self.left and not self.right:
            return True
        else:
            return False
