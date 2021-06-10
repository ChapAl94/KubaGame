# Name: Albert Chap
# Date: 01 June 2021
# Description: Final Project Kuba Game simulator

class KubaGame :
    def __init__(self, playerA_tuple, playerB_tuple) :
        """ initializes the board with taking in the tuples for each player and determing
            This method is also for initializing the board.
        INITIALIZES BOARD
        """
        self._playerA = playerA_tuple
        self._playerB = playerB_tuple
        self._playerA_red_count = 0
        self._playerB_red_count = 0
        self._marble_count = (0,0,0)
        self._marble_count_list = list(self._marble_count)

        self._playerA_W_counter = 0
        self._playerA_B_counter = 0
        self._playerA_R_counter = 0
        self._playerB_W_counter = 0
        self._playerB_B_counter = 0
        self._playerB_R_counter = 0

        self._playerA_pieces = [self._playerA_W_counter,self._playerA_B_counter,self._playerA_R_counter]  # create a dictionary of all the pieces W,B,R
        self._playerB_pieces = [self._playerB_W_counter,self._playerB_B_counter, self._playerB_R_counter]  # create a dictionary of all teh pieces W,B,R

        self._winner = None
        self._player_turn = None
        self._white = 'W'
        self._black = 'B'
        self._previous_move = []  # This matrix can store previous board movement and will get updated
        # self._gameboard = [['W', 'W', '', '', '', 'B', 'B'],
        #                    ['W', 'W', '', 'R', '', 'B', 'B'],
        #                    ['', '', 'R', 'R', 'R', '', ''],
        #                    ['', 'R', 'R', 'R', 'R', 'R', ''],
        #                    ['', '', 'R', 'R', 'R', '', ''],
        #                    ['B', 'B', '', 'R', '', 'W', 'W'],
        #                    ['B', 'B', '', '', '', 'W', 'W']]
        self._gameboard = [['', '', '', '', 'W', 'B', 'B'],
                           ['W', 'W', '', 'W', '', 'B', 'B'],
                           ['', '', 'R', 'R', 'R', '', ''],
                           ['', 'R', 'R', 'R', 'R', 'R', ''],
                           ['', '', 'R', 'R', 'R', '', ''],
                           ['B', 'B', '', 'R', '', 'W', 'W'],
                           ['B', 'B', '', 'R', '', 'W', 'W']]

    def get_current_turn(self) :
        """ returns players name whose turn it is
            return none if no player has made first move yet
            TRACK PLAYERS TURN
        """
        return self._player_turn

    def set_current_turn(self, player_name):
        self._player_turn = player_name
        return self._player_turn

    def get_winner(self) :
        """ returns winner of the game
            if no winner return none
        """
        return self._winner

    def set_winner(self, name) :
        """"
        sets winner of the game ,m updates winner
        """
        self._winner = name

    def get_captured(self, player_name) :
        """
        returns the number of Red marbles captured by the player
        :param player_name:
        :return:
        """
        if player_name == self._playerA[0]:
            return self._playerA_red_count
        elif player_name == self._playerB[0]:
            return self._playerB_red_count

    def get_marble(self, coordinates) :
        """
        use coordinates given in tuple format to extract the row and column
        to find what marble is there. compare against the current game board.
        """
        row = coordinates[0]
        column = coordinates[1]
        if self._gameboard[row][column] != '':
            return self._gameboard[row][column]
        else:
            return 'X'

    def get_marble_count(self) :
        """
        GET MARBLE COUNT
        scans the current board to get how many per each, returns a tuple (W,B,R)
        :return:
        """
        for i in self._gameboard :
            for j in i :
                if j == 'R' :
                    self._marble_count_list[2] += 1
                elif j == 'B' :
                    self._marble_count_list[1] += 1
                elif j == 'W' :
                    self._marble_count_list[0] += 1
        self._marble_count = tuple(self._marble_count_list)
        return self._marble_count

    def move_left_board(self, player_name, row, column):
        """
        this method utilizes the move_left method,
        uses row to grab specific row and create a new list = row_board
        call move left method (column, row_board)
        pop old row
        insert new row
        update list of board orientations
        return new board
        :param row:
        :param column:
        :param board:
        :return: new board
        """
        if column == 0 :
            if self._gameboard[row][0] == 'R':
                if player_name == self._playerA[0] :
                    self._playerA_red_count += 1
                    if self._playerA_red_count == 7 :
                        self._winner = self._playerA[0]
                else :
                    self._playerB_red_count += 1
                    if self._playerB_red_count == 7 :
                        self._winner = self._playerB[0]
            elif self._playerA[1] != self._gameboard[row][0] :
                if self._playerB[1] == 'B' :
                    if self._marble_count[1] == 1 :
                        self._winner = self._playerA[0]
                elif self._playerB[1] == 'W' :
                    if self._marble_count[0] == 1 :
                        self._winner = self._playerA[0]
            elif self._playerB[1] != self._gameboard[row][0] :
                if self._playerA[1] == 'B' :
                    if self._marble_count[1] == 1 :
                        self._winner = self._playerB[0]
                elif self._playerA[1] == 'W' :
                    if self._marble_count[0] == 1 :
                        self._winner = self._playerB[0]
            self._gameboard[row][0] = ''
        elif self._gameboard[row][column] == '' :
            return None
        else:
            self.move_left_board(player_name,row, column - 1)
            self._gameboard[row][column - 1] = self._gameboard[row][column]
            self._gameboard[row][column] = ''
        if self._player_turn is None :
            self.set_current_turn(player_name)
        elif self._player_turn == self._playerA[0] :
            self.set_current_turn(self._playerB[0])
        elif self._player_turn == self._playerB[0] :
            self.set_current_turn(self._playerA[0])
        return True

    def move_right_board(self, player_name, row, column) :
        """
        right movement on the board takes in the following parameters:
        :param player_name:
        :param row:
        :param column:
        :param board:
        :return:
        """
        if column == 6:
            if self._gameboard[row][6] == 'R':
                if player_name == self._playerA[0] :
                    self._playerA_red_count += 1
                    if self._playerA_red_count == 7 :
                        self._winner = self._playerA[0]
                else :
                    self._playerB_red_count += 1
                    if self._playerB_red_count == 7 :
                        self._winner = self._playerB[0]
            elif self._playerA[1] != self._gameboard[row][6] :
                if self._playerB[1] == 'B' :
                    if self._marble_count[1] == 1 :
                        self._winner = self._playerA[0]
                elif self._playerB[1] == 'W' :
                    if self._marble_count[0] == 1 :
                        self._winner = self._playerA[0]
            elif self._playerB[1] != self._gameboard[row][6] :
                if self._playerA[1] == 'B' :
                    if self._marble_count[1] == 1 :
                        self._winner = self._playerB[0]
                elif self._playerA[1] == 'W' :
                    if self._marble_count[0] == 1 :
                        self._winner = self._playerB[0]
            self._gameboard[row][6] = ''
        elif self._gameboard[row][column] == '':
            return None
        else:
            self.move_right_board(player_name, row, column + 1)
            self._gameboard[row][column + 1] = self._gameboard[row][column]
            self._gameboard[row][column] = ''
        if self._player_turn is None :
            self.set_current_turn(player_name)
        elif self._player_turn == self._playerA[0] :
            self.set_current_turn(self._playerB[0])
        elif self._player_turn == self._playerB[0] :
            self.set_current_turn(self._playerA[0])
        return True
    def move_forward_board(self, player_name, row, column):
        """
        This method will keep track of up ward movement
        - will iterate through the current matrix (get current board setup) of the board and grab the individual
        elements and convert into a row.
         - move forward utilizes the move right when column is transposed into a row: call move right method to
         create new.
         modified list
         - iterate through teh board and iterate through the modified list and place values in their respective
            sections
        return board

        :param row:
        :param column:
        :param board:
        :return:new board layout (update new board layout and put new board in the list in init method)
        """
        if row == 0:
            if self._gameboard[row][column] == 'R':
                if player_name == self._playerA[0]:
                    self._playerA_red_count += 1
                    if self._playerA_red_count == 7:
                        self._winner = self._playerA[0]
                else:
                    self._playerB_red_count += 1
                    if self._playerB_red_count == 7 :
                        self._winner = self._playerB[0]
            elif self._playerA[1] != self._gameboard[0][column] :
                if self._playerB[1] == 'B' :
                    if self._marble_count[1] == 1 :
                        self._winner = self._playerA[0]
                elif self._playerB[1] == 'W' :
                    if self._marble_count[0] == 1 :
                        self._winner = self._playerA[0]
            elif self._playerB[1] != self._gameboard[0][column] :
                if self._playerA[1] == 'B' :
                    if self._marble_count[1] == 1 :
                        self._winner = self._playerB[0]
                elif self._playerA[1] == 'W' :
                    if self._marble_count[0] == 1 :
                        self._winner = self._playerB[0]
            self._gameboard[0][column] = ''
        elif self._gameboard[row][column] == '':
            return None
        else:
            self.move_forward_board(player_name, row-1, column)
            self._gameboard[row-1][column] = self._gameboard[row][column]
            self._gameboard[row][column] = ''
        if self._player_turn is None :
            self.set_current_turn(player_name)
        elif self._player_turn == self._playerA[0] :
            self.set_current_turn(self._playerB[0])
        elif self._player_turn == self._playerB[0] :
            self.set_current_turn(self._playerA[0])
        return True

    def move_back_board(self, player_name, row, column):
        """
        This method will keep track of the backwards movement
        - iterate through the current matrix (get current board setup) of the board and grab the individual elements and
        convert into a row.
        -move back utilitzes same functionality as move left when column is transposed into a row: call move left method
        to create new
        :param row:
        :param column:
        :param board:
        :return: new board layout
        """
        if row == 6:
            if self._gameboard[6][column] == 'R':
                if player_name == self._playerA[0]:
                    self._playerA_red_count += 1
                    if self._playerA_red_count == 7:
                        self._winner = self._playerA[0]
                else:
                    self._playerB_red_count += 1
                    if self._playerB_red_count == 7:
                        self._winner = self._playerB[0]
            elif self._playerA[1] != self._gameboard[6][column]:
                if self._playerB[1] == 'B':
                    if self._marble_count[1] == 1:
                        self._winner = self._playerA[0]
                elif self._playerB[1] == 'W':
                    if self._marble_count[0] == 1:
                        self._winner = self._playerA[0]
            elif self._playerB[1] != self._gameboard[6][column] :
                if self._playerA[1] == 'B' :
                    if self._marble_count[1] == 1 :
                        self._winner = self._playerB[0]
                elif self._playerA[1] == 'W' :
                    if self._marble_count[0] == 1 :
                        self._winner = self._playerB[0]
            self._gameboard[6][column] = ''
        elif self._gameboard[row][column] == '':
            return None
        else:
            self.move_back_board(player_name, row+1,column)
            self._gameboard[row+1][column] = self._gameboard[row][column]
            self._gameboard[row][column] = ''
        if self._player_turn is None :
            self.set_current_turn(player_name)
        elif self._player_turn == self._playerA[0] :
            self.set_current_turn(self._playerB[0])
        elif self._player_turn == self._playerB[0] :
            self.set_current_turn(self._playerA[0])
        return True

    def make_move_helper(self, player_name, coordinates, direction):
        row = coordinates[0]
        column = coordinates[1]
        self._previous_move.clear()
        self._previous_move.append(coordinates)
        if direction == 'L' :
            self._previous_move.append(direction)
            return self.move_left_board(player_name, row, column)
        elif direction == 'R' :
            self._previous_move.append(direction)
            return self.move_right_board(player_name, row, column)
        elif direction == 'F' :
            self._previous_move.append(direction)
            return self.move_forward_board(player_name, row, column)
        elif direction == 'B' :
            self._previous_move.append(direction)
            return self.move_back_board(player_name, row, column)


    def make_move(self, player_name, coordinates, direction) :
        """
        USES OTHER METHODS TO DETERMINE MOVEMENT ON BOARD

        This method will be used to determing the move of the player.
        - directions are L,R,F,B,
        - uses validate_move to check if validate move is true or false:
                if false return false
                if true check to see if player scores with score method
                if L use move_left_board (utilize whatever direction of that list)
                update the board after wards with the copied board
                and add the new board orientation in the new list
        - check if we have a winner if true
            -print winner


        """
        # Sets the rows and columns from the parameter to use in methods
        row = coordinates[0]
        column = coordinates[1]
        if (row not in range(0,7) or column not in range(0,7)) or\
            (coordinates in self._previous_move and direction in self._previous_move) or \
             (self._player_turn != player_name and self._player_turn is not None) or\
            (self._gameboard[row][column] == '' or self._winner is not None):
            return False
        elif direction == 'R':
            if self._gameboard[coordinates[0]][coordinates[1]-1] != '' and coordinates[1] > 0:
                return False
            elif player_name == self._playerA[0]:
                if self._gameboard[row][6] == self._playerA[1] and '' not in self._gameboard[row]:
                    return False
                else:
                    return self.make_move_helper(player_name,coordinates,direction)
            elif player_name == self._playerB[0]:
                if self._gameboard[row][6] == self._playerB[1] and '' not in self._gameboard[row]:
                    return False
                else:
                    return self.make_move_helper(player_name, coordinates, direction)

        elif direction == 'L':
            if self._gameboard[coordinates[0]][coordinates[1]+1] != '' and coordinates[1] < 6:
                return False
            elif player_name == self._playerA[0]:
                if self._gameboard[row][0] == self._playerA[1]:
                    return False
                else:
                    return self.make_move_helper(player_name, coordinates, direction)
            elif player_name == self._playerB[0]:
                if self._gameboard[row][0] == self._playerB[1]:
                    return False
                else:
                    return self.make_move_helper(player_name, coordinates, direction)
            # else:
            #     pass
        elif direction == 'F':
            column_list = [i[column] for i in self._gameboard]
            if row < 6 and self._gameboard[row+1][column] != '':
                return False
            elif player_name == self._playerA[0]:
                if self._gameboard[0][column] == self._playerA[1] and '' not in column_list:
                    column_list.clear()
                    return False
                else:
                    return self.make_move_helper(player_name, coordinates, direction)
            elif player_name == self._playerB[0]:
                if self._gameboard[0][column] == self._playerB[1] and '' not in column_list:
                    column_list.clear()
                    return False
                else:
                    return self.make_move_helper(player_name, coordinates, direction)
        elif direction == 'B':
            column_list = [i[column] for i in self._gameboard]
            if row > 0 and self._gameboard[row-1][column] != '':
                return False
            elif player_name == self._playerA[0]:
                if self._gameboard[6][column] == self._playerA[1] and '' not in column_list:
                    column_list.clear()
                    return False
                else:
                    return self.make_move_helper(player_name, coordinates, direction)
            elif player_name == self._playerB[0]:
                if self._gameboard[6][column] == self._playerB[1] and '' not in column_list:
                    column_list.clear()
                    return False
                else:
                    return self.make_move_helper(player_name, coordinates, direction)


        # else:
        #     self._previous_move.clear()
        #     self._previous_move.append(coordinates)
        #     if direction == 'L':
        #         self._previous_move.append(direction)
        #         return self.move_left_board(player_name, row, column)
        #     elif direction == 'R':
        #         self._previous_move.append(direction)
        #         return self.move_right_board(player_name, row, column)
        #     elif direction == 'F' :
        #         self._previous_move.append(direction)
        #         return self.move_forward_board(player_name, row, column)
        #     elif direction == 'B' :
        #         self._previous_move.append(direction)
        #         return self.move_back_board(player_name, row, column)
        #     return True





#
game = KubaGame(('PlayerA', 'W'), ('PlayerB', 'B'))
# print(game.get_marble_count()) #returns (8,8,13)
#
# print(game.make_move('PlayerA', (0,7), 'R'))
# print(game.make_move('PlayerA', (6,5), 'L')) #Cannot make this move
# print(game.get_captured('PlayerA')) #returns 0
# print(game.get_current_turn()) #returns 'PlayerB' because PlayerA has just played.
# print(game.get_winner()) #returns None
#
# print(game.get_marble((5,5)) )#returns 'W'
print(game.move_right_board('John',0,4))
print(game._gameboard)