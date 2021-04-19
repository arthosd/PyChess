from src.GameEngine.Position import tulpe_position


class Pawn:
    """
    Class qui va contenir un les données sur un pion
    """

    def __init__(self, pawn_type, position):
        self._pawn_type = pawn_type      # Le type de la pièce
        # Tuple contenant la position de la pièces
        self._position = tulpe_position(position[0], position[1])
        # Les movement qui sont autorisées
        self._is_white = self._determinate_color(pawn_type)  # Boolean
        self._allowed_moves = self._generate_new_moves(
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

        tab = []  # Va contenir les positions généré
        pos = new_position

        # La ligne supérieur
        for i in range(-1, 2, 1):

            temp_pos = (pos[0]+i, pos[1]+1)

            if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7:
                tab.append(temp_pos)

        # La ligne inférieur
        for i in range(-1, 2, 1):
            temp_pos = (pos[0]+i, pos[1]-1)

            if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7:
                tab.append(temp_pos)

        # Faire les deux cotés manquants

        temp_pos = (pos[0]-1, pos[1])

        if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7:
            tab.append(temp_pos)

        temp_pos = (pos[0]+1, pos[1])

        if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7:
            tab.append(temp_pos)

        return {"moves": tab, "eat_moves": tab}

    def _queen_moves_generation(self, new_position):
        """
        Genère les positions du roi
        """

        tab = []                    # Va contenir les positions généré
        pos = new_position          # La position du pion
        stop_generating = False     # Pour stopper les boucles

        temp_pos = pos

        # On fait l'horizontal - gauche
        while stop_generating == False:

            temp_pos = (temp_pos[0]-1, temp_pos[1])

            if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7:
                tab.append(temp_pos)
            else:
                stop_generating = True

        stop_generating = False

        # On fait l'horizontal - droit
        while stop_generating == False:

            temp_pos = (temp_pos[0]+1, temp_pos[1])

            if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7:
                tab.append(temp_pos)
            else:
                stop_generating = True

        stop_generating = False

        # On fait la vertical - bas
        while stop_generating == False:

            temp_pos = (temp_pos[0], temp_pos[1]+1)

            if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7:
                tab.append(temp_pos)
            else:
                stop_generating = True

        stop_generating = False

        # On fait la vertical - haut
        while stop_generating == False:

            temp_pos = (temp_pos[0], temp_pos[1]-1)

            if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7:
                tab.append(temp_pos)
            else:
                stop_generating = True

        # On reprend les mouvements du fou
        bishop_moves = self._bishop_moves_generation(pos)

        return {"moves": tab + bishop_moves["moves"], "eat_moves": tab + bishop_moves["eat_moves"]}

    def _knight_moves_generation(self, new_position):
        """
        Genère les positions du cavalier
        """

        tab = []                    # Va contenir les positions généré
        pos = new_position          # La position du pion

        # Haut

        temp_pos = (pos[0]-1, pos[1]+2)  # Gauche

        if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7:
            tab.append(temp_pos)

        temp_pos = (pos[0]+1, pos[1]+2)  # Droit

        if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7:
            tab.append(temp_pos)

        # Droit
        temp_pos = (pos[0]+2, pos[1]-1)  # Haut

        if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7:
            tab.append(temp_pos)

        temp_pos = (pos[0]+2, pos[1]+1)  # Bas

        if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7:
            tab.append(temp_pos)

        # Bas
        temp_pos = (pos[0]+1, pos[1]-2)  # Droit

        if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7:
            tab.append(temp_pos)

        temp_pos = (pos[0]-1, pos[1]-2)  # Gauche

        if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7:
            tab.append(temp_pos)

        # Gauche
        temp_pos = (pos[0]-2, pos[1]-1)  # Haut

        if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7:
            tab.append(temp_pos)

        temp_pos = (pos[0]-2, pos[1]+1)  # Bas

        if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7:
            tab.append(temp_pos)

        return {"moves": tab, "eat_moves": tab}

    def _rook_moves_generation(self, new_position):
        """
        Genère les positions de la tour
        """

        tab = []                    # Va contenir les positions généré
        pos = new_position          # La position du pion
        stop_generating = False     # Pour stopper les boucles

        temp_pos = pos

        # On fait l'horizontal - gauche
        while stop_generating == False:

            temp_pos = (temp_pos[0]-1, temp_pos[1])

            if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7:
                tab.append(temp_pos)
            else:
                stop_generating = True

        stop_generating = False

        # On fait l'horizontal - droit
        while stop_generating == False:

            temp_pos = (temp_pos[0]+1, temp_pos[1])

            if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7:
                tab.append(temp_pos)
            else:
                stop_generating = True

        stop_generating = False

        # On fait la vertical - bas
        while stop_generating == False:

            temp_pos = (temp_pos[0], temp_pos[1]+1)

            if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7:
                tab.append(temp_pos)
            else:
                stop_generating = True

        stop_generating = False

        # On fait la vertical - haut
        while stop_generating == False:

            temp_pos = (temp_pos[0], temp_pos[1]-1)

            if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7:
                tab.append(temp_pos)
            else:
                stop_generating = True

        return {"moves": tab, "eat_moves": tab}

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
        # On modifie la position de la pièce actuelle
        self._position = tulpe_position(position[0], position[1])
        # On génère les nouvelles positions
        self._allowed_moves = self._generate_new_moves(
            tulpe_position(position[0], position[1]))

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
