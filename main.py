#https://isn-icn-ljm.pagesperso-orange.fr/basthon-notebook/?from=https://isn-icn-ljm.pagesperso-orange.fr/notebook/ABR-villes.ipynb&aux=https://isn-icn-ljm.pagesperso-orange.fr/fichiers/villes.csv

import csv
import networkx as nx
import matplotlib.pyplot as plt
from classe import Ville,Noeud

# A FAiRE: 2) TP "Villes" + Projet le prolongeant:
# a) rajouter une interface utilisateur (en console par exemple), permettant d'effectuer des requêtes simples sur ces 200 villes:
# Par exemple : "Quelles sont les 10 villes les plus peuplées de France ?" , "Quelles sont les 5 villes ayant la plus petite superficie" ?
# b) Utiliser la bibliothèque folium pour faire apparaitre les résultats sur une carte dans une page web



#PARTIE TP:

# À faire : Compléter la fonction inserer(noeud,liste) qui permet de construire l'ABR en fonction du rang
def insererRang(noeud,liste):
    ''' l element noeud est celui avec lequel on va comparer la ville,
    le noeud sera donc une racine temporaire differente a chaque appele recursif'''
    v = Ville(liste) # On crée un objet ville
    if v.getRang() < noeud.ville.getRang():# On compare les rangs
        if noeud.left is None: # Si le noeud n'a pas de fils gauche
            noeud.left = Noeud(liste) # On le crée avec la valeur
        else:
            insererRang(noeud.left,liste) # Sinon on l'insère dans le sous-arbre gauche

    if v.getRang() > noeud.ville.getRang():
        if noeud.right is None:
            noeud.right = Noeud(liste)
        else:
            insererRang(noeud.right,liste)


#importation des villes du fichier csv sous forme de liste:
liste_villes=[]   
with open("villes.csv",'r',encoding='utf-8') as f:
    lecteur=csv.reader(f,delimiter=',')
    for ligne in lecteur:   #importation des villes sous forme de liste
        liste_villes.append(ligne)



#Question: Pour obtenir un arbre équilibré, il faut choisir une ville dont le rang est de 100. Pourquoi ? /En quoi est-ce important pour la recherche dans l'arbre ?
# Réponse: Car il faut choisir la médiane du nb de vlle qui est 200 pour qu'il y est en moyenne environ le meme nb de branche a gauche que a droite

print('---------------')
print("ABR construit en fonction des RANGS des villes:")
listeRang = liste_villes[107] #racine de l'ABR en fonction du rang
noeudRang = Noeud(listeRang)
#noeudRang.getValeur() #affiche les infos de la ville
for el in liste_villes:
    insererRang(noeudRang,el)


# parcours INFIXE:
global lInfixe
lInfixe = []
def parcours_infixe(noeud) :
    '''Dans un parcours infixe, on liste le noeud la seconde fois qu on le rencontre.'''
    if not noeud == None:
        parcours_infixe(noeud.right) #appelle recursif avec le fils gauche (si un fils g n'a pas de fls g il l'ajt ensuite a la liste)
        lInfixe.append(noeud.ville.nom)
        #print(arbr.valeur)
        parcours_infixe(noeud.left)
parcours_infixe(noeudRang)


#À faire : Écrire une fonction rechercher(noeud,rang), qui retourne la ville dont le rang est rang.
def rechercherRang(noeud,rang):
    assert(0<=rang<201), ' le rang est compris entre 1 et 200'
    return lInfixe[rang]

print("Voici la ville de rang 44:")
rechercherRang(noeudRang,44)

#À faire :  Modifier ce qu'il faut pour faire afficher les villes par ordre croissant de leur superficie.
def insererSuperficie(noeud,liste):
    ''' l element noeud est celui avec lequel on va comparer la ville,
    le noeud sera donc une racine temporaire differente a chaque appele recursif'''
    v = Ville(liste) # On crée un objet ville
    if v.getSuperficie() < noeud.ville.getSuperficie():# On compare les superficie
        if noeud.left is None: # Si le noeud n'a pas de fils gauche
            noeud.left = Noeud(liste) # On le crée avec la valeur
        else:
            insererSuperficie(noeud.left,liste) # Sinon on l'insère dans le sous-arbre gauche

    if v.getSuperficie() > noeud.ville.getSuperficie():
        if noeud.right is None:
            noeud.right = Noeud(liste)  
        else:
            insererSuperficie(noeud.right,liste)


print('---------------')
print("ABR construit en fonction des SUPERFICIE des villes:")

# initialisation de l'ABR superficie:
listeSuperficie = liste_villes[107] #racine de l'ABR en fonction de la superficie
noeudSup = Noeud(listeSuperficie)
#noeudSup.getValeur() #affiche les infos de la ville
for el in liste_villes:
    insererSuperficie(noeudSup,el)



#Écrivez une fonction rechercheMax(noeud) qui renvoie la ville ayant la plus grande superficie.
def rechercheMax(noeud):
    """
   est ce que on veut seulement le nom de la ville?
    """
    if noeud.right is None:
        return noeud.getValeur() #si on veut toutes les infos de la ville
    rechercheMax(noeud.right)

print("Voici la ville avec la plus grande superficie:")
rechercheMax(noeudSup)

#Écrivez une fonction rechercheMin(noeud) qui renvoie la ville ayant la plus petite superficie.
def rechercheMin(noeud):
    """
    """
    if noeud.left is None:
        return noeud.getValeur()
    rechercheMin(noeud.left)

print("Voici la ville avec la plus petite superficie:")
rechercheMin(noeudSup)




#pas necessaire:
def hauteur(arbre):
    """
    """
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


#repr_graph(noeudSup,(10,10))

