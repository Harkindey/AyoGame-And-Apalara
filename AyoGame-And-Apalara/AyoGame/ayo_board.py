#!/usr/bin/python
#-*- coding: iso-8859-1



"""
Ayo Game. Imports 'ayo_player' class which may be HUMAN or COMPUTER.
If it is COMPUTER, the AI is used.
God bless ya!!!

"""

import Tkinter
import ayo_player
#from ayo_computer import game_play
import time
from random import random

hole_mat = []
#global board_mat
#board_mat = [[(1,1),(1,2),(1,3),(1,4),(1,5),(1,6)],
#             [(2,1),(2,2),(2,3),(2,4),(2,5),(2,6)]]#tuples

DEFAULT_BOARD = [[4,4,4,4,4,4],
             [4,4,4,4,4,4]]
board_mat = list(DEFAULT_BOARD)
#constant sizes
WIN_WIDTH = 900
WIN_HEIGHT = 300
#variable sizes
B_WIDTH = WIN_WIDTH * 2 / 3
B_HEIGHT = B_WIDTH / 3
X_ALLOWANCE = B_WIDTH * 1 / 60
Y_ALLOWANCE = B_HEIGHT * 1 / 20
WIN_SIZE = str(WIN_WIDTH)+"x"+str(WIN_HEIGHT)
SIZE_X = B_WIDTH/(len(board_mat[0]))
SIZE_Y = B_HEIGHT/(len(board_mat))

#popup class

class popup(Tkinter.Frame):
    
    def say_hi(self):
        print ("hi there, everyone!")

    def createWidgets(self):
        self.messageVar = Tkinter.StringVar()
        self.messageVar.set(self.message)
        Tkinter.Label(self, text=self.message, foreground="red").grid(column=0,row=0,sticky=(Tkinter.N,Tkinter.W, Tkinter.S, Tkinter.E))
        #self.hi_there["command"] = self.say_hi

        #self.hi_there.pack({"side": "left"})

    def __init__(self, master=None, message="Hello"):
        Tkinter.Frame.__init__(self, master)
        self.message = message
        self.pack()
        self.createWidgets()

def createpopup(message="Hello"):
    tk = Tkinter.Tk()
    cpopup = popup(master=tk, message=message)
    tk.mainloop()

