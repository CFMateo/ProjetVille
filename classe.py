
class Ville :
    """
    classe définissant une ville de France. Chaque ville a 4 attributs :
        - nom
        - numero de departement
        - population (hab)
        - superficie (km^2)
        - rang au niveau national (place)
    """

    def __init__(self,liste) :
        """
        Fonction constructrice de l'objet 'Ville'.
        Voir la documentation de la classe pour voir les paramètres que l'on peut y ajouter.
        L'argument liste est une liste qui contient les paramètres de la ville que l'on souhaite modéliser.
        (les paramètres doivent être donnés dans l'ordre ci-dessous)
        """
        self.nom = liste[0]
        self.departement = int(liste[1])
        self.population = int(liste[2])
        self.superficie = float(liste[3])
        self.rang = int(liste[4])
        
    def getRang(self) :
        """
        Méthode qui renvoit le rang de la ville.
        """
        return self.rang

    def getSuperficie(self) :
        """
        Méthode qui renvoit la superficie de la ville.
        """
        return self.superficie
        
    def afficherVille(self) :
        """
        Méthode qui affiche tout les paramètres de la ville.
        (pas besoin d'utiliser la fonction print lors de l'appel de 
        cette fonction car elle y est déja intégrée)
        """
        print("Nom :" ,self.nom)
        print("Département :" ,self.departement)
        print("Population :" ,self.population)
        print("Superficie :" ,self.superficie,"km²")
        print("Rang :" ,self.rang)

    def afficherNom(self):
        """
        Méthode qui renvoit le nom de la ville.
        """
        return self.nom

class Noeud:
    # Le constructeur
    def __init__(self, liste, left=None, right=None):
        """
        Args:
            liste (liste): _description_
            left (Noeud): fils gauche de ce noeud dans l'arbre. (None par défaut)
            right (Noeud): fils droit de ce noeud dans l'arbre. (None par défaut)
        """
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
