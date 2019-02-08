class BlackJackGame():
    def __init__(self, name, bet, deck_amount):
        self.__name=name
        self.__bet=bet
        self.__cards=[['2',1,2],['3',1,3],['4',1,4],['5',1,5],['6',1,6],['7',1,7],['8',1,8],['9',1,9],['10',1,10],['Jack',1,10],['Queen',1,10],['King',10],['A',1,11]]
        for card in self.__cards:
            card[1]=4*deck_amount
        self.__player_cards=[]
        self.__player_hand=[]
        self.__computer_cards=[]
        self.__player_weight=[]
        self.__computer_weight = 0

    def hit(self):
        pass

    def stand(self):
        pass

    def double_down(self):
        pass

    def insurance(self):
        pass

    def split(self):
        pass

    def show(self):
        pass

    def get_first_cards(self):
        pass

    def is_busted(self):
        pass

    def check(self):
        pass

    def count(self, type):
        pass

    def set_player_cards(self,*args):
        pass

    def set_computer_cards(self,*args):
        pass

    def get_player(self):
        pass

    def get_computer(self):
        pass

    def get_player_weight(self):
        pass

    def get_computer_weight(self):
        pass


