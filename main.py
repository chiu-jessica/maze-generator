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
            if [row-1, col] not in self.walls:
                self.walls.append([row-1, col])
        if row < len(self.board)-1 and self.board[row+1][col] == "u":
            self.board[row+1][col] = "w"
            if [row+1, col] not in self.walls:
                self.walls.append([row+1, col])
        if col > 0 and self.board[row][col-1] == "u":
            self.board[row][col-1] = "w"
            if [row, col-1] not in self.walls:
                self.walls.append([row, col-1])
        if col < len(self.board[row]) and self.board[row][col+1] == "u":
            self.board[row][col+1] = "w"
            if [row, col+1] not in self.walls:
                self.walls.append([row, col+1])
    
    def removeWall(self, row, col):
        for wall in self.walls:
            if wall[0] == row and wall[1] == col:
                self.walls.remove(wall)

    def breakWall(self, wall:tuple[int, int]):
        cells = self.surroundingCells(wall)
        if cells < 2:
            self.board[wall[0]][wall[1]] = "c"
            self.removeWall(wall[0], wall[1])
            self.addWalls(wall[0], wall[1])
            return True
        else:
            return False

    def generate(self):
        startingRow = random.randint(1, self.height-2) 
        startingCol = random.randint(1, self.width-2)
        self.board[startingRow][startingCol] = "c"
        self.walls.extend([[startingRow-1, startingCol], [startingRow, startingCol-1], [startingRow+1, startingCol], [startingRow, startingCol+1]])
        self.board[startingRow-1][startingCol] = "w"
        self.board[startingRow][startingCol-1] = "w"
        self.board[startingRow+1][startingCol] = "w"
        self.board[startingRow][startingCol+1] = "w"
 
        while len(self.walls):
            randWall = self.walls[random.randint(0, len(self.walls)-1)]
            # create left and right path
            if randWall[1] != 0:
                if self.board[randWall[0]][randWall[1]-1] == "u" and self.board[randWall[0]][randWall[1]+1] == "c":
                    if self.breakWall(randWall):
                        continue
            if randWall[1] != len(self.board[0])-1:
                if self.board[randWall[0]][randWall[1]+1] == "u" and self.board[randWall[0]][randWall[1]-1] == "c":
                    if self.breakWall(randWall):
                        continue

            # create top and bottom path
            if randWall[0] != 0:
                if self.board[randWall[0]-1][randWall[1]] == "u" and self.board[randWall[0]+1][randWall[1]] == "c":
                    if self.breakWall(randWall):
                        continue
            if randWall[0] != len(self.board)-1:
                if self.board[randWall[0]+1][randWall[1]] == "u" and self.board[randWall[0]-1][randWall[1]] == "c":
                    if self.breakWall(randWall):
                        continue

            self.removeWall(randWall[0], randWall[1])

        found_start = False
        found_end = False
        # replace remaining u's to w's
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == "u":
                    self.board[i][j] = "w"

        # create start and end
        for i in range(len(self.board[0])):
            if not found_start and self.board[1][i] == "c":
                self.board[0][i] = "c"
                found_start = True
            if not found_end and self.board[len(self.board)-2][len(self.board[0])-1-i] == "c":
                self.board[len(self.board)-1][len(self.board[0])-1-i] = "c" # checking from right to left (opp side)
                found_end = True
            if found_end and found_start:
                break
        
    def surroundingCells(self, wall):
        cellCounter = 0
        if self.board[wall[0]-1][wall[1]] == "c":
            cellCounter += 1
        if self.board[wall[0]+1][wall[1]] == "c":
            cellCounter += 1
        if self.board[wall[0]][wall[1]-1] == "c":
            cellCounter += 1
        if self.board[wall[0]][wall[1]+1] == "c":
            cellCounter += 1
        
        return cellCounter

if __name__ == "__main__":
    maze = Maze(20, 20)
    maze.initMaze()
    maze.generate()
    maze.printBoard()
