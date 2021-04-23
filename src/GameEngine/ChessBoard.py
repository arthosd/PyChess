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

    def _select_pawn(self, positon):
        """
        Selectionner un pion en foncton de sa position
        """
        pos = tulpe_position(positon[0], positon[1])

        for white in self.state[0]:  # On itère sur les blancs
            if pos == white.get_position():
                return white

        for black in self.state[1]:
            if pos == black.get_position():
                return black

        return None

    def _get_pawn_at(self, positon):
        """
        Récupère le pion à la position donnée en argument
        """

        for white in self.state[0]:  # On itère sur les blancs
            if positon == white.get_position():
                return white

        for black in self.state[1]:  # On itère sur les pions noirs
            if positon == black.get_position():
                return black

        return None

    def play(self):
        """
        Récupère l'input d'un jouer
        """

        print("Whites moves")
        print("who to move")
        move = input()
        pawn_to_move = self._select_pawn(move)  # Le pion à bouger
        if pawn_to_move == None:
            print("None")
        else:
            print(pawn_to_move.resume())  # On affiche un résumé

        """if self.white_points:
            print("White moves")
            move = input()
            # Il faut faire les vérification sur l'input
        else:
            print("Black moves")
            move = input()
            # Il faut faire les vérification sur l'input"""

        pass

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
                    Pawn("wr", "g1"),
                    Pawn("wk", "h1"),
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
                    Pawn("br", "g8"),
                    Pawn("bk", "h8"),
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

    def _allow_movement(self, can_pawn_move,):
        """
        Vérifie si can_pawn_move = True
        si oui, il vérifie s'il n'y a pas déjà un quelq'un à cette endroit
        si, oui le pions est mangé et il est mit dans les points de l'équipe qui a mangé
        """
        pass

    def _is_there_pawn_at_position(self, positon):
        """
        Renvoie True s'il y a un pion à la posiiton données.
        False Sinon.
        """

        whites = self.state[0]
        blacks = self.state[1]

        for pawn in whites:
            if pawn.get_position == tulpe_position(positon):
                return True

        for pawn in blacks:
            if pawn.get_position == tulpe_position(positon):
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
