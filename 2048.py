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

    def play(self) -> None:
        """
        """

def main():
    # Initialise game
    game = Game(4)

    # Play game
    print(game)


if __name__ == "__main__":
    main()
