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
                if self.board[i][j] == "c":
                    print(Fore.WHITE, self.board[i][j], end = " ")
                elif self.board[i][j] == "w":
                    print(Fore.RED, self.board[i][j], end = " ")
                else:
                    print(Fore.BLUE, self.board[i][j], end = " ")
            print()

    def addWalls(self, row, col):
        if row > 0 and self.board[row-1][col] =="u":
            self.board[row-1][col] = "w"
            self.walls.append([row-1, col])
        if row < len(self.board)-1 and self.board[row+1][col] == "u":
            self.board[row+1][col] = "w"
            self.walls.append([row+1, col])
        if col > 0 and self.board[row][col-1] == "u":
            self.board[row][col-1] = "w"
            self.walls.append([row, col-1])
        if col < len(self.board[row]) and self.board[row][col+1] == "u":
            self.board[row][col+1] = "w"
            self.walls.append([row, col+1])

    def generate(self):
        startingRow = random.randint(1, self.height-2) 
        startingCol = random.randint(1, self.width-2)
        self.board[startingRow][startingCol] = "c"
        self.walls.extend([[startingRow-1, startingCol], [startingRow, startingCol-1], [startingRow+1, startingCol], [startingRow, startingCol+1]])
        self.board[startingRow-1][startingCol] = "w"
        self.board[startingRow][startingCol-1] = "w"
        self.board[startingRow+1][startingCol] = "w"
        self.board[startingRow][startingCol+1] = "w"
 
        counter = 0
        while len(self.walls):
            randWall = self.walls[random.randint(0, len(self.walls)-1)]
            if counter == 4:
                break
            # build path up or down
            if randWall[0] != 0 and randWall[0] != len(self.board)-1:
                if (self.board[randWall[0]-1][randWall[1]] == "u" and self.board[randWall[0]+1][randWall[1]] == "c") or (self.board[randWall[0]+1][randWall[1]] == "u" and self.board[randWall[0]-1][randWall[1]] == "c"):
                    self.board[randWall[0]][randWall[1]] = "c"
                    self.walls.remove(randWall)
                    self.addWalls(randWall[0], randWall[1])
            # build path left or right
            if randWall[1] != 0 and randWall[1] != len(self.board)-1:
                if (self.board[randWall[0]][randWall[1]-1] == "u" and self.board[randWall[0]][randWall[1]+1] == "c") or (self.board[randWall[0]][randWall[1]+1] == "u" and self.board[randWall[0]][randWall[1]-1] == "c"):
                    self.board[randWall[0]][randWall[1]] = "c"
                    self.walls.remove(randWall)
                    self.addWalls(randWall[0], randWall[1])

            counter += 1
    
if __name__ == "__main__":
    maze = Maze(6, 6)
    maze.initMaze()
    maze.generate()
    maze.printBoard()
