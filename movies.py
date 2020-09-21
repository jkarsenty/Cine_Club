import os
import json
import logging
import pprint

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR,"data","movies.json")

def get_movies():

    """fonction pour recuperer tous les films.
    L'appel de cette fonction cree une instance de Movie pour chaque film."""

    # ouverture du fichier de notre liste de films
    with open(DATA_FILE,"r") as f:
        movies_list = json.load(f)

    # notre liste des instances
    movies = [Movie(m)for m in movies_list] 
    return movies

class Movie:
    """
    class of our movie
    """
    def __init__(self,title):
        self.title = title.title() #title() pour avoir des majuscules en debut de mot

    def __str__(self):
        return self.title

    def _get_movies(self):
        """methode interne a notre classe : 
        Recuperer les infos du fichier movies.json
        """
        with open(DATA_FILE,"r") as f:
            return json.load(f)

    def _write_movies(self, movies):
        """methode interne a notre classe : 
        Ecrire les infos dans le fichier movies.json
        """
        with open(DATA_FILE,"w") as f:
            json.dump(movies, f, indent=4)

    def add_to_movies(self):
        """methode pour ajouter un film a notre liste"""
        
        # Recuperation de la liste des films
        movies_list = self._get_movies()

        # Ajout du film
        if self.title not in movies_list :
            """si le film n'est pas dans la liste"""
            movies_list.append(self.title)
            self._write_movies(movies_list)
            return True

        else :
            """si le film est deja dans la liste"""
            logging.warning(f"le film {self.title} est déjà dans la liste")
            return False

    def remove_from_movies(self):

        """methode pour supprimer un film de la liste"""

        # Recuperation de la liste des films
        movies_list = self._get_movies()

        # Suppression du films
        if self.title in movies_list :
            """si le film est dans la liste"""
            movies_list.remove(self.title)
            self._write_movies(movies_list) #on reecrie la liste sans le film efface
            return True

        else : 
            """si le film n'est pas dans la liste"""
            logging.warning(f"le film {self.title} n'etait pas dans la liste")
            return False

if __name__ == "__main__":
    m = Movie("hunger game")
    m.add_to_movies()
    movies = get_movies()
    pprint.pprint(movies)