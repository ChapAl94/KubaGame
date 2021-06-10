# Name: Albert Chap
# Date: 01 June 2021
# Description: Final Project Kuba Game simulator. A game played by two people to see who can capture 7 Red marbles
#              first. This game is played on a 7x7 board.

class KubaGame :
    def __init__(self, playerA_tuple, playerB_tuple) :
        """ initializes the board with taking in the tuples for each player and determining
            This method is also for initializing the board.
        """
        self._playerA = playerA_tuple
        self._playerB = playerB_tuple
        self._playerA_red_count = 0
        self._playerB_red_count = 0
        self._marble_count = (0, 0, 0)
        self._marble_count_list = list(self._marble_count)
        self._winner = None
        self._player_turn = None
        self._white = 'W'
        self._black = 'B'
        self._previous_move = []  # This matrix can store previous board movement and will get updated
        self._gameboard = [['W', 'W', '', '', '', 'B', 'B'],
                           ['W', 'W', '', 'R', '', 'B', 'B'],
                           ['', '', 'R', 'R', 'R', '', ''],
                           ['', 'R', 'R', 'R', 'R', 'R', ''],
                           ['', '', 'R', 'R', 'R', '', ''],
                           ['B', 'B', '', 'R', '', 'W', 'W'],
                           ['B', 'B', '', '', '', 'W', 'W']]

    def get_current_turn(self) :
        """ returns players name whose turn it is
            return none if no player has made first move yet
            TRACK PLAYERS TURN
        """
        return self._player_turn

    def set_current_turn(self, player_name) :
        self._player_turn = player_name
        return self._player_turn

    def get_winner(self) :
        """ returns winner of the game
            if no winner return none
        """
        return self._winner

    def set_winner(self, name) :
        """"
        sets winner of the game ,and updates winner
        """
        self._winner = name

    def get_captured(self, player_name) :
        """
        returns the number of Red marbles captured by the player
        :param player_name:
        :return:
        """
        if player_name == self._playerA[0] :
            return self._playerA_red_count
        elif player_name == self._playerB[0] :
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
        self._marble_count_list[0] = 0
        self._marble_count_list[1] = 0
        self._marble_count_list[2] = 0
        for i in self._gameboard :
            for j in i :
                if j == 'R' :
                    self._marble_count_list[2] += 1
                    self._marble_count = tuple(self._marble_count_list)
                elif j == 'B' :
                    self._marble_count_list[1] += 1
                    self._marble_count = tuple(self._marble_count_list)
                elif j == 'W' :
                    self._marble_count_list[0] += 1
                    self._marble_count = tuple(self._marble_count_list)
        return self._marble_count

    def move_left_board(self, player_name, row, column) :
        """ This method does all the calculations moving left taking in the parameters
        players, row and column. And updates the score.
        :param row:
        :param column:
        :param player_name:
        :return: boolean: True or false
        """
        if column == 0 :
            # Checks to see if the Red is going to be captured
            if self._gameboard[row][0] == 'R' :
                if player_name == self._playerA[0] :
                    self._playerA_red_count += 1
                    if self._playerA_red_count == 7 :
                        self._winner = self._playerA[0]
                else :
                    self._playerB_red_count += 1
                    if self._playerB_red_count == 7 :
                        self._winner = self._playerB[0]
            # Checks to see if the opposing color is going to be captured
            elif self._playerA[1] != self._gameboard[row][0] :
                if self._playerB[1] == 'B' :
                    if self._marble_count[1] == 1 :
                        self._winner = self._playerA[0]
                elif self._playerB[1] == 'W' :
                    if self._marble_count[0] == 1 :
                        self._winner = self._playerA[0]
                return False
            elif self._playerB[1] != self._gameboard[row][0] :
                if self._playerA[1] == 'B' :
                    if self._marble_count[1] == 1 :
                        self._winner = self._playerB[0]
                elif self._playerA[1] == 'W' :
                    if self._marble_count[0] == 1 :
                        self._winner = self._playerB[0]
                return False
            self._gameboard[row][0] = ''
        elif self._gameboard[row][column] == '' :
            return None
        # Recursive call to iterate and move individual pieces to the left
        else :
            self.move_left_board(player_name, row, column - 1)
            self._gameboard[row][column - 1] = self._gameboard[row][column]
            self._gameboard[row][column] = ''
        return True

    def move_right_board(self, player_name, row, column) :
        """
        This method represents the right movement on the board takes in the following parameters:
        :param player_name:
        :param row:
        :param column:
        :return: Boolean: True or False
        """
        if column == 6 :
            # Checks to see if the Red is going to be captured
            if self._gameboard[row][6] == 'R' :
                if player_name == self._playerA[0] :
                    self._playerA_red_count += 1
                    if self._playerA_red_count == 7 :
                        self._winner = self._playerA[0]
                else :
                    self._playerB_red_count += 1
                    if self._playerB_red_count == 7 :
                        self._winner = self._playerB[0]
            # Checks to see if the opposing color is going to be captured
            elif self._playerA[1] != self._gameboard[row][6] :
                if self._playerB[1] == 'B' :
                    if self._marble_count[1] == 1 :
                        self._winner = self._playerA[0]
                elif self._playerB[1] == 'W' :
                    if self._marble_count[0] == 1 :
                        self._winner = self._playerA[0]
                return False
            elif self._playerB[1] != self._gameboard[row][6] :
                if self._playerA[1] == 'B' :
                    if self._marble_count[1] == 1 :
                        self._winner = self._playerB[0]
                elif self._playerA[1] == 'W' :
                    if self._marble_count[0] == 1 :
                        self._winner = self._playerB[0]
                return False
            self._gameboard[row][6] = ''
        elif self._gameboard[row][column] == '' :
            return None
        else :
            # Recursive call to iterate and move individual pieces to the right
            self.move_right_board(player_name, row, column + 1)
            self._gameboard[row][column + 1] = self._gameboard[row][column]
            self._gameboard[row][column] = ''
        return True

    def move_forward_board(self, player_name, row, column) :
        """
        This method will keep track of forward movement
        :param row:
        :param column:
        :param player_name
        :return:Boolean: True or False
        """
        if row == 0 :
            if self._gameboard[row][column] == 'R' :
                if player_name == self._playerA[0] :
                    self._playerA_red_count += 1
                    if self._playerA_red_count == 7 :
                        self._winner = self._playerA[0]
                else :
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
                return False
            elif self._playerB[1] != self._gameboard[0][column] :
                if self._playerA[1] == 'B' :
                    if self._marble_count[1] == 1 :
                        self._winner = self._playerB[0]
                elif self._playerA[1] == 'W' :
                    if self._marble_count[0] == 1 :
                        self._winner = self._playerB[0]
                return False
            self._gameboard[0][column] = ''
        elif self._gameboard[row][column] == '' :
            return None
        else :
            self.move_forward_board(player_name, row - 1, column)
            self._gameboard[row - 1][column] = self._gameboard[row][column]
            self._gameboard[row][column] = ''
        return True

    def move_back_board(self, player_name, row, column) :
        """
        This method will keep track of the backwards movement of pieces, this code will update the board, and update
        players scores and determine who wins

        :param row:
        :param column:
        :param player_name
        :return: True or False
        """
        if row == 6 :
            if self._gameboard[6][column] == 'R' :
                if player_name == self._playerA[0] :
                    self._playerA_red_count += 1
                    if self._playerA_red_count == 7 :
                        self._winner = self._playerA[0]
                else :
                    self._playerB_red_count += 1
                    if self._playerB_red_count == 7 :
                        self._winner = self._playerB[0]
            elif self._playerA[1] != self._gameboard[6][column] :
                if self._playerB[1] == 'B' :
                    if self._marble_count[1] == 1 :
                        self._winner = self._playerA[0]
                elif self._playerB[1] == 'W' :
                    if self._marble_count[0] == 1 :
                        self._winner = self._playerA[0]
                return False
            elif self._playerB[1] != self._gameboard[6][column] :
                if self._playerA[1] == 'B' :
                    if self._marble_count[1] == 1 :
                        self._winner = self._playerB[0]
                elif self._playerA[1] == 'W' :
                    if self._marble_count[0] == 1 :
                        self._winner = self._playerB[0]
                return False
            self._gameboard[6][column] = ''
        elif self._gameboard[row][column] == '' :
            return None
        else :
            self.move_back_board(player_name, row + 1, column)
            self._gameboard[row + 1][column] = self._gameboard[row][column]
            self._gameboard[row][column] = ''
        return True

    def make_move_helper(self, player_name, coordinates, direction) :
        """
        This method is utilized in the make_move, this method calls the directional methods
        in this program.
        :param player_name:
        :param coordinates:
        :param direction:
        :return:
        """
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
        This method validates the move a player makes takes in and returns the following parameters:
        :param player_name:
        :param coordinates:
        :param direction:
        :return: Boolean: True or False
        """
        # Sets the rows and columns from the parameter to use in methods
        row = coordinates[0]
        column = coordinates[1]
        # Checks conditions of the game to make sure move is valid
        if (row not in range(0, 7) or column not in range(0, 7)) or \
                (coordinates in self._previous_move and direction in self._previous_move) or \
                (self._player_turn != player_name and self._player_turn is not None) or \
                (self._gameboard[row][column] == '' or self._winner is not None) :
            return False
        elif direction == 'R' :
            if self._gameboard[coordinates[0]][coordinates[1] - 1] != '' and coordinates[1] > 0 :
                return False
            elif player_name == self._playerA[0] :
                if self._gameboard[row][6] == self._playerA[1] and '' not in self._gameboard[row] :
                    return False
                else :
                    if player_name == self._playerA[0] :
                        self.set_current_turn(self._playerB[0])
                    elif self._player_turn == self._playerB[0] :
                        self.set_current_turn(self._playerA[0])
                    return self.make_move_helper(player_name, coordinates, direction)
            elif player_name == self._playerB[0] :
                if self._gameboard[row][6] == self._playerB[1] and '' not in self._gameboard[row] :
                    return False
                else :
                    if player_name == self._playerA[0] :
                        self.set_current_turn(self._playerB[0])
                    elif self._player_turn == self._playerB[0] :
                        self.set_current_turn(self._playerA[0])
                    return self.make_move_helper(player_name, coordinates, direction)


        elif direction == 'L' :
            if self._gameboard[coordinates[0]][coordinates[1] + 1] != '' and coordinates[1] < 6 :
                return False
            elif player_name == self._playerA[0] :
                if self._gameboard[row][0] == self._playerA[1] :
                    return False
                else :
                    if player_name == self._playerA[0] :
                        self.set_current_turn(self._playerB[0])
                    elif self._player_turn == self._playerB[0] :
                        self.set_current_turn(self._playerA[0])
                    return self.make_move_helper(player_name, coordinates, direction)
            elif player_name == self._playerB[0] :
                if self._gameboard[row][0] == self._playerB[1] :
                    return False
                else :
                    if player_name == self._playerA[0] :
                        self.set_current_turn(self._playerB[0])
                    elif self._player_turn == self._playerB[0] :
                        self.set_current_turn(self._playerA[0])
                    return self.make_move_helper(player_name, coordinates, direction)


        elif direction == 'F' :
            column_list = [i[column] for i in self._gameboard]
            if row < 6 and self._gameboard[row + 1][column] != '' :
                return False
            elif player_name == self._playerA[0] :
                if self._gameboard[0][column] == self._playerA[1] and '' not in column_list :
                    column_list.clear()
                    return False
                else :
                    if player_name == self._playerA[0] :
                        self.set_current_turn(self._playerB[0])
                    elif self._player_turn == self._playerB[0] :
                        self.set_current_turn(self._playerA[0])
                    return self.make_move_helper(player_name, coordinates, direction)
            elif player_name == self._playerB[0] :
                if self._gameboard[0][column] == self._playerB[1] and '' not in column_list :
                    column_list.clear()
                    return False
                else :
                    if player_name == self._playerA[0] :
                        self.set_current_turn(self._playerB[0])
                    elif self._player_turn == self._playerB[0] :
                        self.set_current_turn(self._playerA[0])
                    return self.make_move_helper(player_name, coordinates, direction)
        elif direction == 'B' :
            column_list = [i[column] for i in self._gameboard]
            if row > 0 and self._gameboard[row - 1][column] != '' :
                return False
            elif player_name == self._playerA[0] :
                if self._gameboard[6][column] == self._playerA[1] and '' not in column_list :
                    column_list.clear()
                    return False
                else :
                    if player_name == self._playerA[0] :
                        self.set_current_turn(self._playerB[0])
                    elif self._player_turn == self._playerB[0] :
                        self.set_current_turn(self._playerA[0])
                    return self.make_move_helper(player_name, coordinates, direction)
            elif player_name == self._playerB[0] :
                if self._gameboard[6][column] == self._playerB[1] and '' not in column_list :
                    column_list.clear()
                    return False
                else :
                    if player_name == self._playerA[0] :
                        self.set_current_turn(self._playerB[0])
                    elif self._player_turn == self._playerB[0] :
                        self.set_current_turn(self._playerA[0])
                    return self.make_move_helper(player_name, coordinates, direction)




