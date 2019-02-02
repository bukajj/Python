import TicTacToeGame
import unittest

class TicTacToeTest(unittest.TestCase):
    def print_test():
        test_1=TicTacToeGame('John','Mark')
        assert test_1.__field.len()==4
        assert test_1.__field[0].len()==4
        assert test_1.__field[1].len()==4
        assert test_1.__field[2].len()==4
    def set_test():
        test_1=TicTacToeGame('John','Mark')
        test_1.__set('x',(0,0))
        test_1.__set('o',(1,1))
        test_1.__set('dads',(1,2))
        test_1.__set('x',(3,3))
        assert test_1.__field[0][0]=='X'
        assert test_1.__field[0][1]==' '
        assert test_1.__field[0][2]==' '
        assert test_1.__field[1][0]==' '
        assert test_1.__field[1][1]=='O'
        assert test_1.__field[1][2]==' '
        assert test_1.__field[2][0]==' '
        assert test_1.__field[2][1]==' '
        assert test_1.__field[2][2]==' '

if __name__=="__main__":
    unittest.main()



