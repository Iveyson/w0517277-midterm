class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        print("Grid initialized.")


class Mouse:
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        print("Mouse initialized.")

#cursor is 0,0 for default position, but can be moved by the user to select a cell on the grid.
class Cursor:
    def __init__(self):
        self.x = 0
        self.y = 0
        print("Cursor initialized.")


class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("Wall initialized.")


class ScoreManager:
    def __init__(self):
        self.score = 0
        print("Score Manager initialized.")

#Game controller is responsible for initializing the game and managing the interactions between the game objects.
#currently it is just responsible for initializing the game objects
class GameController:
    def __init__(self):
        self.grid = None
        self.mouse = None
        self.cursor = None
        self.score_manager = None
        print("Game Controller created.")

    def initialize_game(self):
        self.grid = Grid(10, 10)
        self.mouse = Mouse(5, 5)
        self.cursor = Cursor()
        self.score_manager = ScoreManager()
        print("Game initialized.")



game = GameController()
game.initialize_game()