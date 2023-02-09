from flask import Flask, render_template, request
import folium
from ABRVilles import nvilles_haut_rang, nvilles_bas_rang, nvilles_haut_sup, nvilles_bas_sup
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def choixvilles():
    if request.method == "POST":
        result = request.args
        nb = result['nbVilles']
        t = result['typetrie']
        villesSelec = SelecVille(nb,t) 
        # create the map and add markers for the selected cities
        map = folium.Map(location=[47.000, 2.000], zoom_start=6)
        for villes in villesSelec:
            folium.Marker(location=LatetLong(villes)).add_to(map)
        return map
    else:
        # render the form for the user to select cities
        return render_template("index.html")

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

def LatetLong(map,villes):
    """
    return the location (latitude and longitude) of the city """
    geolocator = Nominatim(user_agent="Projet_ville")
    for i in range(len(villes)):
        location = geolocator.geocode(villes[i])
        latitude = location.latitude
        longitude = location.longitude
        folium.Marker([latitude, longitude]).add_to(map)

if __name__ == "__main__":
    app.run(debug=True)
