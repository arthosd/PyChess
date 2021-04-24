"""
Tablier du jeu d'échec
"""
from src.GameEngine.Pawn import Pawn
from src.GameEngine.Position import tulpe_position


class ChessBoard:

    def __init__(self, state=[]):
        # Les pions qui sont sur le tablier
        self.state = self._generate_state(state)
        self.white_to_move = True   # Les pions blanc joue
        self.white_points = []      # Tableau qui va contenir les pions mangé par les blancs
        self.black_points = []      # Tableau qui va contenir les pions mangé par les blancs

    def _simple_pawn_moves_generation(self, pawn, new_position):
        """
        Genère les positions du pions.
        """

        is_first_move = pawn.get_first_move()

        mouvement = []          # Va contenir tous les mouvements possibles

        if pawn._is_white == True:  # Si le pion est blanc

            # Le tuple contenant la position du pion
            posX, posY = new_position

            if is_first_move == True:
                new_pos = (posX, posY-2)
                if new_pos[1] >= 0 and new_pos[1] <= 7 and self._is_there_pawn_at_position(new_pos) == False:
                    # Le mouvement en avant du pion
                    mouvement.append(new_pos)

            new_pos = (posX, posY-1)

            if new_pos[1] >= 0 and new_pos[1] <= 7 and self._is_there_pawn_at_position(new_pos) == False:
                # Le mouvement en avant du pion
                mouvement.append(new_pos)

            # Vérifier qu'il y a un pion dans les digonales

            new_pos = (posX+1, posY + 1)

            if self._is_there_pawn_at_position(new_pos) == True:

                temp_pawn = self._get_pawn_at(new_pos)  # On récupère le pion

                if temp_pawn.get_is_white() != pawn.get_is_white():  # S'il est de couleur différente du pion
                    mouvement.append(new_pos)

            new_pos = (posX - 1, posY + 1)

            if self._is_there_pawn_at_position(new_pos) == True:

                temp_pawn = self._get_pawn_at(new_pos)  # On récupère le pion

                if temp_pawn.get_is_white() != pawn.get_is_white():  # S'il est de couleur différente du pion
                    mouvement.append(new_pos)

        else:  # S'il est noir
            # Le tuple contenant la position du pion

            posX, posY = new_position

            if is_first_move == True:
                new_pos = (posX, posY+2)
                if new_pos[1] >= 0 and new_pos[1] <= 7 and self._is_there_pawn_at_position(new_pos) == False:
                    # Le mouvement en avant du pion
                    mouvement.append(new_pos)

            posX, posY = new_position

            new_pos = (posX, posY+1)

            if new_pos[1] >= 0 and new_pos[1] <= 7 and self._is_there_pawn_at_position(new_pos) == False:
                # Le mouvement en avant du pion
                mouvement.append(new_pos)

            # Il faut faire les mouvement de manger

            new_pos = (posX+1, posY - 1)

            if self._is_there_pawn_at_position(new_pos) == True:

                temp_pawn = self._get_pawn_at(new_pos)  # On récupère le pion

                if temp_pawn.get_is_white() != pawn.get_is_white():  # S'il est de couleur différente du pion
                    mouvement.append(new_pos)

            new_pos = (posX - 1, posY - 1)

            if self._is_there_pawn_at_position(new_pos) == True:

                temp_pawn = self._get_pawn_at(new_pos)  # On récupère le pion

                if temp_pawn.get_is_white() != pawn.get_is_white():  # S'il est de couleur différente du pion
                    mouvement.append(new_pos)

        return mouvement

    def _bishop_moves_generation(self, pawn, new_position):
        """
        Genère les positions du bishop
        """

        tab = []
        stop_generating = False
        pos = new_position

        # Generate up left
        while stop_generating == False:

            pos = (pos[0]-1, pos[1]+1)

            if pos[0] >= 0 and pos[0] <= 7 and pos[1] >= 0 and pos[1] <= 7 and self._is_there_pawn_at_position(pos) == False:
                tab.append(pos)
            else:
                # S'il y a quelqu'un à cette position
                if self._is_there_pawn_at_position(pos) == True:
                    # Si c'est un pion adversaire on le rajoute aux mouvements possibles
                    if self._get_pawn_at(pos).get_is_white() != pawn.get_is_white():
                        tab.append(pos)

                stop_generating = True

        stop_generating = False  # Restart

        # Generate up right
        while stop_generating == False:

            pos = (pos[0]+1, pos[1]-1)

            if pos[0] >= 0 and pos[0] <= 7 and pos[1] >= 0 and pos[1] <= 7 and self._is_there_pawn_at_position(pos) == False:
                tab.append(pos)
            else:
                # S'il y a quelqu'un à cette position
                if self._is_there_pawn_at_position(pos) == True:
                    # Si c'est un pion adversaire on le rajoute aux mouvements possibles
                    if self._get_pawn_at(pos).get_is_white() != pawn.get_is_white():
                        tab.append(pos)

                stop_generating = True

        stop_generating = False  # Restart

        # Generate down left
        while stop_generating == False:

            pos = (pos[0]+1, pos[1]+1)

            if pos[0] >= 0 and pos[0] <= 7 and pos[1] >= 0 and pos[1] <= 7 and self._is_there_pawn_at_position(pos) == False:
                tab.append(pos)
            else:
                # S'il y a quelqu'un à cette position
                if self._is_there_pawn_at_position(pos) == True:
                    # Si c'est un pion adversaire on le rajoute aux mouvements possibles
                    if self._get_pawn_at(pos).get_is_white() != pawn.get_is_white():
                        tab.append(pos)

                stop_generating = True

        stop_generating = False  # Restart

        # Generate down rigth
        while stop_generating == False:

            pos = (pos[0]-1, pos[1]+1)

            if pos[0] >= 0 and pos[0] <= 7 and pos[1] >= 0 and pos[1] <= 7 and self._is_there_pawn_at_position(pos) == False:
                tab.append(pos)
            else:

                # S'il y a quelqu'un à cette position
                if self._is_there_pawn_at_position(pos) == True:
                    # Si c'est un pion adversaire on le rajoute aux mouvements possibles
                    if self._get_pawn_at(pos).get_is_white() != pawn.get_is_white():
                        tab.append(pos)

                stop_generating = True

        # On rajoute les mouvements possibles dans le pion
        return tab

    def _king_moves_generation(self, pawn, new_position):
        """
        Genère les positions du roi
        """

        tab = []  # Va contenir les positions généré
        pos = new_position

        # La ligne supérieur
        for i in range(-1, 2, 1):

            temp_pos = (pos[0]+i, pos[1]+1)

            if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7 and self._is_there_pawn_at_position(temp_pos) == False:
                tab.append(temp_pos)
            else:
                # S'il y a quelqu'un à cette position
                if self._is_there_pawn_at_position(temp_pos) == True:
                    # Si c'est un pion adversaire on le rajoute aux mouvements possibles
                    if self._get_pawn_at(temp_pos).get_is_white() != pawn.get_is_white():
                        tab.append(temp_pos)

        print(tab)

        # La ligne inférieur
        for i in range(-1, 2, 1):
            temp_pos = (pos[0]+i, pos[1]-1)

            if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7 and self._is_there_pawn_at_position(temp_pos) == False:
                tab.append(temp_pos)
                print("AJout")
            else:
                # S'il y a quelqu'un à cette position
                if self._is_there_pawn_at_position(temp_pos) == True:
                    # Si c'est un pion adversaire on le rajoute aux mouvements possibles
                    if self._get_pawn_at(temp_pos).get_is_white() != pawn.get_is_white():
                        print(pawn.get_is_white())
                        tab.append(temp_pos)
                        print("AJout")

        # Faire les deux cotés manquants

        print(tab)

        temp_pos = (pos[0]-1, pos[1])

        if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7 and self._is_there_pawn_at_position(temp_pos) == False:
            tab.append(temp_pos)
        else:
            # S'il y a quelqu'un à cette position
            if self._is_there_pawn_at_position(temp_pos) == True:
                # Si c'est un pion adversaire on le rajoute aux mouvements possibles
                if self._get_pawn_at(temp_pos).get_is_white() != pawn.get_is_white():
                    tab.append(temp_pos)

        temp_pos = (pos[0]+1, pos[1])

        if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7 and self._is_there_pawn_at_position(temp_pos) == False:
            tab.append(temp_pos)
        else:
            # S'il y a quelqu'un à cette position
            if self._is_there_pawn_at_position(temp_pos) == True:
                # Si c'est un pion adversaire on le rajoute aux mouvements possibles
                if self._get_pawn_at(temp_pos).get_is_white() != pawn.get_is_white():
                    tab.append(temp_pos)

        return tab

    def _queen_moves_generation(self, pawn, new_position):
        """
        Genère les positions de la reine
        """

        tab = []                    # Va contenir les positions généré
        pos = new_position          # La position du pion
        stop_generating = False     # Pour stopper les boucles

        temp_pos = pos

        # On fait l'horizontal - gauche
        while stop_generating == False:

            temp_pos = (temp_pos[0]-1, temp_pos[1])

            if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7 and self._is_there_pawn_at_position(temp_pos) == False:
                tab.append(temp_pos)
            else:
                # S'il y a quelqu'un à cette position
                if self._is_there_pawn_at_position(temp_pos) == True:
                    # Si c'est un pion adversaire on le rajoute aux mouvements possibles
                    if self._get_pawn_at(temp_pos).get_is_white() != pawn.get_is_white():
                        tab.append(temp_pos)

                stop_generating = True

        stop_generating = False

        # On fait l'horizontal - droit
        while stop_generating == False:

            temp_pos = (temp_pos[0]+1, temp_pos[1])

            if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7 and self._is_there_pawn_at_position(temp_pos) == False:
                tab.append(temp_pos)
            else:
                # S'il y a quelqu'un à cette position
                if self._is_there_pawn_at_position(temp_pos) == True:
                    # Si c'est un pion adversaire on le rajoute aux mouvements possibles
                    if self._get_pawn_at(temp_pos).get_is_white() != pawn.get_is_white():
                        tab.append(temp_pos)

                stop_generating = True

        stop_generating = False

        # On fait la vertical - bas
        while stop_generating == False:

            temp_pos = (temp_pos[0], temp_pos[1]+1)

            if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7 and self._is_there_pawn_at_position(temp_pos) == False:
                tab.append(temp_pos)
            else:
                # S'il y a quelqu'un à cette position
                if self._is_there_pawn_at_position(temp_pos) == True:
                    # Si c'est un pion adversaire on le rajoute aux mouvements possibles
                    if self._get_pawn_at(temp_pos).get_is_white() != pawn.get_is_white():
                        tab.append(temp_pos)
                stop_generating = True

        stop_generating = False

        # On fait la vertical - haut
        while stop_generating == False:

            temp_pos = (temp_pos[0], temp_pos[1]-1)

            if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7 and self._is_there_pawn_at_position(temp_pos) == False:
                tab.append(temp_pos)
            else:
                # S'il y a quelqu'un à cette position
                if self._is_there_pawn_at_position(temp_pos) == True:
                    # Si c'est un pion adversaire on le rajoute aux mouvements possibles
                    if self._get_pawn_at(temp_pos).get_is_white() != pawn.get_is_white():
                        tab.append(temp_pos)

                stop_generating = True

        # On reprend les mouvements du fou
        bishop_moves = self._bishop_moves_generation(pawn, pos)

        tab = tab + bishop_moves

        return tab

    def _knight_moves_generation(self, pawn, new_position):
        """
        Genère les positions du cavalier
        """

        tab = []                    # Va contenir les positions généré
        pos = new_position          # La position du pion

        # Haut

        temp_pos = (pos[0]-1, pos[1]+2)  # Gauche

        if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7 and self._is_there_pawn_at_position(temp_pos) == False:
            tab.append(temp_pos)
        else:
            # S'il y a quelqu'un à cette position
            if self._is_there_pawn_at_position(temp_pos) == True:
                # Si c'est un pion adversaire on le rajoute aux mouvements possibles
                if self._get_pawn_at(temp_pos).get_is_white() != pawn.get_is_white():
                    tab.append(temp_pos)

        temp_pos = (pos[0]+1, pos[1]+2)  # Droit

        if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7 and self._is_there_pawn_at_position(temp_pos) == False:
            tab.append(temp_pos)
        else:
            # S'il y a quelqu'un à cette position
            if self._is_there_pawn_at_position(temp_pos) == True:
                # Si c'est un pion adversaire on le rajoute aux mouvements possibles
                if self._get_pawn_at(temp_pos).get_is_white() != pawn.get_is_white():
                    tab.append(temp_pos)

        # Droit
        temp_pos = (pos[0]+2, pos[1]-1)  # Haut

        if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7 and self._is_there_pawn_at_position(temp_pos) == False:
            tab.append(temp_pos)
        else:
            # S'il y a quelqu'un à cette position
            if self._is_there_pawn_at_position(temp_pos) == True:
                # Si c'est un pion adversaire on le rajoute aux mouvements possibles
                if self._get_pawn_at(temp_pos).get_is_white() != pawn.get_is_white():
                    tab.append(temp_pos)

        temp_pos = (pos[0]+2, pos[1]+1)  # Bas

        if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7 and self._is_there_pawn_at_position(temp_pos) == False:
            tab.append(temp_pos)
        else:
            # S'il y a quelqu'un à cette position
            if self._is_there_pawn_at_position(temp_pos) == True:
                # Si c'est un pion adversaire on le rajoute aux mouvements possibles
                if self._get_pawn_at(temp_pos).get_is_white() != pawn.get_is_white():
                    tab.append(temp_pos)

        # Bas
        temp_pos = (pos[0]+1, pos[1]-2)  # Droit

        if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7 and self._is_there_pawn_at_position(temp_pos) == False:
            tab.append(temp_pos)
        else:
            # S'il y a quelqu'un à cette position
            if self._is_there_pawn_at_position(temp_pos) == True:
                # Si c'est un pion adversaire on le rajoute aux mouvements possibles
                if self._get_pawn_at(temp_pos).get_is_white() != pawn.get_is_white():
                    tab.append(temp_pos)

        temp_pos = (pos[0]-1, pos[1]-2)  # Gauche

        if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7 and self._is_there_pawn_at_position(temp_pos) == False:
            tab.append(temp_pos)
        else:
            # S'il y a quelqu'un à cette position
            if self._is_there_pawn_at_position(temp_pos) == True:
                # Si c'est un pion adversaire on le rajoute aux mouvements possibles
                if self._get_pawn_at(temp_pos).get_is_white() != pawn.get_is_white():
                    tab.append(temp_pos)

        # Gauche
        temp_pos = (pos[0]-2, pos[1]-1)  # Haut

        if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7 and self._is_there_pawn_at_position(temp_pos) == False:
            tab.append(temp_pos)
        else:
            # S'il y a quelqu'un à cette position
            if self._is_there_pawn_at_position(temp_pos) == True:
                # Si c'est un pion adversaire on le rajoute aux mouvements possibles
                if self._get_pawn_at(temp_pos).get_is_white() != pawn.get_is_white():
                    tab.append(temp_pos)

        temp_pos = (pos[0]-2, pos[1]+1)  # Bas

        if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7 and self._is_there_pawn_at_position(temp_pos) == False:
            tab.append(temp_pos)
        else:
            # S'il y a quelqu'un à cette position
            if self._is_there_pawn_at_position(temp_pos) == True:
                # Si c'est un pion adversaire on le rajoute aux mouvements possibles
                if self._get_pawn_at(temp_pos).get_is_white() != pawn.get_is_white():
                    tab.append(temp_pos)

        return tab

    def _rook_moves_generation(self, pawn, new_position):
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

            if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7 and self._is_there_pawn_at_position(temp_pos) == False:
                tab.append(temp_pos)
            else:
                # S'il y a quelqu'un à cette position
                if self._is_there_pawn_at_position(temp_pos) == True:
                    # Si c'est un pion adversaire on le rajoute aux mouvements possibles
                    if self._get_pawn_at(temp_pos).get_is_white() != pawn.get_is_white():
                        tab.append(temp_pos)
                stop_generating = True

        stop_generating = False

        # On fait l'horizontal - droit
        while stop_generating == False:

            temp_pos = (temp_pos[0]+1, temp_pos[1])

            if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7 and self._is_there_pawn_at_position(temp_pos) == False:
                tab.append(temp_pos)
            else:
                # S'il y a quelqu'un à cette position
                if self._is_there_pawn_at_position(temp_pos) == True:
                    # Si c'est un pion adversaire on le rajoute aux mouvements possibles
                    if self._get_pawn_at(temp_pos).get_is_white() != pawn.get_is_white():
                        tab.append(temp_pos)

                stop_generating = True

        stop_generating = False

        # On fait la vertical - bas
        while stop_generating == False:

            temp_pos = (temp_pos[0], temp_pos[1]+1)

            if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7 and self._is_there_pawn_at_position(temp_pos) == False:
                tab.append(temp_pos)
            else:
                # S'il y a quelqu'un à cette position
                if self._is_there_pawn_at_position(temp_pos) == True:
                    # Si c'est un pion adversaire on le rajoute aux mouvements possibles
                    if self._get_pawn_at(temp_pos).get_is_white() != pawn.get_is_white():
                        tab.append(temp_pos)

                stop_generating = True

        stop_generating = False

        # On fait la vertical - haut
        while stop_generating == False:

            temp_pos = (temp_pos[0], temp_pos[1]-1)

            if temp_pos[0] >= 0 and temp_pos[0] <= 7 and temp_pos[1] >= 0 and temp_pos[1] <= 7 and self._is_there_pawn_at_position(temp_pos) == False:
                tab.append(temp_pos)
            else:
                # S'il y a quelqu'un à cette position
                if self._is_there_pawn_at_position(temp_pos) == True:
                    # Si c'est un pion adversaire on le rajoute aux mouvements possibles
                    if self._get_pawn_at(temp_pos).get_is_white() != pawn.get_is_white():
                        tab.append(temp_pos)

                stop_generating = True

        return tab

    def _generate_moves(self, pawn):
        """
        On génere les moves possibles pour le pions
        """

        if pawn.get_pawn_type()[1] == "p":  # si'cest un simple paw
            return self._simple_pawn_moves_generation(pawn, pawn.get_position())

        elif pawn.get_pawn_type()[1] == "b":  # Si c'est un bishop
            return self._bishop_moves_generation(pawn, pawn.get_position())

        elif pawn.get_pawn_type()[1] == "Q":  # Si c'est la Queen
            return self._queen_moves_generation(pawn, pawn.get_position())

        elif pawn.get_pawn_type()[1] == "K":  # Si c'est le King
            return self._king_moves_generation(pawn, pawn.get_position())

        elif pawn.get_pawn_type()[1] == "k":  # Si c'est un knight
            return self._knight_moves_generation(pawn, pawn.get_position())

        else:  # Si c'est le rook
            return self._rook_moves_generation(pawn, pawn.get_position())

        pass

    def _get_pawn_at(self, positon):
        """
        Récupère le pion à la position donnée en argument.
        Renvoie None s'il n'y a pas de pion.
        """

        for white in self.state[0]:  # On itère sur les blancs
            if positon == white.get_position():
                return white

        for black in self.state[1]:  # On itère sur les pions noirs
            if positon == black.get_position():
                return black

        return None

    def _select_pawn(self, is_white):

        is_pawn_selected = False

        if is_white == True:
            print("White moves.")
        else:
            print("Black moves.")

        while is_pawn_selected == False:

            position = input("Indicate piece position: ")
            position = tulpe_position(position[0], position[1])
            pawn = self._get_pawn_at(position)

            # Si le pion existe et qu'il est de la meme couleur que le joueur
            if pawn != None and pawn.get_is_white() == is_white:
                moves = self._generate_moves(pawn)

                if len(moves) != 0:
                    return (pawn, moves)
                else:
                    print("Pas de position possible pour cette pièce")
            else:
                if pawn == None:
                    print("No piece at this position.")
                else:
                    print("It's not your piece")

    def _select_destination(self, pawn, moves):
        """
        Demande à l'utilisateur de choisir une position
        et vérifie que cette position est autorisé.
        """

        destination_selected = False

        while destination_selected == False:

            destination = input("Indicate destination: ")
            destination = tulpe_position(destination[0], destination[1])

            is_allowed = self._allow_movement(pawn, moves, destination)

            if is_allowed == True:
                return destination
            else:
                print("Forbidden mouvement.", end=" ")

        return None

    def _eat(self, pawn):
        """
        Eat pawn 
        """

        pawn_color = pawn.get_is_white()

        if pawn_color == True:  # S'il est blanc
            # On cherche dans les Blancs

            compteur = 0

            for white in self.state[0]:
                if white == pawn:
                    print(self.state[0].pop(compteur))

                compteur = compteur + 1
        else:  # S'il est noir
            # On change dans les noirs
            compteur = 0

            for white in self.state[1]:
                if white == pawn:
                    print(self.state[1].pop(compteur))

                compteur = compteur + 1

    def _eatOrMove(self, pawn, destination):
        """
        Vérifie s'il y a un pion à manger sur le terrain à la destination donné.
        Sinon juste fait bouger le pion à la position donner
        """

        destination_pawn = self._get_pawn_at(destination)

        if destination_pawn == None:
            # On bouge le pion
            pawn.move_to(destination)
        else:
            self._eat(destination_pawn)

    def play(self):
        """
        Fonction principale pour le jeu
        """

        stop_game = False                   # Décide de stopper ou non le jeu

        while stop_game == False:

            pawn_selected, moves = self._select_pawn(
                self.white_to_move)    # On choisi un pion
            destination = self._select_destination(
                pawn_selected, moves)  # On choisi un destination

            self._eatOrMove(pawn_selected, destination)

            self.draw_board()

            self.white_to_move = not self.white_to_move  # C'est à l'autre équipe de jouer

    def _is_pawn_eatable(self, pawn):
        """
        Vérifie s'il n'y a pas déjà un pion à cet endroit.
        return le pion, None Sinon
        """
        pass

    def _generate_state(self, state):
        """
        Génère le state initial si ce dernier est vide
        """

        if len(state) == 0:
            # On met la fonction de génration ici

            chess_board = [  # Matrice [2][16] , les 0 c'est les blancs
                [
                    Pawn("wr", "a1"),
                    Pawn("wk", "b1"),
                    Pawn("wb", "c1"),
                    Pawn("wQ", "d1"),
                    Pawn("wK", "e1"),
                    Pawn("wb", "f1"),
                    Pawn("wk", "g1"),
                    Pawn("wr", "h1"),
                    Pawn("wp", "a2"),
                    Pawn("wp", "b2"),
                    Pawn("wp", "c2"),
                    Pawn("wp", "d2"),
                    Pawn("wp", "e2"),
                    Pawn("wp", "f2"),
                    Pawn("wp", "g2"),
                    Pawn("wp", "h2"),
                ],
                [
                    Pawn("br", "a8"),
                    Pawn("bk", "b8"),
                    Pawn("bb", "c8"),
                    Pawn("bQ", "d8"),
                    Pawn("bK", "e8"),
                    Pawn("bb", "f8"),
                    Pawn("bk", "g8"),
                    Pawn("br", "h8"),
                    Pawn("bp", "a7"),
                    Pawn("bp", "b7"),
                    Pawn("bp", "c7"),
                    Pawn("bp", "d7"),
                    Pawn("bp", "e7"),
                    Pawn("bp", "f7"),
                    Pawn("bp", "g7"),
                    Pawn("bp", "h7"),
                ]
            ]

            return chess_board

        else:
            return state

    def _allow_movement(self, pawn, moves, to_position):
        """
        On donne le pion qui va bouger ainsi que la position à laquelle il doit aller
        """

        mouvements = moves  # On génre les moves possibles

        for move in mouvements:
            if to_position == move:
                return True

        return False

    def _is_there_pawn_at_position(self, positon):
        """
        Renvoie True s'il y a un pion à la posiiton données.
        False Sinon.
        """

        whites = self.state[0]
        blacks = self.state[1]

        for pawn in whites:
            if pawn.get_position() == positon:
                return True

        for pawn in blacks:
            if pawn.get_position() == positon:
                return True

        return False

    def draw_board(self):
        """
        dessine le board
        """

        # On commence à mettre dans une matrice les coordonnées
        drawing_board = [
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
        ]

        # On place les blancs
        for white in self.state[0]:

            posx = white.get_position()[1]  # La position X du pawn
            posY = white.get_position()[0]  # La position Y du pawn

            drawing_board[posx][posY] = white.get_pawn_type()  # Le nom du pion

        # On place les Noirs
        for black in self.state[1]:

            posx = black.get_position()[1]  # La position X du pawn
            posY = black.get_position()[0]  # La position Y du pawn

            drawing_board[posx][posY] = black.get_pawn_type()  # Le nom du pion

        for rows in drawing_board:
            for element in rows:
                print("|  "+element, sep=' \t', end='\t')

            print("|", end="\n")

            for compteur in range(8):
                if compteur == 7:
                    print("|-------|", end="")
                    pass
                else:
                    print("|-------", end="")
            print("", end="\n")
