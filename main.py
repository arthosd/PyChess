# Point d'entrée du jeu d'échec
from src.GameEngine.ChessBoard import ChessBoard
from src.GameEngine.Pawn import Pawn

#chessBoard = ChessBoard()
# chessBoard.draw_board()

pion = Pawn("bp", "a1")

pion.resume()
print(pion.get_pawn_type()[1])
