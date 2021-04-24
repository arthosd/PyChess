"""
Contient les fonctions sérialisation
"""
import pickle
import os


def create_directory(directory):
    # On vérifie s'il n'existe pas déjà avant de le crée
    if os.path.exists(directory) == False:
        os.mkdir(directory)


def serialize_object(obj, directory="save"):
    """
    Utilise pickle pour sauvgarder l'état d'un objet
    """

    # Crée le dossier s'il n'existe pas
    create_directory(directory)
    fichier = open(directory+"/"+"save.pickle", "wb")
    pickle.dump(obj, fichier)
    fichier.close()


def load_object(file_path="save/save.pickle"):
    """
    Load le fichier pickle et le renvoie
    """

    fichier = open(file_path, "rb")
    obj = pickle.load(fichier)
    fichier.close()

    return obj


def is_there_saved_game(file="save/save.pickle"):
    """
    Retourne Vrai s'il y a une partie déjà sauvegardéé
    """

    if os.path.exists(file) == False:
        return False

    return True
