"""
Class qui va contenir un les données sur un pion
"""
from src.GameEngine.Position import tulpe_position


class Pawn:

    def __init__(self, pawn_type, position):
        self._pawn_type = pawn_type      # Le type de la pièce
        # Tuple contenant la position de la pièces
        self._position = tulpe_position(position[0], position[1])
        self._allowed_moves = []         # Les movement qui sont autorisées
        self._is_white = self._determinate_color(pawn_type)  # Boolean

    def get_pawn_type(self):
        """
        Le nom de la pièce
        """
        return self._pawn_type

    def get_position(self):
        """
        retourne la position du pion
        """
        return self._position

    def get_is_white(self):
        """
        return is white
        """
        return self.get_is_white

    def _generate_new_moves(self, position):
        """
        """
        pass

    def is_move_allowed(self, move_tuple):
        """
        Return True si le tuple de mouvement est dans les mouvements
        du pions.
        Return False Sinon
        """

        for move in self._allowed_moves:
            if move_tuple == move:
                return True

        return False

    def move_to(self, position):
        # Vérifie si le pion peux se déplacer à cet endroit
        # Modifie le self.posiiton
        pass

    def _determinate_color(self, pawn_type):

        first_letter = pawn_type[0]

        if first_letter == "w":
            return True
        else:
            return False

    def resume(self):
        print("\t"+str(self._pawn_type))
        print("\t"+str(self._position))
        print("\t"+str(self._is_white))
