class TicTacToeGame:
    
    def  __init__(self, player1, player2):
        self.__player1=player1
        self.__player2=player2
        self.__field=[['+',0,1,2],[0,' ',' ',' '],[1,' ',' ',' '],[2,' ',' ',' ']]
    
    def __print():
        for tup in __field:
            print(tup[0] + ' ' + tup[1] + ' ' + tup[2] + ' ' + tup[3])
    
    def __set(value, position):
        if 0<=position[0]<=2 and 0<=position[1]<=2 and (value=='x' or value=='o'):
            if __field[position[0]+1][position[1]+1]==' ':
                __field[position[0]+1][position[1]+1]=value
                return True
            else:
                return False
        else:
            return False


    def __win():
        if __field[1][1]==__field[1][2]==__field[1][3] and __field[1][1]!=' ':
            return True
        elif __field[1][1]==__field[2][1]==__field[3][1] and __field[1][1]!=' ':
            return True
        elif __field[1][1]==__field[2][2]==__field[3][3] and __field[1][1]!=' ':
            return True
        elif __field[1][3]==__field[2][2]==__field[3][1] and __field[1][3]!=' ':
            return True
        elif __field[1][2]==__field[2][2]==__field[3][2] and __field[1][2]!=' ':
            return True
        elif __field[1][3]==__field[2][3]==__field[3][3] and __field[1][3]!=' ':
            return True
        elif __field[2][1]==__field[2][2]==__field[2][3] and __field[2][1]!=' ':
            return True
        elif __field[3][1]==__field[3][2]==__field[3][3] and __field[3][1]!=' ':
            return True
        else:
            return False

    def play():
        key=False
        player=__player2
        winner=player
        while key==False:
           if player==__player1:
               player=__player2
           else:
               player=__player1
           __print()
           print(player + ': Check field (a,b)')
           answer=input()
           key1=False
           while key1==False:
               if(player==__player1):
                   key1=__set('x',answer)
               else:
                   key1=__set('o',answer)
           if __win()==True:
               winner=player
               key=True
        print('The winner is: ' + winner)

            