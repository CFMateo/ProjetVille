from flask import Flask, render_template, request
import folium
from ABRVilles import nvilles_haut_rang, nvilles_bas_rang, nvilles_haut_sup, nvilles_bas_sup
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def choixvilles():
    if request.method == "GET":
        return render_template("index.html")

    global nb,t
    #result = request.args #ici on stock dans les variables les valeurs entre par l'utilsateur
    nb = request.form.get('nbVilles')
    print(nb)
    t = request.form.get('typetrie')
    return map()


@app.route('/map',methods=['POST'])
def map():
    global nb
    map = folium.Map(location=[47.000, 2.000], zoom_start=6) #on initialise la map basique
    villesSelec = SelecVille(nb,t) #va nous renvoyer la liste de ville demandée par l'utilisateur
    for i in range(nb): #ajout des marqueurs des villes sur la map
        folium.Marker(location=[villesSelec[i].getLat(), villesSelec[i].getLong()],popup=villesSelec[i].nom,
                icon=folium.Icon(),).add_to(map)
    #on renvoie une représentation html de la carte!
    return map._repr_html_()

def SelecVille(nbdeVille,typedetrie):
    """
    """
    if typedetrie == 'HAUTrang': #l'utilisateur veut les villes avec le plus haut rang
        return nvilles_haut_rang(nbdeVille)
    elif typedetrie == 'MOINSrang': #l'utilisateur veut les villes avec le plus petit rang
        return nvilles_bas_rang(nbdeVille)
    elif typedetrie == 'HAUTsup': #l'utilisateur veut les villes avec les plus grandes superficies
        return nvilles_haut_sup(nbdeVille)
    elif typedetrie == 'MOINSsup': #l'utilisateur veut les villes avec les plus petites superficies
        return nvilles_bas_sup(nbdeVille)
    else:
        return "erreur"


if __name__ == "__main__":
    app.run(debug=True)
