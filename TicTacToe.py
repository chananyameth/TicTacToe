import os

class TicTacToe:    
    def __init__(self):
        os.system("cls" if os.name=="nt" else "clear")
        self.moves = [' '] * 9

    def do_move(self, x_o, i):
        inp = input("Enter a number of cell for " + str(x_o) + "'s move: ")
        try:
            int(inp)    #checks if inp isn't a number
            if 9<int(inp) or int(inp)<1:     #checks if inp isn't in the correct range(1-9)
                raise ValueError
        except ValueError:
            print('Error! Enter a number betwin 1 and 9:')
            self.do_move(x_o, i)
            return
            
        if self.moves[int(inp)-1] != ' ':
            print('Error! This place is already taken. Try again:')
            self.do_move(x_o, i)
        else:
            self.moves[int(inp)-1] = x_o

    def check_for_winner(self):#TODO:
        if self.moves[0]==self.moves[1] and self.moves[1]==self.moves[2] and self.moves[0]!=' ': return self.moves[0]
        if self.moves[3]==self.moves[4] and self.moves[4]==self.moves[5] and self.moves[3]!=' ': return self.moves[3]
        if self.moves[6]==self.moves[7] and self.moves[7]==self.moves[8] and self.moves[6]!=' ': return self.moves[6]
        if self.moves[0]==self.moves[3] and self.moves[3]==self.moves[6] and self.moves[0]!=' ': return self.moves[0]
        if self.moves[1]==self.moves[4] and self.moves[4]==self.moves[7] and self.moves[1]!=' ': return self.moves[1]
        if self.moves[2]==self.moves[5] and self.moves[5]==self.moves[8] and self.moves[2]!=' ': return self.moves[2]
        if self.moves[0]==self.moves[4] and self.moves[4]==self.moves[8] and self.moves[0]!=' ': return self.moves[0]
        if self.moves[6]==self.moves[4] and self.moves[4]==self.moves[2] and self.moves[6]!=' ': return self.moves[6]
        return ' '

    def game(self):
        for i in range(9):
            os.system("cls" if os.name=="nt" else "clear")
            self.show_board()
            
            if i%2 == 0:
                self.do_move('X', i)
            else:
                self.do_move('O', i)
                
            result = self.check_for_winner()
            if result != ' ':
                return "The winner is " + result + "!"
                
        #if no one won yet
        return "There is no winner..."

    def show_board(self):
        print('''
      ║     ║    
   {6}  ║  {7}  ║  {8}
      ║     ║    
 ═════╬═════╬═════
      ║     ║    
   {3}  ║  {4}  ║  {5} 
      ║     ║    
 ═════╬═════╬═════
      ║     ║    
   {0}  ║  {1}  ║  {2} 
      ║     ║    
'''.format(*self.moves))
        print('''
 7 | 8 | 9
 - + - + -
 4 | 5 | 6
 - + - + -
 1 | 2 | 3
''')

        
def main():
    while True:
        TicTacToe().game()
        q = input('Do you want another game? (y/n)  ')
        if q!="y":
            print("Goodbye!")
            return

        

if __name__ == "__main__":
    main()
