from PySide2 import QtWidgets, QtCore

from movies import get_movies
from movies import Movie

class App(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.setup_ui()
        self.populate_movies()
        self.setup_connections()

    def setup_ui(self):
        """methode pour creer les differents element de notre UI"""

        # CREATION DU LAYOUT
        self.layout = QtWidgets.QVBoxLayout(self) #le layout sous forme de  verticale

        # CREATION DES WIDGETS
        
        self.led_writeFilm = QtWidgets.QLineEdit() #zone pour ecrire le film
        self.btn_addFilm = QtWidgets.QPushButton("Ajouter un film") #bouton
        self.lw_listeFilm = QtWidgets.QListWidget() #zone liste des films
        self.lw_listeFilm.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_delFilm = QtWidgets.QPushButton("Supprimer le(s) film(s)") #bouton


        # AJOUT AU LAYOUT
        self.layout.addWidget(self.led_writeFilm)
        self.layout.addWidget(self.btn_addFilm)
        self.layout.addWidget(self.lw_listeFilm)
        self.layout.addWidget(self.btn_delFilm)

    def setup_connections(self):

        # ajout du film ecrit dans la line edit
        self.led_writeFilm.returnPressed.connect(self.add_movie)
        # ajout du film lorsque l'on clique sur le bouton
        self.btn_addFilm.clicked.connect(self.add_movie)
        # suppression du film lorsque l'on clique sur le bouton
        self.btn_delFilm.clicked.connect(self.remove_movie)

    def populate_movies(self):

        self.lw_listeFilm.clear()

        #recupere la liste des classe Movie du fichier movies.json
        movies = get_movies()
        
        for m in movies:
            """on boucle sur les classes dans la liste"""

            # on va stocker la classe en tant qu'item
            lw_item = QtWidgets.QListWidgetItem(m.title) #on cree un list widget item
            lw_item.setData(QtCore.Qt.UserRole, m) #on attache la classe movie a l'objet list widget
            
            # ajout du movie dans le widget liste 
            self.lw_listeFilm.addItem(lw_item)
    
    def add_movie(self):

        movie_title = self.led_writeFilm.text() #recupere le titre dun film
        if not movie_title:
            """si pas de titre inscrit"""
            return False
        
        # on cree une instance de la classe movie avec notre titre    
        movie = Movie(title=movie_title)
        resultat = movie.add_to_movies() #booleen si l'element est present dans la liste

        if resultat == True :
            """si le film n'est pas dans la liste alors on l'ajoute"""
            # on va stocker la classe en tant qu'item
            lw_item = QtWidgets.QListWidgetItem(movie.title) #on cree un list widget item
            lw_item.setData(QtCore.Qt.UserRole, movie)  #on attache la classe movie a l'objet list widget
            self.lw_listeFilm.addItem(lw_item)      #ajout du movie dans le widget liste 

        # on vide le texte du line edit
        self.led_writeFilm.setText("")
    

    def remove_movie(self):

        for selected_item in self.lw_listeFilm.selectedItems():
            """on boucle sur les film selectionne avec le curseur dans notre list widget.
            On peut en select plusieurs grace a selectedItems"""

            #on recupere l'instance de notre film qui est stocke grace a ".data"
            movie = selected_item.data(QtCore.Qt.UserRole)
            #methode de ma classe movie pour supprimer un film
            movie.remove_from_movies()
            
            # ".takeItem permet d'enelver un element de la list widget selon son indice"
            self.lw_listeFilm.takeItem(self.lw_listeFilm.row(selected_item))

# create an application
app = QtWidgets.QApplication([])
# create a window on my app
win = App()
win.show()
# execute the app
app.exec_() 