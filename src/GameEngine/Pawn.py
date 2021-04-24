from src.GameEngine.Position import tulpe_position


class Pawn:
    """
    Class qui va contenir un les données sur un pion
    """

    def __init__(self, pawn_type, position):
        self._first_move = True          # Si c'est la premier fois qu'il bouge
        self._pawn_type = pawn_type      # Le type de la pièce
        # Tuple contenant la position de la pièces
        self._position = tulpe_position(position[0], position[1])
        # Les movement qui sont autorisées
        self._is_white = self._determinate_color(pawn_type)  # Boolean
        # Les mouvements autorisés
        self._allowed_moves = []

    def get_allowed_moves(self):
        """
        Retourne le tableau contenant les position légales
        """
        return self._allowed_moves

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
        return self._is_white

    def _generate_new_moves(self, pawn_position):
        """
        On detecte le pion qui joue.
        En fonction de ça, on calcul les nouvelles positions
        """

        if self.get_pawn_type()[1] == "p":  # si'cest un simple paw
            return self._simple_pawn_moves_generation(pawn_position)

        elif self.get_pawn_type()[1] == "b":  # Si c'est un bishop
            return self._bishop_moves_generation(pawn_position)

        elif self.get_pawn_type()[1] == "Q":  # Si c'est la Queen
            return self._queen_moves_generation(pawn_position)

        elif self.get_pawn_type()[1] == "K":  # Si c'est le King
            return self._king_moves_generation(pawn_position)

        elif self.get_pawn_type()[1] == "k":  # Si c'est un knight
            return self._knight_moves_generation(pawn_position)

        else:  # Si c'est le rook
            return self._rook_moves_generation(pawn_position)

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
        if self._first_move == True:
            self._first_move == False

        # On modifie la position de la pièce actuelle
        self._position = position

    def _determinate_color(self, pawn_type):

        first_letter = pawn_type[0]
        print(first_letter)

        if first_letter == "w":
            return True
        else:
            return False

    def set_allowed_moves(self, positions):
        self._allowed_moves = positions

    def get_first_move(self):
        return self._first_move

    def resume(self):
        print("\t"+str(self._pawn_type))
        print("\t"+str(self._position))
        print("\t"+str(self._is_white))
