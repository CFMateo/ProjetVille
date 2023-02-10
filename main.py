from flask import Flask, render_template, request
import folium
from geopy.geocoders import Nominatim
from ABRVilles import nvilles_haut_rang, nvilles_bas_rang, nvilles_haut_sup, nvilles_bas_sup
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def choixvilles():
    ''' Ce qui va etre la page d'accueil pour l'utilsateur, il pouura specifier ces choix
    par rapports a:
    nb : int ,qui est le nombre de ville avec equel il voudra faire la recherche
    t: string, qui est le type de trie selon lequel les villes seront sellectionnées
    '''
    if request.method == "GET":
        return render_template("index.html")
    #si la methode est post:
    global nb,t #va nous permettre d'utiliser ces variables dans les differentes fonctions
    nb = int(request.form.get('nbVilles')) #ici on stock dans les variables les valeurs entrées par l'utilisateur
    t = request.form.get('typetrie')
    return map()


@app.route('/map',methods=['POST'])
def map():
    global nb,map
    map = folium.Map(location=[47.000, 2.000], zoom_start=6) #on initialise la map 'basique'
    villesSelec = SelecVille(nb,t) #va nous renvoyer la liste de ville demandée par l'utilisateur
    for i in range(nb): 
        ajtbalise(villesSelec[i]) #ajout des marqueurs des villes sur la map
    return map._repr_html_() #va nous renvoyer un fichier html de la map avec les balises

def SelecVille(nbdeVille,typedetrie):
    """
    Fonction qui va permettre de sllectionner les villes que l'utilsateur souhaite,
    selon un certain mode de trie.;
    """
    global nb
    if typedetrie == 'HAUTrang': #l'utilisateur veut les villes avec le plus haut rang
        return nvilles_haut_rang(nb)
    elif typedetrie == 'MOINSrang': #l'utilisateur veut les villes avec le plus petit rang
        return nvilles_bas_rang(nb)
    elif typedetrie == 'HAUTsup': #l'utilisateur veut les villes avec les plus grandes superficies
        return nvilles_haut_sup(nb)
    elif typedetrie == 'MOINSsup': #l'utilisateur veut les villes avec les plus petites superficies
        return nvilles_bas_sup(nb)


def ajtbalise(nomVille):
    """
    grace  ala bibliotheque geopy on va recuperer la position sur la map de
    la ville souhaiter.
    nomVille : str
    
    """
    global map
    geolocator = Nominatim(user_agent="Projet_ville")
    location = geolocator.geocode(nomVille)
    latitude = location.latitude
    longitude = location.longitude
    folium.Marker([latitude, longitude],popup=nomVille,
                icon=folium.Icon(),).add_to(map)


if __name__ == "__main__":
    app.run(debug=True)
