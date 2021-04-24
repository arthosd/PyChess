# Point d'entrée du jeu d'échec
from src.GameEngine.ChessBoard import ChessBoard
from src.GameEngine.Pawn import Pawn

chessBoard = ChessBoard()
chessBoard.draw_board()

chessBoard.play()
