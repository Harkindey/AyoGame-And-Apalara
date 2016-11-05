


import random

DEFAULT_BOARD = [[4,4,4,4,4,4],
                 [4,4,4,4,4,4]]

# gameplay rules and actions
class gameplay:
    
    def __init__(self,player):
        self.player = player
        return
    
    def do_play(self,player,hole_id=(1,1), board_mat=DEFAULT_BOARD[:]):
        # returns captured seeds, final_board_mat
        #player = self.player
        
        board_mat = list(board_mat)
        current_hole = hole_id
        captured = 0
        if not(player == hole_id[0]):
            return "You can only play seeds on your side of the board", board_mat
        hole = hole_id[1]
        seeds = board_mat[player-1][hole-1]
        board_mat[current_hole[0]-1][current_hole[1]-1] = 0
        print ("seeds = ", seeds)
        if not (seeds == 0):
            print (current_hole)
            while seeds >= 1:
                current_hole = self.next_hole(current_hole[0], current_hole[1])
                board_mat[current_hole[0]-1][current_hole[1]-1] += 1
                seeds -= 1
            print (board_mat[current_hole[0]-1][current_hole[1]-1])
            if board_mat[current_hole[0]-1][current_hole[1]-1] <= 3 and current_hole[0]==self.other_player(player) and board_mat[current_hole[0]-1][current_hole[1]-1] > 1:
                while current_hole[0] == self.other_player(player):
                    if board_mat[current_hole[0]-1][current_hole[1]-1] <= 3 and board_mat[current_hole[0]-1][current_hole[1]-1] > 1:
                        captured += board_mat[current_hole[0]-1][current_hole[1]-1]
                        print ("captured = ", captured)
                        board_mat[current_hole[0]-1][current_hole[1]-1] = 0
                    else:
                        break
                    current_hole = self.prev_hole(current_hole[0],current_hole[1])
        return captured, board_mat

        
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

# game tree classes
class game_tree:
    def __init__(self):
        self.nodes = []
        return

    def add_node(self, node):
        self.nodes.append(node)
        return

class game_node:
    def __init__(self,player,hole,captured):
        self.player = player
        self.hole = hole
        self.captured = captured
        self.nodes = []
        return

    def add_node(self, node):
        self.nodes.append(node)
        return

    def print_tree(self, level=0):
        self.print_game_tree(self, level)
        return

    def print_game_tree(self, game_tree, level=0):
        print (level)
        message = level*"-" + "+player = %d\n" % game_tree.player
        message += level*"-" + "|hole played = %d\n" % game_tree.hole
        message += level*"-" + "|seeds captured = %d\n" % game_tree.captured
        print (message)
        if len(game_tree.nodes) != 0:
            level += 1
           
            for node in game_tree.nodes:
                self.print_game_tree(node, level)
        
        
        return game_tree

