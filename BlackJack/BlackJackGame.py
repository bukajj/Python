import random


class BlackJackGame:

    def __init__(self, name='test', bet=1, deck_amount=1):
        self.__name=name
        self.__bet=bet
        self.__cards=[['2',1,2],['3',1,3],['4',1,4],['5',1,5],['6',1,6],['7',1,7],['8',1,8],['9',1,9],['10',1,10],['Jack',1,10],['Queen',1,10],['King',1,10],['A',1,11]]
        for card in self.__cards:
            card[1]=4*deck_amount
        self.__player_cards=[]
        self.__player_hand=[]
        self.__computer_cards=[]
        self.__player_weight=[]
        self.__computer_weight = 0

    def hit(self,type):
        if type=='p':
            if self.__player_hand==self.__player_cards[0]:
                card=int(random.random()*12)
                while(self.__cards[card][1]==0):
                    card=int(random.random()*12)
                self.__player_hand.append(card)
                self.__player_cards[0].append(card)
                self.__cards[card][1] -= 1

            else:
                card=int(random.random()*12)
                while (self.__cards[card][1] == 0):
                    card=int(random.random()*12)
                self.__player_hand.append(card)
                self.__player_cards[1].append(card)
                self.__cards[card][1] -= 1
        else:
            card=int(random.random()*12)
            while (self.__cards[card][1] == 0):
                card=int(random.random()*12)
            self.__computer_cards.append(card)
            self.__cards[card][1] -= 1

    def stand(self):
        if self.is_busted()[0]==True:
            return False
        else:
            while self.count('c')<17:
                self.hit('c')
            return self.check()

    def double_down(self):
        self.hit('p')
        self.__bet*=2
        if self.is_busted()[0]==True:
            return False
        else:
            return self.check()

    def insurance(self):
        if self.__computer_cards[0]!=12:
            return (False,False)
        if self.__cards[self.__computer_cards[1]][2]==10:
            return (True,True)
        else:
            return (True,False)

    def split(self):
        if self.__player_cards==[]:
            return False
        if self.__player_hand[0]==self.__player_hand[1]:
            self.__player_cards=[[self.__player_hand[0]], [self.__player_hand[1]]]
            self.__player_hand=self.__player_cards[0]
            return True
        else:
            return False

    def show(self):
        print(self.__name + ': ' + str(self.__player_cards))
        print('Computer: ' + str(self.__computer_cards[0]))

    def showAll(self):
        print(self.__name + ': ' + str(self.__player_cards))
        print('Computer: ' + str(self.__computer_cards))

    def get_first_cards(self):
        self.__player_cards=[[]]
        self.hit('p')
        self.hit('p')
        self.hit('c')
        self.hit('c')

    def is_busted(self):
        player=False
        computer=False
        if self.count('p')>21:
            player=True
        if self.count('c')>21:
            computer=True
        return (player,computer)

    def check(self):
        key=self.is_busted()[1]
        if key==True:
            return True
        else:
            if self.count('p')>self.count('c'):
                return True
            else:
                return False

    def count(self, type):
            count=0
            if type=='p':
                a=[]
                for card in self.__player_hand:
                    if card!=12:
                        count += self.__cards[card][2]
                    else:
                        a.append(True)
                        count+=11
                for aa in a:
                    if aa == True:
                        if count > 21:
                            count -= 10
            else:
                a = []
                for card in self.__computer_cards:
                    if card != 12:
                        count += self.__cards[card][2]
                    else:
                        a.append(True)
                        count += 11
                for aa in a:
                    if aa == True:
                        if count > 21:
                            count -= 10
            return count


    def set_player_cards(self,*args):
        self.__player_cards.clear()
        self.__player_hand.clear()
        self.__player_cards=[[]]
        for card in args:
            if card>12 or card<0:
                self.__player_cards.clear()
                self.__player_hand.clear()
                break
            else:
                self.__player_hand.append(card)
                self.__player_cards[0].append(card)
                self.__cards[card][1]-=1


    def set_computer_cards(self,*args):
        self.__computer_cards.clear()
        for card in args:
            if card>12 or card<0:
                self.__computer_cards.clear()
                break
            else:
                self.__computer_cards.append(card)
                self.__cards[card][1] -= 1

    def get_player(self):
        return self.__player_cards

    def get_computer(self):
        return  self.__computer_cards




