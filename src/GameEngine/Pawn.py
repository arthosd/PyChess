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

    def _simple_pawn_moves_generation(self, new_position):
        """
        Genère les positions du pion
        """

        # Limit gauche = 0
        # Limit droite = 7
        # Limit haute = 0
        # Limit basse = 7

        if self._is_white == True:  # Si le pion est blanc

            pass
        else:  # S'il est noir
            pass

    def _bishop_moves_generation(self, new_position):
        """
        Genère les positions du bishop
        """
        pass

    def _king_moves_generation(self, new_position):
        """
        Genère les positions du roi
        """
        pass

    def _queen_moves_generation(self, new_position):
        """
        Genère les positions du roi
        """
        pass

    def _knight_moves_generation(self, new_position):
        """
        Genère les positions du cavalier
        """
        pass

    def _rook_moves_generation(self, new_position):
        """
        Genère les positions de la tour
        """
        pass

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

    def _generate_new_moves(self, pawn_position):
        """
        On detecte le pion qui joue.
        En fonction de ça, on calcul les nouvelles positions
        """

        if self.get_pawn_type()[1] == "p":  # si'cest un simple paw
            pass

        elif self.get_pawn_type()[1] == "b":  # Si c'est un bishop
            pass

        elif self.get_pawn_type()[1] == "Q":  # Si c'est la Queen
            pass

        elif self.get_pawn_type()[1] == "K":  # Si c'est le King
            pass

        elif self.get_pawn_type()[1] == "k":  # Si c'est un knight
            pass

        else:  # Si c'est le rook
            pass
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
