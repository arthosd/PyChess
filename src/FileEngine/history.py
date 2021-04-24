"""
Fichier contenant toutes les fonctions d'enregistrement de l'historique de mouvement.
"""
import sys

# la liste des arguments passé sur la console
arguments = sys.argv
# Le chemin d'accès vers le fichier
file_path = "history.txt"

if len(arguments) > 1:
    file_path = arguments[1]

history_file = open(file_path, "w")


def write_in_history(text_to_write):
    """
    Ecrit du texte à la suite du fichier
    """
    history_file.writelines(text_to_write+"\n")


def close_file():
    """
    Ferme le flux vers le fichier
    """
    history_file.close()
