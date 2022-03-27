"""
This module implements tictactoe game for 2 players
Valid input to occupy a cell - integer in range [0, 8]
"""
import copy


class TicTacGame:
    """
    This class implements tictactoe game
    Available methods: show_board,  put, validate_input, start_game, check_winner
    """

    def __init__(self):
        self._size = 9
        self._field = ['-' for _ in range(self._size)]
        self._current_round = 0
        self._victory_poses = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                               (0, 3, 6), (1, 4, 7), (2, 5, 8),
                               (0, 4, 8), (2, 4, 6))

    def show_board(self) -> None:
        """
        This method shows the game board
        - for free cell
        × for Player-1 cell
        O for Player-2 cell
        """
        print(f'It`s {self._current_round} round in the game')
        for i in range(self._size):
            print(f'{self._field[i]:>3}', end='')
            if i % int(self._size ** 0.5) == 2:
                print()

    def put(self, pos) -> None:
        """
        This method puts player`s value to field in pos cell
        """
        if self._current_round % 2 == 0:
            self._field[pos] = '×'
        else:
            self._field[pos] = 'O'
        self._current_round += 1

    def validate_input(self, inp) -> int:
        """
        This method validates player`s input
        It must be an integer in range [0, 8]
        :return
        Position if the input is correct and -1 else
        """
        try:
            pos = int(inp)
        except ValueError:
            print(f'{inp} isn`t available cell. Please, input integer value')
            return -1
        if pos < 0 or pos >= self._size:
            print('Position must be in range [0, 8]')
            return -1
        if self._field[pos] != '-':
            print('This cell is already occupied')
            return -1
        return pos

    def start_game(self) -> None:
        """
        This method runs the game
        """
        current_winner = 'in progress'
        while current_winner == 'in progress':
            self.show_board()
            print(f'Now it is Player-{self._current_round % 2 + 1} turn.')
            pos = -1
            while pos == -1:
                try:
                    pos = self.validate_input(input('Input cell number:'))
                except EOFError:
                    print('The game is over due to no input, please, run the program again')
                    return
            self.put(pos)
            current_winner = self.check_winner()
        self.show_board()
        print(current_winner)

    def check_winner(self) -> str:
        """
        This method checks is there winner
        :return:
        "Draw" if there is a draw in the game
        "Player-i is the winner!" if there is the winner
        "in progress" if the game hasn't finished yet
        """
        for victory_pos in self._victory_poses:
            if self._field[victory_pos[0]] == self._field[victory_pos[1]] and \
                    self._field[victory_pos[1]] == self._field[victory_pos[2]]:
                if self._field[victory_pos[0]] == '×':
                    return 'Player-1 is the winner!'
                if self._field[victory_pos[0]] == 'O':
                    return 'Player-2 is the winner!'
        for cell in self._field:
            if cell == '-':
                return 'in progress'
        return 'Draw'

    def get_field(self):
        """Getter for field"""
        return copy.copy(self._field)


if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()
