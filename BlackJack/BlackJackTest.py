import unittest
import BlackJackGame

class BlackJackTest(unittest.TestCase):
    def count_test(self):
        test=BlackJackGame('test',1,1)
        test.set_player_cards(2,6)
        self.assertTrue(test.count('p')==10)
        test.set_player_cards(2, 15)
        self.assertTrue(test.count('p')==0)
        test.set_player_cards(22, 5)
        self.assertTrue(test.count('p') == 0)
        test.set_player_cards(-22, 5)
        self.assertTrue(test.count('p') == 0)
        test.set_player_cards(12, 12)
        self.assertTrue(test.count('p') == 2)
        test.set_player_cards(12, 11)
        self.assertTrue(test.count('p') == 21)


    def hit_test(self):
        test = BlackJackGame('test', 1, 1)
        test.set_player_cards(2, 6)
        test.hit('p')
        self.assertTrue(test.get_player()[0].count()==3)
        test.hit('p')
        self.assertTrue(test.get_player()[0].count() == 4)
        test.hit('p')
        self.assertTrue(test.get_player()[0].count() == 5)
'''
    def check_test(self):
        test = BlackJackGame('test', 1, 1)
        test.set_player_cards(2, 6)
        test.set_computer_cards(2, 6)
        self.assertTrue(test.check()==False)
        test.set_player_cards(2, 10)
        test.set_computer_cards(2, 6)
        self.assertTrue(test.check() == True)
        test.set_player_cards(2, 6)
        test.set_computer_cards(12, 6)
        self.assertTrue(test.check() == False)

    def stand_test(self):
        test = BlackJackGame('test', 1, 1)
        test.set_player_cards(2, 6)
        test.set_computer_cards(2, 6)
        test.stand()
        self.assertTrue(test.get_computer().count()>2)
        test.set_computer_cards(12, 6)
        test.stand()
        self.assertTrue(test.get_computer().count() == 2)
        test.set_computer_cards(12, 12)
        test.stand()
        self.assertTrue(test.get_computer().count() > 2)
        test.set_computer_cards(11, 11)
        test.stand()
        self.assertTrue(test.get_computer().count() == 2)

    def insurance_test(self):
        test = BlackJackGame('test', 1, 1)
        test.set_player_cards(2, 6)
        test.set_computer_cards(12, 6)
        self.assertTrue(test.insurance()==(True,False))
        test.set_computer_cards(2, 6)
        self.assertTrue(test.insurance() == (False,False))
        test.set_computer_cards(12, 10)
        self.assertTrue(test.insurance() == (True,True))

    def split_test(self):
        test = BlackJackGame('test', 1, 1)
        test.set_player_cards(6, 6)
        self.assertTrue(test.split()==True)
        self.assertTrue(test.get_player().count()==2)
        test = BlackJackGame('test', 1, 1)
        test.set_player_cards(2, 6)
        self.assertTrue(test.split() == False)
        self.assertTrue(test.get_player().count() == 1)
        test.set_player_cards(2, 16)
        self.assertTrue(test.split() == False)
        self.assertTrue(test.get_player().count() == 0)

    def is_busted_test(self):
        test = BlackJackGame('test', 1, 1)
        test.set_player_cards(6, 10,10)
        test.set_computer_cards(12, 6)
        self.assertTrue(test.is_busted()==(True,False))
        test.set_player_cards(6, 6)
        test.set_computer_cards(10,10,5)
        self.assertTrue(test.is_busted() == (False, True))
        test.set_player_cards(6, 6)
        test.set_computer_cards(12, 6)
        self.assertTrue(test.is_busted() == (False, False))
        test.set_player_cards(6, 9,10)
        test.set_computer_cards(11, 6,10)
        self.assertTrue(test.is_busted() == (True,True))'''

if __name__ == '__main__':
        unittest.main()