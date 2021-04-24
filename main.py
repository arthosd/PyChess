# Point d'entrée du jeu d'échec
from src.GameEngine.ChessBoard import ChessBoard
from src.GameEngine.Pawn import Pawn
from src.FileEngine.load import load_object, is_there_saved_game

chessBoard = None

print("Welcome to pychess !")

if is_there_saved_game() == False:
    print("You have no saved game !")
    print("Be aware that you can save at the beggining of your turn by typing save while choosing pawn.")
    chessBoard = ChessBoard()

else:
    answer = input("You have saved a game, do you want to load it ? (y/n) : ")

    if answer == "y" or answer == "Y":
        # On load le pickle file
        chessBoard = load_object()
        print(chessBoard.white_to_move)
    else:
        # On réinitialise la game
        chessBoard = ChessBoard()

chessBoard.draw_board()
chessBoard.play()
