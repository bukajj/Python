import unittest
import BlackJackGame

class BlackJackTest(unittest.TestCase):
    def count_test(self):
        test=BlackJackGame('test',1,1)
        test.set_player_cards(2,6)
        self.assertTrue(test.count()==10)
        test.set_player_cards(2, 15)
        self.assertTrue(test.count()==0)
        test.set_player_cards(22, 5)
        self.assertTrue(test.count() == 0)


    def hit_test(self):
        test = BlackJackGame('test', 1, 1)
        test.set_player_cards(2, 6)
        ass

if __name__ == '__main__':
        unittest.main()