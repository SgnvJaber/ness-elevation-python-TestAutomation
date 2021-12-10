#Source:https://www.practicepython.org/solution/2015/11/23/26-check-tic-tac-toe-solutions.html
def check_winner(game):
    winners = {0: "Nobody", 1: "Player 1", 2: "Player 2"}
    for i in range(1, 3):
        # horizontal win
        if game[0] == [i, i, i] or game[1] == [i, i, i] or game[2] == [i, i, i]:
            return winners[i]
        # vertical first column
        elif game[0][0] == i and game[1][0] == i and game[2][0] == i:
            return winners[i]
        # vertical second column
        elif game[0][1] == i and game[1][1] == i and game[2][1] == i:
            return winners[i]
        # vertical third column
        elif game[0][2] == i and game[1][2] == i and game[2][2] == i:
            return winners[i]
        # diagonal top-bottom
        elif game[0][0] == i and game[1][1] == i and game[2][2] == i:
            return winners[i]
        # diagonal bottom-top
        elif game[0][2] == i and game[1][1] == i and game[2][0] == i:
            return winners[i]
    else:
        return winners[0]


winner_is_1 = [[1, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_2 = [[2, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_1V2 = [[0, 1, 0],
                 [2, 1, 0],
                 [2, 1, 1]]

winner_is_2V2 = [[0, 2, 0],
                 [1, 2, 0],
                 [1, 2, 2]]

no_winner = [[1, 2, 0],
             [2, 1, 0],
             [2, 1, 2]]
no_winnerV1 = [[1, 2, 0],
               [2, 1, 0],
               [2, 1, 0]]

winner = check_winner(winner_is_2V2)
print("The winner is:", winner)
