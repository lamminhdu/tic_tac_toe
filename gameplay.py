from player import RandomComputerPlayer, HumanPlayer
from game import TicTacToe


def play(game, x_player, o_player, print_game=True):
    players = {"x": x_player, "o": o_player}
    if print_game:
        game.print_board_nums()
        print("X go first")
        letter = "x"

    while game.empty_square():
        square = players[letter].get_move(game)
        if game.make_move(square, letter):
            if print_game:
                print(f"player {letter} made move to {square}")
                game.print_board()
        if game.current_winner:
            print(f"{game.current_winner} wins!")
            break
        else:
            # switch player
            letter = "o" if letter == "x" else "x"
    if not game.current_winner:
        print("Tie!")

if __name__ == "__main__":
    game = TicTacToe()
    x_player = HumanPlayer("x")
    o_player = RandomComputerPlayer("o")
    play(game, x_player, o_player, True)