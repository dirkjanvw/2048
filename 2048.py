#!/usr/bin/env python3
# Created by Dirk-Jan (2023)
# Recreating the 2048 game in python.

import random

class Game:
    def __init__(self, size: int):
        self.size = size
        self.board = [[0 for i in range(self.size)] for j in range(self.size)]

        # first generation
        self.generate()

    def __str__(self) -> str:
        """
        Shows the board of the 2048 game.
        """
        output = ""

        # first line
        width = len(str(max([x for y in self.board for x in y])))
        output += "="
        for i in range(self.size):
            output += "="*(width+1)
        output += "\n"

        # next lines
        for j in range(self.size):
            output += "|"
            for i in range(self.size):
                output += f"{self.board[i][j]:>{width}}|"
            output += "\n"
            output += "="
            for i in range(self.size):
                output += "="*(width+1)
            output += "\n"
        
        # return
        return output

    def generate(self) -> None:
        """
        Generate two new tiles on the board
        """

        # Get all fields that are 0
        empty = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    empty.append((i,j))

        # Get two random tiles to put number
        to_generate = []
        for i in range(2):
            pick = random.choice(empty)
            to_generate.append(pick)
            empty.remove(pick)

        # Put numbers on board
        for tile in to_generate:
            self.board[tile[0]][tile[1]] = 2

    def play(self, move: str) -> None:
        """
        Plays a move in the 2048 game.

        Arguments:
            move (str): h, j, k, or l meaning: left, down, up c.q. right
        """

        match move:
            case 'h':
                self.move_left()
            case 'j':
                self.move_down()
            case 'k':
                self.move_up()
            case 'l':
                self.move_right()

    def move_left(self) -> None:
        """
        """

    def move_right(self) -> None:
        """
        """

        #for i in range(self.size):
        #    new = [0 for k in range(self.size)]
        #    p = self.size
        #    for j in range(self.size):

    def move_down(self) -> None:
        """
        """
        for i in range(self.size):
            new = [0 for k in range(self.size)]
            p = self.size-1
            for j in range(self.size):
                if self.board[i][j] != 0:
                    new[p] = self.board[i][j]
                    p -= 1
            self.board[i] = new

    def move_up(self) -> None:
        """
        """
        for i in range(self.size):
            new = [0 for k in range(self.size)]
            p = 0
            for j in range(self.size):
                if self.board[i][j] != 0:
                    new[p] = self.board[i][j]
                    p += 1
            self.board[i] = new

def get_input() -> str:
    """
    Gets user input for movement.

    Returns:
        str: h, j, k, or l meaning: left, down, up c.q. right
    """

    move = ''
    while move not in ['h','j','k','l']:
        move = input("next move (h/j/k/l): ")

    return move

def main():
    # Initialise game
    game = Game(4)

    # Play game
    while True:
        print(game)
        game.play(get_input())
        #print(game)
        game.generate()

if __name__ == "__main__":
    main()
