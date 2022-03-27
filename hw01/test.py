""""
This module tests TicTacGame class from tictactoe.py
"""
from tictactoe import TicTacGame


def test_data_validation() -> None:
    """Test data_validation method"""
    game = TicTacGame()
    # incorrect input
    assert game.validate_input('lol') == -1
    assert game.validate_input('10') == -1
    assert game.validate_input('-1') == -1
    assert game.validate_input('9') == -1
    # correct input
    assert game.validate_input('0') == 0
    assert game.validate_input('1') == 1
    assert game.validate_input('2') == 2
    assert game.validate_input('3') == 3
    assert game.validate_input('4') == 4
    assert game.validate_input('5') == 5
    assert game.validate_input('6') == 6
    assert game.validate_input('7') == 7
    assert game.validate_input('8') == 8
    # occupied cells
    game._field = ['×', 'O', '×', 'O', '×', 'O', '×', 'O', '×']
    assert game.validate_input('0') == -1
    assert game.validate_input('1') == -1
    assert game.validate_input('2') == -1
    assert game.validate_input('3') == -1
    assert game.validate_input('4') == -1
    assert game.validate_input('5') == -1
    assert game.validate_input('6') == -1
    assert game.validate_input('7') == -1
    assert game.validate_input('8') == -1


def test_put() -> None:
    """Test put method"""
    game = TicTacGame()
    game.put(0)
    assert game.get_field() == ['×', '-', '-', '-', '-', '-', '-', '-', '-']
    game.put(1)
    assert game.get_field() == ['×', 'O', '-', '-', '-', '-', '-', '-', '-']
    game.put(2)
    assert game.get_field() == ['×', 'O', '×', '-', '-', '-', '-', '-', '-']
    game.put(3)
    assert game.get_field() == ['×', 'O', '×', 'O', '-', '-', '-', '-', '-']
    game.put(4)
    assert game.get_field() == ['×', 'O', '×', 'O', '×', '-', '-', '-', '-']
    game.put(5)
    assert game.get_field() == ['×', 'O', '×', 'O', '×', 'O', '-', '-', '-']
    game.put(6)
    assert game.get_field() == ['×', 'O', '×', 'O', '×', 'O', '×', '-', '-']
    game.put(7)
    assert game.get_field() == ['×', 'O', '×', 'O', '×', 'O', '×', 'O', '-']
    game.put(8)
    assert game.get_field() == ['×', 'O', '×', 'O', '×', 'O', '×', 'O', '×']


def test_check_winner() -> None:
    """Test check_winner method"""
    game = TicTacGame()
    game._field = ['×', '×', '×',
                   '-', '-', '-',
                   '-', '-', '-']
    assert game.check_winner() == 'Player-1 is the winner!'
    game._field = ['×', '×', '-',
                   'O', 'O', 'O',
                   '-', '-', '-']
    assert game.check_winner() == 'Player-2 is the winner!'
    game._field = ['×', '×', '-',
                   '-', '-', '-',
                   'O', 'O', 'O']
    assert game.check_winner() == 'Player-2 is the winner!'
    game._field = ['×', '-', '-',
                   '×', '-', '-',
                   '×', 'O', 'O']
    assert game.check_winner() == 'Player-1 is the winner!'
    game._field = ['-', 'O', '-',
                   '-', 'O', '-',
                   '×', 'O', '-']
    assert game.check_winner() == 'Player-2 is the winner!'
    game._field = ['-', '-', 'O',
                   '-', '-', 'O',
                   '×', '×', 'O']
    assert game.check_winner() == 'Player-2 is the winner!'
    game._field = ['×', '-', 'O',
                   '-', 'O', '×',
                   'O', '×', '']
    assert game.check_winner() == 'Player-2 is the winner!'
    game._field = ['×', '-', 'O',
                   '-', '×', 'O',
                   'O', '×', '×']
    assert game.check_winner() == 'Player-1 is the winner!'
    game._field = ['×', 'O', '×',
                   '×', '×', 'O',
                   'O', '×', 'O']
    assert game.check_winner() == 'Draw'
    game._field = ['-', '-', '-',
                   '-', '-', '-',
                   '-', '-', '-']
    assert game.check_winner() == 'in progress'


if __name__ == '__main__':
    print('==========================================')
    print('Starting the testing')
    print('==========================================')
    test_put()
    test_data_validation()
    test_check_winner()
    print('==========================================')
    print('All tests passed')
    print('==========================================')