class ayo_board(Tkinter.Frame):

    GAME_ON = 1
    GAME_OVER = 0
    MAX_CAPTURELESS = 30
    
    def __init__(self, parent):
        Tkinter.Frame.__init__(self,parent)
        self.parent = parent
        self.initialise()
        self.turn = 2
        self.p1 = ayo_player.ayo_player(1,ayo_player.ayo_player.COMPUTER,level=2)
        self.p2 = ayo_player.ayo_player(2,ayo_player.ayo_player.HUMAN,level=2)
        self.next_player = self.p2
        self.draw_scores((0,0))
        self.game_state = self.GAME_ON
        self.captureless_count = 0
        self.board_mat = [1,2]
        self.board_mat[0]= list(DEFAULT_BOARD[0])
        self.board_mat[1]= list(DEFAULT_BOARD[1])
        self.matrix_copy = list(self.board_mat)

    def initialise(self, board_mat=board_mat):
        self.create_menu()

        self.parent.title("Ayo Board")
        self.pack(fill=Tkinter.BOTH, expand=1)
        self.board_mat = [1,2]
        self.board_mat[0]= list(DEFAULT_BOARD[0])
        self.board_mat[1]= list(DEFAULT_BOARD[1])
        print (self.board_mat)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.scoreboard = Tkinter.Canvas(self, relief=Tkinter.SUNKEN, bg="white", width=SIZE_X+(1+1)*X_ALLOWANCE, height=B_HEIGHT+(2+1)*Y_ALLOWANCE) #Add allowance to the ends
        self.canvas = Tkinter.Canvas(self, relief=Tkinter.SUNKEN, bg="brown", width=B_WIDTH+X_ALLOWANCE, height=B_HEIGHT+Y_ALLOWANCE) #Add allowance to the ends
        self.canvas.grid(column=0,row=0)#, sticky=(Tkinter.N, Tkinter.W))
        self.scoreboard.grid(column=1,row=0)
        #self.score_canvas = Tkinter.Canvas(self, relief=Tkinter.SUNKEN, bg="brown", width=SIZE_X, height=B_WIDTH+Y_ALLOWANCE)
        #self.score_canvas.pack(side=Tkinter.BOTTOM, expand=True, fill=Tkinter.BOTH, padx=(WIN_WIDTH+2*B_WIDTH-X_ALLOWANCE)/2, pady=int((WIN_HEIGHT-B_HEIGHT-Y_ALLOWANCE)/2))
        #self.canvas.pack(side=Tkinter.BOTTOM, expand=True, fill=Tkinter.BOTH, padx=int((WIN_WIDTH-B_WIDTH-X_ALLOWANCE)/2), pady=int((WIN_HEIGHT-B_HEIGHT-Y_ALLOWANCE)/2))
        print ('canvas created')
        # draw holes
        self.hole = [['','','','','',''],['','','','','','']]
        self.text_id = [['','','','','',''],['','','','','','']]
        print (DEFAULT_BOARD)
        for j, line in enumerate(self.board_mat, 1): # j is player id (1,2)
            for i, value in enumerate(line, 1): # i is hole position (1,2,3,4,5,6)
                x1 = (i-1)*SIZE_X + X_ALLOWANCE
                y1 = (j-1)*SIZE_Y + Y_ALLOWANCE
                x2 = (i)*SIZE_X
                y2 = (j)*SIZE_Y
                self.canvas.create_oval(x1, y1, x2, y2, fill="black")
                self.hole[j-1][i-1] = (x1, y1, x2, y2)
                c_x, c_y = self.center_pos(x1,y1,x2,y2) # get center of circles, which are approximately the text positions and will eventually become the centres of the images containing seeds

                self.text_id[j-1][i-1] = self.canvas.create_text(c_x, c_y, anchor=Tkinter.CENTER, font="Purisa", text=str(value), fill="white")
                #print self.text_id[j-1][i-1]
        self.canvas.bind("<ButtonPress-1>", self.clicked)

        #draw scoreboard
        self.scoretext_id = [0,0]
        hole_1_pos = ((X_ALLOWANCE,Y_ALLOWANCE), (SIZE_X+X_ALLOWANCE, SIZE_Y+X_ALLOWANCE))
        hole_2_pos = ((X_ALLOWANCE,SIZE_Y+2*Y_ALLOWANCE), (SIZE_X+X_ALLOWANCE, 2*SIZE_Y+2*Y_ALLOWANCE))
        self.scoreboard.create_oval(hole_1_pos[0][0],hole_1_pos[0][1], hole_1_pos[1][0], hole_1_pos[1][1], fill="black")
        self.scoreboard.create_oval(hole_2_pos[0][0],hole_2_pos[0][1],hole_2_pos[1][0],hole_2_pos[1][1], fill="black")
        self.scoretext_id[1-1] = self.scoreboard.create_text((hole_1_pos[0][0]+hole_1_pos[1][0])/2,(hole_1_pos[0][1]+hole_1_pos[1][1])/2, font="Purisa", fill="white")
        self.scoretext_id[2-1] = self.scoreboard.create_text((hole_2_pos[0][0]+hole_2_pos[1][0])/2,(hole_2_pos[0][1]+hole_2_pos[1][1])/2, font="Purisa", fill="white")
        self.countdown_text_id = self.scoreboard.create_text(X_ALLOWANCE+SIZE_X/2,SIZE_Y+1.5*Y_ALLOWANCE, fill="black")

        #self.game_play = game_play()

    def create_menu(self):
        self.menubar = Tkinter.Menu(self.parent)
        self.parent.config(menu=self.menubar)

        self.fileMenu = Tkinter.Menu(self.menubar)
        self.fileMenu.add_command(label="Exit", command=self.on_exit)

        self.gameMenu = Tkinter.Menu(self.menubar)
        self.gameMenu.add_command(label="Restart", command=self.restart)
        self.gameMenu.add_command(label="Switch P1 mode", command=self.switchmode1)
        self.gameMenu.add_command(label="Switch P2 mode", command=self.switchmode2)
        
        self.menubar.add_cascade(label="File", menu=self.fileMenu)
        self.menubar.add_cascade(label="Game", menu=self.gameMenu)

    def draw_text(self, board_mat):
        for j, line in enumerate(board_mat, 1):
            for i, value in enumerate(line, 1):
                self.canvas.itemconfigure(self.text_id[j-1][i-1], text=str(value))

                '''
                x1 = (i-1)*SIZE_X + X_ALLOWANCE
                y1 = (j-1)*SIZE_Y + Y_ALLOWANCE
                x2 = (i)*SIZE_X
                y2 = (j)*SIZE_Y
                c_x, c_y = self.center_pos(x1,y1,x2,y2) # get center of circles, which are approximately the text positions and will eventually become the centres of the images containing seeds
                print self.text_id[j-1][i-1]
                print value
                '''

    def draw_scores(self, score_tuple):
        for i in range(2):
            self.scoreboard.itemconfigure(self.scoretext_id[i-1], text=str(score_tuple[i-1]))
        self.update_idletasks()

 
    def center_pos(self, x1,y1,x2,y2):
        x = (x1 + x2) / 2
        y = (y1 + y2) / 2
        return x, y

    def clicked(self, event):
        coords_j_i = self.get_hole_from_coords(event.x, event.y)
        if not(coords_j_i == None):
            hole_j, hole_i = coords_j_i
            self.clicked_hole(hole_j, hole_i)
            #print hole_j, hole_i
        

    def get_hole_from_coords(self, x, y):
        #hole1_center = self.hole[1-1][1-1][0]+SIZE_X/2, self.hole[1-1][1-1][1]+SIZE_Y/2 # first hole in array
        the_hole = None
        for j, line in enumerate(self.hole, 1):
            for i, hole in enumerate(line, 1):
                if self.in_circle(x,y, hole[0],hole[1],hole[2],hole[3]):
                    the_hole = j,i
                    break
            if not(the_hole == None):
                break
        return the_hole

    def in_circle(self, x,y, x1,y1, x2,y2): # where (x,y) are point coords, (x1,y1),(x2,y2) are coords of bounding box of circle
        xc = (x1 + x2) / 2 # x-coord of center
        yc = (y1 + y2) / 2 # y-coord of center
        r2 = (xc - x1)**2 # square of radius -> r^2
        l2 = (x - xc)**2 + (y - yc)**2 # distance of point from center
        if (l2 < r2):
            return True
        else:
            return False

    def get_clicked_coords(self, event):
        x, y = event.x, event.y
        #self.item = self.canvas.create_oval(event.x, event.y, event.x+5/2, event.y+5/2, fill='red')

    def clicked_hole(self, hole_j, hole_i):
        
        # game play called from here
        if self.turn == 1:
            self.next_player = self.p1                    
        else:
            self.next_player = self.p2

        if self.next_player.player_type == self.next_player.HUMAN:
            hole_id = (hole_j, hole_i)
            captured, self.board_mat = self.next_move(self.next_player.id, (hole_id))

 
        return

    def refresh_board(self, board_mat):
        self.draw_text(board_mat)
        self.update_idletasks()

    def on_exit(self):
        self.parent.destroy()

    def restart(self):
        DEFAULT_BOARD = [[4,4,4,4,4,4],
                    [4,4,4,4,4,4]]
        self.parent.destroy()
        main()

    # ACTUAL GAMEPLAY

    def next_move(self, player=2, hole_id=(2,1), board_mat=board_mat):
        self.scoreboard.itemconfigure(self.countdown_text_id, text=str(self.MAX_CAPTURELESS-self.captureless_count))
        self.draw_scores((self.p1.score,self.p2.score))
        # returns captured seeds, final_board_mat
        if self.game_state == self.GAME_OVER:
            reason = "Game over naa ni"
            winner = "No winner yet o."
            if self.p1.score > self.p2.score:
                reason = winner = "Player 1 wins!"
            if self.p2.score > self.p1.score:
                reason = winner = "Player 2 wins!"
            if self.p2.score == self.p1.score:
                reason = winner = "It's a draw!!"
            if self.captureless_count >= self.MAX_CAPTURELESS:
                reason = "Infinite play imminent"
            if self.no_seeds_left(int(self.p1.id)):
                reason = "Player 1 has no seeds left!"
            if self.no_seeds_left(int(self.p2.id)):
                reason = "Player 2 has no seeds left!"
            createpopup(message="Game over, baby!!!\n"+reason+"\n"+winner)
            return 0, self.board_mat
        #self.board_mat = board_mat
        player = self.turn
        current_hole = hole_id
        captured = 0
        if not(player == hole_id[0]):
            return "You can only play seeds on your side of the board", self.board_mat
        hole = hole_id[1]
        seeds = self.board_mat[player-1][hole-1]
        self.board_mat[current_hole[0]-1][current_hole[1]-1] = 0
        #print "seeds = ", seeds
        if not (seeds == 0):
            self.captureless_count += 1
            while seeds >= 1:
                current_hole = self.next_hole(current_hole[0], current_hole[1])
                self.board_mat[current_hole[0]-1][current_hole[1]-1] += 1
                time.sleep(0.5)
                self.refresh_board(self.board_mat)
                seeds -= 1
            #print board_mat[current_hole[0]-1][current_hole[1]-1]
            # capture
            if True:
                while (self.board_mat[current_hole[0]-1][current_hole[1]-1] <= 3 and
                current_hole[0]==self.other_player(player) and
                self.board_mat[current_hole[0]-1][current_hole[1]-1]>1):
                    if True:
                        self.captureless_count = 0
                        captured += self.board_mat[current_hole[0]-1][current_hole[1]-1]
                        print ("captured = ", captured)
                        self.board_mat[current_hole[0]-1][current_hole[1]-1] = 0
                        time.sleep(0.5)
                        self.refresh_board(self.board_mat)
                    else:
                        break
                    current_hole = self.prev_hole(current_hole[0],current_hole[1])

            if self.turn == 1:
                self.p1.score += captured
                self.turn = 2
            else:
                self.p2.score += captured
                self.turn = 1

            if self.turn == 1:
                self.next_player = self.p1
            else:
                self.next_player = self.p2

            if self.next_player.player_type == self.next_player.COMPUTER:
                time.sleep(0.5)
                #hole_no = int(random()*6)+1
                matrix_copy = list(self.board_mat[:])
                board_matter = [1,2]
                board_matter[0] = list(matrix_copy[0])[:]
                board_matter[1] = list(matrix_copy[1])[:]
                hole_no = self.next_player.get_next_move(matrix_copy)
                print (hole_no)
                self.board_mat[0] = list(board_matter[0])
                self.board_mat[1] = list(board_matter[1])
                captured, self.board_mat = self.next_move(self.next_player.id, (self.next_player.id, hole_no), list(self.board_mat))
                print (self.board_mat)
                print ("board matter")
                print (board_matter)
                #done = False
                #while not done:
                #    captured, board_mat = self.next_move(self.next_player.id, (self.next_player.id, hole_no))
                #    if board_mat[self.next_player.id-1][hole_no-1] != 0:
                #        done = True

            if self.captureless_count >= self.MAX_CAPTURELESS or self.no_seeds_left(self.turn) or self.p1.score > 24 or self.p2.score > 24:
                self.game_state = self.GAME_OVER

            print ("player 1 has %d seeds" % self.p1.score)
            print ("player 2 has %d seeds" % self.p2.score)
        return captured, self.board_mat

    def no_seeds_left(self, player):
        for i in self.board_mat[player-1]:
            if i != 0:
                return False
        return True
            
        
    def other_player(self, player):
        # gets other player
        if player==1:
            return 2
        else:
            return 1
        

    def prev_hole(self, player, hole):
        # gets previous hole used.
        if player==1:
            if hole < 6:
                return player, hole+1
            else:
                return 2, 6
        elif player==2:
            if hole > 1:
                return player, hole-1
            else:
                return 1, 1

    def next_hole(self, player, hole):
        # gets next hole to be used.
        if player==1:
            if hole > 1:
                return player, hole-1
            else:
                return 2, 1
        elif player==2:
            if hole < 6:
                return player, hole+1
            else:
                return 1, 6

    def switchmode1(self):
        self.p1.player_type = (self.p1.player_type + 1) % 2

    def switchmode2(self):
        self.p2.player_type = (self.p2.player_type + 1) % 2



def main():
    root = Tkinter.Tk()
    board = ayo_board(root)
    root.geometry(WIN_SIZE)
    root.mainloop()


if __name__ == '__main__':
    main()
