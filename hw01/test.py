""""
This module tests TicTacGame class from tictactoe.py
"""
from tictactoe import TicTacGame


class TicTacGameForTesting(TicTacGame):
    """"
    Getter and setter for TicTacGame._field for correct testing
    """
    def set_field(self, field) -> []:
        """"setter for _field"""
        self._field = field

    def get_field(self) -> []:
        """"getter for field"""
        return self._field


def test_data_validation() -> None:
    """Test data_validation method"""
    game = TicTacGame()
    assert game.validate_input('lol') == -1
    assert game.validate_input('10') == -1
    assert game.validate_input('-1') == -1
    assert game.validate_input('5') == 5


def test_put() -> None:
    """Test put method"""
    game = TicTacGameForTesting()
    game.put(0)
    assert game.get_field() == ['×', '-', '-', '-', '-', '-', '-', '-', '-']
    game.put(1)
    assert game.get_field() == ['×', 'O', '-', '-', '-', '-', '-', '-', '-']
    game.put(0)
    assert game.get_field() == ['×', 'O', '-', '-', '-', '-', '-', '-', '-']


def test_check_winner() -> None:
    """Test check_winner method"""
    game = TicTacGameForTesting()
    game.set_field(['×', '×', '×', '-', '-', '-', '-', '-', '-'])
    assert game.check_winner() == 'Player-1 is the winner!'
    game.set_field(['×', '×', '-', 'O', 'O', 'O', '-', '-', '-'])
    assert game.check_winner() == 'Player-2 is the winner!'
    game.set_field(['×', '×', '-', '-', '-', '-', 'O', 'O', 'O'])
    assert game.check_winner() == 'Player-2 is the winner!'
    game.set_field(['×', '-', '-', '×', '-', '-', '×', 'O', 'O'])
    assert game.check_winner() == 'Player-1 is the winner!'
    game.set_field(['-', 'O', '-', '-', 'O', '-', '×', 'O', '-'])
    assert game.check_winner() == 'Player-2 is the winner!'
    game.set_field(['-', '-', 'O', '-', '-', 'O', '×', '×', 'O'])
    assert game.check_winner() == 'Player-2 is the winner!'
    game.set_field(['×', 'O', '×', '×', '×', 'O', 'O', '×', 'O'])
    assert game.check_winner() == 'Draw'
    game.set_field(['-', '-', '-', '-', '-', '-', '-', '-', '-'])
    assert game.check_winner() == 'in progress'


if __name__ == '__main__':
    print('==========================================')
    print('Starting the testing')
    print('==========================================')
    test_data_validation()
    test_put()
    test_check_winner()
    print('==========================================')
    print('All tests passed')
    print('==========================================')
