from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
#idee: faizre des questions predefini zehma des rectangles zbien fait, qui fait le truc interactif avec plusieurs choix
# qui ensuite on donne la possibilite de faire apparaitre les resultats sur une page web via folium