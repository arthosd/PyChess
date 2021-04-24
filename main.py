# Point d'entrée du jeu d'échec
from src.GameEngine.ChessBoard import ChessBoard
from src.GameEngine.Pawn import Pawn
from src.FileEngine.load import serialize_object, load_object

chessBoard = ChessBoard()
# chessBoard.draw_board()

# serialize_object(chessBoard)

# chessBoard.play()

chessBoard = load_object()

chessBoard.draw_board()
