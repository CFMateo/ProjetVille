"""
https://isn-icn-ljm.pagesperso-orange.fr/basthon-notebook/?from=https://isn-icn-ljm.pagesperso-orange.fr/notebook/ABR-villes.ipynb&aux=https://isn-icn-ljm.pagesperso-orange.fr/fichiers/villes.csv
ALSO RESPOND TO QUESTIONS!!!! (that are in the tp)
mettre bool dans les fonctions pour savoir si l'on veut tout les détails de la ville ou seulement son nom
"""

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

def inserer_r(noeud,liste,parametre='s'):
    """
    rang
    Args:
        noeud (_type_): _description_
        liste (_type_): _description_
        parametre (bool): r pour classer par rang et s pour classer par superficie (s par défaut)
    """
    assert parametre == 's' or parametre == 'r', "Le parametre donné n'est pas reconnu"
    #mettre assert a la fin pour opti? ou pas besoin?
    v = Ville(liste) # On crée un objet ville
    if parametre == 'r':
        
        if v.getRang() < noeud.ville.getRang():# On compare les rangs
            if noeud.left is None: # Si le noeud n'a pas de fils gauche
                noeud.left = Noeud(liste) # On le crée avec la valeur
            else:
                inserer(noeud.left,liste,'r') # Sinon on l'insère dans le sous-arbre gauche 
        elif v.getRang() < noeud.ville.getRang():
            if noeud.right is None:
                noeud.right = Noeud(liste)
            else:
                inserer(noeud.right,liste,'r')
    else:
        if v.superficie < noeud.ville.superficie:# On compare les rangs
            if noeud.left is None: # Si le noeud n'a pas de fils gauche
                noeud.left = Noeud(liste) # On le crée avec la valeur
            else:
                inserer(noeud.left,liste) # Sinon on l'insère dans le sous-arbre gauche
        elif v.superficie > noeud.ville.superficie:
            if noeud.right is None:
                noeud.right = Noeud(liste)
            else:
                inserer(noeud.right,liste)

def inserer(noeud,liste):
    """
    do i need to make each object a city
    Args:
        noeud (_type_): _description_
        liste (_type_): _description_
    """
    v = Ville(liste) # On crée un objet ville
    if v.superficie < noeud.ville.superficie:# On compare les rangs
        if noeud.left is None: # Si le noeud n'a pas de fils gauche
            noeud.left = Noeud(liste) # On le crée avec la valeur
        else:
            inserer(noeud.left,liste) # Sinon on l'insère dans le sous-arbre gauche
    elif v.superficie > noeud.ville.superficie:
        if noeud.right is None:
            noeud.right = Noeud(liste)
        else:
            inserer(noeud.right,liste)

import csv
liste_villes=[]
with open("villes.csv",'r',encoding='utf-8') as f:
    lecteur=csv.reader(f,delimiter=',')
    for ligne in lecteur:
        liste_villes.append(ligne)
#print(liste_villes[0])
#print(liste_villes[1])

liste = liste_villes[107]
noeud = Noeud(liste)
#noeud.getValeur()
for el in liste_villes:
    inserer(noeud,el)

def parcours_infixe(noeud,l=[]):
    """
    CHANGER LE COMM
    vérif si ca marche
    """
    parcours_infixe(noeud.right)
    l.append(noeud.ville.nom)
    parcours_infixe(noeud.left)
    
        
    return l
#print(parcours_infixe(noeud))
#print(liste_villes)
#print(parcours_infixe(noeud))
#noeud.__str__

def rechercher(noeud,rang):
    assert(0<rang<201), ' le rang est compris entre 1 et 200'
    if noeud.ville.rang == rang:
        return noeud
    elif noeud.ville.rang > rang:
        rechercher(noeud.right,rang)
    else:
        rechercher(noeud.left,rang)

#rechercher(noeud,100).getValeur()

def rechercheMax(noeud):
    """
    return only name? 
    Args:
        noeud (_type_): _description_
    Returns:
        _type_: _description_
    """
    if noeud.right is None:
        return noeud.getValeur()
    rechercheMax(noeud.right)
def rechercheMin(noeud):
    """
    Pas besoin d'utiliser print quand on appelle cette fonction, cela renvera seulement un None en plus.
    Cela est du au fait que la methode getValeur() d'un noeud renvoie
    a la methode afficherVille() de la classe Ville qui elle meme utilise
    directement la fonction print pour le renvoi.
    Args:
        noeud (_type_): _description_
    Returns:
        _type_: _description_
    """
    if noeud.left is None:
        return noeud.getValeur()
    rechercheMin(noeud.left)

rechercheMin(noeud)
rechercheMax(noeud)

import networkx as nx
import matplotlib.pyplot as plt


def hauteur(arbre):
    if arbre is None:
        return 0
    else:
        return 1 + max(hauteur(arbre.left), hauteur(arbre.right))

def repr_graph(arbre, size=(8,8), null_node=False):
    """
    size : tuple de 2 entiers. Si size est int -> (size, size)
    null_node : si True, trace les liaisons vers les sous-arbres vides
    """
    def parkour(arbre, noeuds, branches, labels, positions, profondeur, pos_courante, pos_parent, null_node):
        if arbre is not None:
            noeuds[0].append(pos_courante)
            positions[pos_courante] = (pos_courante, profondeur)
            profondeur -= 1
            labels[pos_courante] = str(arbre.ville.nom)
            branches[0].append((pos_courante, pos_parent))
            pos_gauche = pos_courante - 2**profondeur
            parkour(arbre.left, noeuds, branches, labels, positions, profondeur, pos_gauche, pos_courante, null_node)
            pos_droit = pos_courante + 2**profondeur
            parkour(arbre.right, noeuds, branches, labels, positions, profondeur, pos_droit, pos_courante, null_node)
        elif null_node:
            noeuds[1].append(pos_courante)
            positions[pos_courante] = (pos_courante, profondeur)
            branches[1].append((pos_courante, pos_parent))
    
    
    if arbre is None:
        return
    
    branches = [[]]
    profondeur = hauteur(arbre)
    pos_courante = 2**profondeur
    noeuds = [[pos_courante]]
    positions = {pos_courante: (pos_courante, profondeur)} 
    labels = {pos_courante: str(arbre.ville.nom)}
    
    if null_node:
        branches.append([])
        noeuds.append([])
        
    profondeur -= 1
    parkour(arbre.left, noeuds, branches, labels, positions, profondeur, pos_courante - 2**profondeur, pos_courante, null_node)
    parkour(arbre.right, noeuds, branches, labels, positions, profondeur, pos_courante + 2**profondeur, pos_courante, null_node) 

    mon_arbre = nx.Graph()
    
    if type(size) == int:
        size = (size, size)    
    plt.figure(figsize=size)
    
    nx.draw_networkx_nodes(mon_arbre, positions, nodelist=noeuds[0], node_color="white", node_size=550, edgecolors="blue")
    nx.draw_networkx_edges(mon_arbre, positions, edgelist=branches[0], edge_color="black", width=2)
    nx.draw_networkx_labels(mon_arbre, positions, labels)

    if null_node:
        nx.draw_networkx_nodes(mon_arbre, positions, nodelist=noeuds[1], node_color="white", node_size=50, edgecolors="grey")
        nx.draw_networkx_edges(mon_arbre, positions, edgelist=branches[1], edge_color="grey", width=1)

    ax = plt.gca()
    ax.margins(0.1)
    plt.axis("off")
    plt.show()
    plt.close()

repr_graph(noeud,(10,10))
