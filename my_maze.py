"""Algorithms and Data Structures 1 AI - Maze Solving."""
# Using constants might make this more readable.
from typing import override

START = "S"
EXIT = "X"
VISITED = "."
OBSTACLE = "#"
PATH = " "


class MyMaze:
    """Maze object, used for demonstrating recursive algorithms."""

    def __init__(self, maze_str: str):
        """Initialize Maze.

        Args:
            maze_str (str): Maze represented by a string, 
                where rows are separated by newlines (\n).
        """
        # We internally treat this as a list[list[str]], as it makes indexing easier.
        self._maze = list(list(row) for row in maze_str.splitlines())
        self._height = len(self._maze)
        self._width = len(self._maze[0])
        self._exits: list[tuple[int, int]] = []
        self._max_recursion_depth = 0

    def find_exits(self, start_row: int, start_col: int, depth: int = 0):
        """Find and save all exits into `self._exits` using recursion, save
        the maximum recursion depth into `self._max_recursion_depth` and mark the maze.

        An exit is an accessible from an empty cell on the outer rims of the maze.

        You can assume that the starting point is in an empty cell and not on the outer rim.

        Args:
            start_row (int): row to start from. 0 represents the topmost cell.
            start_col (int): column to start from; 0 represents the leftmost cell.
            depth (int): Depth of current iteration.
        """
        if depth > self._max_recursion_depth:
            self._max_recursion_depth = depth
        #Checking if the current cell is not an exitб if it is we found an exit
        is_on_edge = (
            start_row == 0 or
            start_row == self._height - 1 or
            start_col == 0 or
            start_col == self._width - 1
        )
        if is_on_edge:
            self._maze[start_row][start_col] = EXIT
            self._exits.append((start_row, start_col))
            return
        # If not an exit assign the overcamed cell
        if depth == 0:
            self._maze[start_row][start_col] = START
        else:
            self._maze[start_row][start_col] = VISITED
        #Assigning the directions' incrementing pair order for checking the nighbors
        directions = [
            (0, 1),  #East
            (1, 1),  #SouthEast
            (1, 0),  #South
            (1, -1), #SouthWest
            (0, -1), #West
            (-1, -1),#NorthWest
            (-1, 0), #North
            (-1, 1) #NorthEast
        ]
        #Iterating though the neghbours taking every incrementing pair and moving to the next cell
        for row_step, col_step in directions:
            new_row = start_row + row_step
            new_col = start_col + col_step
            #Checking if the cells are in the maze bounds
            if 0 <= new_row < self._height and 0 <= new_col < self._width:
                #moving if only the next cell is not bstacle and visited
                if self._maze[new_row][new_col] == PATH:
                    self.find_exits(new_row, new_col, depth + 1)





        

    @property
    def exits(self) -> "list[tuple[int, int]]":
        """List of tuples of (row, col)-coordinates of currently found exits."""
        return self._exits

    @property
    def max_recursion_depth(self) -> int:
        """Return the maximum recursion depth after executing find_exits()."""
        return self._max_recursion_depth

    @override
    def __str__(self) -> str:
        return "\n".join("".join(row) for row in self._maze)

#Constracting own maze for testing 15*15
if __name__ == "__main__":
    print('Test Custom Maze 15*15')
    lines15 = ['#' * 15] 
    for i in range(1,14):
        if i % 2 != 0:
            lines15.append('#' + ' ' * 13 + '#')
        else:
            if i % 4 == 0:
                lines15.append('# ' + '#' * 13)
            else:
                lines15.append('#' * 13 + ' #')
    lines15.append('#' * 14 + ' ')
    maze_15_structure = "\n".join(lines15)

    my_maze_15 = MyMaze(maze_15_structure)
    my_maze_15.find_exits(1, 1)
    print(my_maze_15)
    print(f"Max recursion depth: {my_maze_15.max_recursion_depth}")


    #Maze 20*20
    print('\nTest Custom Maze 20*20')
    lines20 = ['#' * 20]
    for i in range(1, 19):
        if i % 3 == 0:
            wall = list("#" * 20)
            for j in range(2, 19, 4):
                wall[j] = " "
            lines20.append("".join(wall))
        else:
            room = list("#" + " " * 18 + "#")
            for j in range(4, 19, 4):
                room[j] = "#"
            lines20.append("".join(room))
            
    lines20.append('#' * 19 + ' ')
    maze_20_structure = "\n".join(lines20)
    
    my_maze_20 = MyMaze(maze_20_structure)
    my_maze_20.find_exits(1, 1)
    print(my_maze_20)
    print(f"Max recursion depth: {my_maze_20.max_recursion_depth}")



    

