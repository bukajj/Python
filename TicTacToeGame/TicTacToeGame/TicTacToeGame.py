def play():
    field=[['+',0,1,2],[0,' ',' ',' '],[1,' ',' ',' '],[2,' ',' ',' ']]
    
    def tab_print():
        for tup in field:
            print(str(tup[0]) + ' ' + str(tup[1]) + ' ' + str(tup[2]) + ' ' + str(tup[3]))
    
    def set(value, position):
        if 0<=int(position[0])<=2 and 0<=int(position[1])<=2 and (value=='x' or value=='o'):
            if field[position[0]+1][position[1]+1]==' ':
                field[position[0]+1][position[1]+1]=value
                return True
            else:
                return False
        else:
            return False


    def win():
        if field[1][1]==field[1][2]==field[1][3] and field[1][1]!=' ':
            return True
        elif field[1][1]==field[2][1]==field[3][1] and field[1][1]!=' ':
            return True
        elif field[1][1]==field[2][2]==field[3][3] and field[1][1]!=' ':
            return True
        elif field[1][3]==field[2][2]==field[3][1] and field[1][3]!=' ':
            return True
        elif field[1][2]==field[2][2]==field[3][2] and field[1][2]!=' ':
            return True
        elif field[1][3]==field[2][3]==field[3][3] and field[1][3]!=' ':
            return True
        elif field[2][1]==field[2][2]==field[2][3] and field[2][1]!=' ':
            return True
        elif field[3][1]==field[3][2]==field[3][3] and field[3][1]!=' ':
            return True
        else:
            return False

    print('Player 1: ')
    player1=input()
    print('Player 2: ')
    player2=input()
    key=False
    player=player2
    winner=player
    while key==False:
       if player==player1:
           player=player2
       else:
           player=player1
       tab_print()
       position=[] 
       key1=False
       while key1==False:
           print(player + ': 1st coordinate')
           answer=int(input())
           position.append(answer)
           print(player + ': 2nd coordinate')
           answer=int(input())
           position.append(answer)
           if(player==player1):
               key1=set('x',position)
               position.clear()
           else:
               key1=set('o',position)
               position.clear()
       if win()==True:
           winner=player
           key=True
           print('The winner is: ' + winner)

play()



            