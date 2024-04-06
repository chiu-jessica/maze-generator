from colorama import init, Fore
import random

class Maze:
    board = []
    walls = []
    width = 0
    height = 0

    def __init__(self, _width, _height):
        init()
        self.width = _width
        self.height = _height

    def initMaze(self):
        for i in range(self.height):
            line = []
            for j in range(self.width):
                line.append("u")
            self.board.append(line)
        return self.board
    
    def printBoard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(Fore.MAGENTA, self.board[i][j], end = " ")
            print()

    def generate(self):
        startingRow = random.randint(1, self.height-1) 
        startingCol = random.randint(1, self.width-1)
        self.walls.extend([[startingRow-1, startingCol], [startingRow, startingCol-1], [startingRow+1, startingCol], [startingRow, startingCol+1]])
        self.board[startingRow-1][startingCol] = "w"
        self.board[startingRow][startingCol-1] = "w"
        self.board[startingRow+1][startingCol] = "w"
        self.board[startingRow][startingCol+1] = "w"
        
    
if __name__ == "__main__":
    maze = Maze(6, 6)
    maze.initMaze()
    maze.generate()
    maze.printBoard()
