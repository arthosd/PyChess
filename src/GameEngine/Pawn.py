"""
Class qui va contenir un les données sur un pion
"""
from src.GameEngine.Position import tulpe_position


class Pawn:

    def __init__(self, pawn_type, position):
        self._pawn_type = pawn_type      # Le type de la pièce
        # Tuple contenant la position de la pièces
        self._position = tulpe_position(position[0], position[1])
        # Les movement qui sont autorisées
        self._is_white = self._determinate_color(pawn_type)  # Boolean
        self._allowed_moves = self._bishop_moves_generation(
            self._position)

    def _simple_pawn_moves_generation(self, new_position):
        """
        Genère les positions du pions.

        On renvoie un dictionnaire contenant les mouvements possibles
        """

        mouvement = []          # Va contenir tous les mouvements possibles
        eatable_moves = []      # Contient les mouvements pour manger

        if self._is_white == False:  # Si le pion est blanc

            # Le tuple contenant la position du pion
            posX, posY = new_position

            new_pos = (posX, posY-1)

            if new_pos[1] >= 0 and new_pos[1] <= 7:
                # Le mouvement en avant du pion
                mouvement.append(new_pos)

                # Position pour manger
                if new_pos[0] - 1 >= 0:
                    eatable_moves.append((posX-1, posY-1))

                if new_pos[0] + 1 <= 7:
                    eatable_moves.append((posX+1, posY-1))

        else:  # S'il est noir

            # Le tuple contenant la position du pion
            posX, posY = new_position

            new_pos = (posX, posY+1)

            if new_pos[1] >= 0 and new_pos[1] <= 7:
                # Le mouvement en avant du pion
                mouvement.append(new_pos)

                # Position pour manger
                if new_pos[0] - 1 >= 0:
                    eatable_moves.append((posX-1, posY-1))

                if new_pos[0] + 1 <= 7:
                    eatable_moves.append((posX+1, posY-1))

        return {"moves": mouvement, "eat_moves": eatable_moves}

    def _bishop_moves_generation(self, new_position):
        """
        Genère les positions du bishop
        """

        tab = []
        stop_generating = False
        pos = new_position

        # Generate up left
        while stop_generating == False:

            pos = (pos[0]-1, pos[1]+1)

            if pos[0] >= 0 and pos[0] <= 7 and pos[1] >= 0 and pos[1] <= 7:
                tab.append(pos)
            else:
                stop_generating = True

        stop_generating = False  # Restart

        # Generate up right
        while stop_generating == False:

            pos = (pos[0]+1, pos[1]-1)

            if pos[0] >= 0 and pos[0] <= 7 and pos[1] >= 0 and pos[1] <= 7:
                tab.append(pos)
            else:
                stop_generating = True

        stop_generating = False  # Restart

        # Generate down left
        while stop_generating == False:

            pos = (pos[0]+1, pos[1]+1)

            if pos[0] >= 0 and pos[0] <= 7 and pos[1] >= 0 and pos[1] <= 7:
                tab.append(pos)
            else:
                stop_generating = True

        stop_generating = False  # Restart

        # Generate down rigth
        while stop_generating == False:

            pos = (pos[0]-1, pos[1]+1)

            if pos[0] >= 0 and pos[0] <= 7 and pos[1] >= 0 and pos[1] <= 7:
                tab.append(pos)
            else:
                stop_generating = True

        return {"moves": tab, "eat_moves": tab}

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
        print(first_letter)

        if first_letter == "w":
            return True
        else:
            return False

    def resume(self):
        print("\t"+str(self._pawn_type))
        print("\t"+str(self._position))
        print("\t"+str(self._is_white))