# ayo player class: the actual player
class ayo_player:
    HUMAN = 0
    COMPUTER = 1
    score = 0
    DEFAULT_BOARD = [[4,4,4,4,4,4],
                     [4,4,4,4,4,4]]
    game_tree = ""
    
    def __init__(self,player_id,player_type=HUMAN, level=1):
        self.id = (player_id % 2) + ((player_id + 1) % 2) * 2 #1 for odd numbers, 2 for even numbers
        self.player_type = player_type
        self.level = level
        self.gameplay = gameplay(self)
        self.score = 0
        self.board_mat = list(DEFAULT_BOARD)

    def __str__(self):
        return self.id

    def get_next_move(self, board_matr):
        #self.game_tree = game_node()
        board_matx = list(board_matr[:])
        game_tree = game_node(0,0,0)
        print ("id = %d" % self.id)
        #self.game_tree = self.create_game_tree(list(board_matx[:]),0,self.level,self.id,game_tree)
        #self.game_tree = self.create_game_trees(list(board_matx), self.level, self.gameplay.other_player(self.id))
        self.game_tree = self.create_2game_tree(list(board_matx), self.id)
        best_path, diff = self.get_best_path(self.game_tree)
        print (best_path)
        return best_path[0]

    def print_game_tree(self, game_tree, level=0):
        while level<=self.level+1:
            print ("level = %d"% level)
            message = level*"\t-" + "+player = %d\n" % game_tree.player
            message += level*"\t-" + "|hole played = %d\n" % game_tree.hole
            message += level*"\t-" + "|seeds captured = %d\n" % game_tree.captured
            print (message)
            level += 1
            if not (len(game_tree.nodes) == 0):
                for node in game_tree.nodes:
                    self.print_game_tree(node,level)

        return

    def create_game_tree(self,board_matrix,this_level,level,player,base_node):
        board_mat = [1,2]
        board_mat[0] = list(board_matrix[0])
        board_mat[1] = list(board_matrix[1])
        parent_node = base_node
        if this_level == level:
            for i in range(1, len(board_mat[player-1])+1):
                board_mat = list(board_mat[:])
                hole = board_mat[player-1][i-1]
                if hole == 0:
                    continue
                captured, new_board = self.gameplay.do_play(player, (player,i), list(board_mat))
                print (new_board)
                node = game_node(player, i, captured)
                parent_node.add_node(node)
            return parent_node
        else:
            for i in range(1, len(board_mat[player-1])+1):
                hole_seeds = board_mat[player-1][i-1]
                if hole_seeds == 0:
                    continue
                board_copy = list(board_mat)
                captured, boardx = self.gameplay.do_play(player, (player,i), list(board_copy))
                new_board = list(boardx)
                print (new_board)
                node = game_node(player, i, captured)
                node2 = self.create_game_tree(list(new_board),this_level+1,level,self.gameplay.other_player(player),node)
                parent_node.add_node(node)
            return parent_node
                
    def create_2game_tree(self,board_matrix,player_id):
        this_board_mat = [1,2]
        this_board_mat[0] = list(board_matrix[0])
        this_board_mat[1] = list(board_matrix[1])
        other_player_id = self.gameplay.other_player(player_id)
        parent_node = game_node(0,0,0)
        for i in range(1, len(board_matrix[player_id-1])+1):
            if this_board_mat[0][i-1] == 0:
                continue
            captured, new_board = self.gameplay.do_play(player_id, (player_id,i), list(this_board_mat))
            node1 = game_node(player_id,i,captured)

            for j in range(1, len(new_board[other_player_id-1])+1):
                this_board_mat2 = [1,2]
                this_board_mat2[0] = list(new_board[0])
                this_board_mat2[1] = list(new_board[1])
                if this_board_mat2[1][j-1] == 0:
                    continue
                captured, new_board2 = self.gameplay.do_play(other_player_id, (other_player_id,j),this_board_mat2)
                node2 = game_node(other_player_id, j, captured)
                node1.add_node(node2)
                print (this_board_mat)
                print (new_board2)
            
            parent_node.add_node(node1)
        return parent_node

    def best_play2(self,board_matrix,player_id):
        board_mat = [1,2]
        board_mat[0] = list(board_matrix[0])
        board_mat[1] = list(board_matrix[1])
        other_player_id = self.gameplay.other_player(player_id)
        parent_node = game_node(0,0,0)
        diff = 0
        max_diff = 0
        best_play = ["",""]
        for i in range(1, len(board_matrix[player_id-1])+1):
            captured, new_board = self.gameplay.do_play(player_id, (player_id,i), list(board_mat))
            node1 = game_node(player_id,i,captured)
            diff = captured

            for j in range(1, len(new_board[other_player_id-1])+1):
                captured, new_board2 = self.gameplay.do_play(other_player_id, (other_player_id,j),list(new_board))
                node2 = game_node(other_player_id, j, captured)
                node1.add_node(node2)
                diff -= captured
                if diff > max_diff:
                    max_diff = diff
                    best_play = [i,j]
            
            parent_node.add_node(node1)
        return parent_node

    def get_diff(self,node):
        if node.player == self.id:
            diff = node.captured
        else:
            diff = node.captured * (-1)
        return diff

    def get_best_path(self,parent_node):
        diff = 0
        max_diff = 0
        path = list()
        next_path = list()
        best_path = list()
        if len(parent_node.nodes) == 0:
            path.append(parent_node.hole)
            diff = self.get_diff(parent_node)
            return path, diff
        else:
            for node in parent_node.nodes:
                path = list()
                path.append(node.hole)
                next_path, res = self.get_best_path(node)
                diff += res
                path.extend(next_path)
                if diff > max_diff or len(best_path)==0:
                    max_diff = diff
                    best_path = path
                elif (random.randrange(0,4)==1) and diff== max_diff:
                    max_diff = diff
                    best_path = path
        return best_path, max_diff
     

    def create_game_trees(self, board_mat,level,otherplayer):
        player = self.gameplay.other_player(otherplayer)
        level_node = game_node(player,0,0)
        temp_board = list(board_mat)
        temp_board_old = temp_board
        if level == 1:
            # 1 level game play
            for i in range(1,len(self.DEFAULT_BOARD[player-1])):
                if temp_board[player-1][i-1] == 0:
                    continue
                temp_captured, temp_board = self.gameplay.do_play(player,(player,i),temp_board_old)
                print (temp_captured, temp_board)
                node = game_node(player,i,temp_captured)
                level_node.add_node(node)
        else:
            for i in range(1,len(self.DEFAULT_BOARD[player-1])):
                if temp_board[player-1][i] == 0:
                    continue
                node = self.create_game_trees(temp_board, level-1,player)
                level_node.add_node(node)

        return level_node
        
     
        return

def main():
    player1 = ayo_player(1, ayo_player.HUMAN, level=2)
    player1.get_next_move(list(player1.DEFAULT_BOARD))
    #player1.print_game_tree(player1.game_tree, 0)

if __name__ == "__main__":
    main()
