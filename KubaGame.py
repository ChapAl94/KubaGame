# Name: Albert Chap
# Date: 01 June 2021
# Description: Final Project

class KubaGame:
    def __init__(self,playerA_tuple ,playerB_tuple):
        """ initializes the board with taking in the tuples for each player and determing
            This method is also for initializing the board.
        INITIALIZES BOARD
        """
        self._playerA_name = playerA_tuple[0]
        self._playerB_name = playerB_tuple[0]
        self._playerA_color = playerA_tuple[1]
        self._playerB_color = playerB_tuple[1]
        self._playerA_pieces = {}  # create a dictionary of all the pieces W,B,R
        self._playerB_pieces = {}  # create a dictionary of all teh pieces W,B,R
        self._winner = None
        self._playerturn = None
        self._white = 'W'
        self._black = 'B'
        self._previous_board_orientation = []               #This matrix can store previous board movement and will get updated
        self._gameboard = [['W','W','','','','B','B'],
                           ['W','W','','R','','B','B'],
                           ['','','R','R','R','',''],
                           ['','R','R','R','R','R',''],
                           ['','','R','R','R','',''],
                           ['W','W','','R','','B','B'],
                           ['W','W','','','','B','B']]

    def get_current_turn(self):
        """ returns players name whose turn it is
            return none if no player has made first move yet
            TRACK PLAYERS TURN
        """
        return self._playerturn

    def get_winner(self):
        """ returns winner of the game
            if no winner return none
        """
        return self._winner

    def set_winner(self, name):
        """"
        sets winner of the game ,m updates winner
        """
        self._winner = name

    def get_captured(self, player_name):
        """
        returns the number of Red marbles captured by the player
        :param player_name:
        :return:
        """
        if player_name == "player A":
            return self._playerA_pieces[2]
        elif player_name == "player B":
            return self._playerB_pieces[2]

    def get_marble(self, coordinates):
        """
        use coordinates given in tuple format to extract the row and column
        to find what marble is there. compare agains the current game board.
        """
        row = coordinates[0]
        column = coordinates[1]

        return self._gameboard[row][column]

    def get_marble_count(self):
        """
        GET MARBLE COUNT
        scans the current board to get how many per each, returns a tuple (W,B,R)
        :return:
        """
        pass

    def move_left(self, column,row_board):
        """
        -input is a list.
        -This method keeps track of the left movement of a list.
        -This takes column and creates a separate temporary list that goes from beginning to what is called and
        will be reversed using reverse()
        -Another list is made and for the remainder of that row to add in the end.
        -iterate through the reversed temp list to find '' spaces if there is it will create another
        temp list = temp_list2
        slice from beginning of this templist2  till index of space and use rotation code.
        create a templist three to slice templist1 from index after space to end
        -combine all the lists and revers it assign to temp1_list and reverse back
        -new_row will be temp1list plus end part.

        return new_row

        :param coordinates:
        :param board:
        :return: new_row
        """
        pass

    def move_right(self, column, row_board):
        """
        input is a list.
        This method will be used to keep track of all right movement for given list.
        - create a temp list templist1 that takes the list from the given column input till end of the list using slicing
        - slice the input list from beginning (this will be used for later to put together the whole mutated list)
        - iterate through templist1 if there is a ''
            - find index of the ''
            -create  a templist2 slicing temp1list from beginning to the location of the '' (index)
            - rotate that templist once
            -create another templist for the ending part of templist2
            -create a paramter new_row that adds beginning list, the rotate list, and end
        -else:
         - create beg list slice row_board from beg to column
         -create another list slice from row_board from column to end
         -new row = adding all those lists

         return new_row


        :param coordinates:
        :param board:
        :return: new_row
        """
        pass

    def move_left_board(self,row,column,board):
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
        pass

    def move_right_board(self,row,column,board):
        """
        this method utilitizes move right method,
        -uses row parameter to grab a specific row and create a new list = row_board
        calls move right method( column, row_board
        pop old row from board
        insert new row from board
        return new row

        :param row:
        :param column:
        :param board:
        :return:
        """
        pass

    def move_foward_board(self, row, column, board):
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
        pass

    def move_back_board(self, row, column, board):
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
        pass

    def winning_conditions(self, player):
        """
        take a look at the key of the player
        if player has seven R
        return True

        if player has all opposing color
        return True

        else return false
        :param player:
        :return: Boolean: True or False
        """
        pass

    def validate_mov(self, player, coordinates, direction):
        """
        VALIDATE A MOVE
        check if current player is equal to players turn
            if not return false else return trur
        if direction is left: extract coordinates from tuple
            use get_marble method and pass coordinates to behind the current coordinate through it
            if value from get_marble is '' return true else return false
            use move_left_board to get board orientation and compare if in board orientation list
            if so return false
        if direction is right:
            use get_marbel method and pass coordinates to left of current coordinate
            if value is '' return true else false
            use move_right_board to get board orientation and compare if in board orientation list
            return false
        if direction is forward:
            use get marble method and pass coordinate below:
             if value is '' return true else false
             use move_foward_board to get board orientation and compare if in board orientation list
             return false
        if direction is backwards:
            use get marble method and pass coordinate above:
             if value is '' return true else false
             use move_backward_board to get board orientation and compare if in board orientation list
             return false
        if  winning conditions are true
            return False



        :param player:
        :param coordinates:
        :param direction:
        :return: boolean: True or False
        """
        pass

    def score(self, player, coordinates, direction, board):
        """
        create a scoring list =
        -if L use coordinates to extract row from board
         to find if there are no spaces from beginning of list to location of the list
            if true:
                check to see what color and if so update
            else return none
        -if R use cooridates to extract row form board to find if there are no spaces from location to end of row
            if true:
                check to see what color and if so update
            else return none
        -if F use coordinates to extract row form board to find if there are no spaces from location
                check to see what color and update list with player and list
            return None
        -if B use same logic
            return None
        :param coordinates:
        :param board:
        :return: a list [player, color]
        """
        pass

    def make_move(self, playername, coordinates,direction):
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
        else
            False
        :param direction:
        :param coodinates
        :param playername:
        :return: boolean: True or False

        """
    pass

