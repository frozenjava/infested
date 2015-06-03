#
# Player.py
# Josh Artuso
# 06/02/15
#
# This is the player object
#

class Player:

    COORD_X = 400
    COORD_Y = 300

    COORD_X_CHANGE = 0
    COORD_Y_CHANGE = 0

    COLOR = (255, 0, 0)
    PLAYER_HEIGHT = 10
    PLAYER_WIDTH = 10

    BOUNDARIES = [800, 600]

    VISUAL_UPDATE_NEEDED = False

    def __init__(self, coordinates=None, color=None):
        if not coordinates:
            coordinates = [400, 300]

        if not color:
            color = (255, 0, 0)

        self.COORD_X = coordinates[0]
        self.COORD_Y = coordinates[1]
        self.COLOR = color

    def request_update_x(self, value):
        """
        Update the players x position
        :param value: The value to change x by
        :return:
        """
        if not self.check_x_boundary(value):
            self.COORD_X_CHANGE = value
        else:
            if self.correct_x_position(value) >= 0:
                self.COORD_X_CHANGE = self.correct_x_position(value)

    def request_update_y(self, value):
        """
        Update the players y position
        :param value: The value to change y by
        :return:
        """
        if not self.check_y_boundary(value):
            self.COORD_Y_CHANGE = value
        else:
            if self.correct_y_position(value) >= 0:
                self.COORD_Y_CHANGE = self.correct_y_position(value)

    def check_x_boundary(self, value=0):
        """
        Check if the player is at the boundaries of the game
        :param value: The value pixels that the player will move next
        :return:
        """
        move_distance = self.PLAYER_WIDTH / 2
        if self.COORD_X + value >= self.BOUNDARIES[0] - move_distance or self.COORD_X + value < 0:
            return True
        else:
            return False

    def check_y_boundary(self, value=0):
        """
        Check if the player is at the boundaries of the game
        :param value: The value pixels that the player will move next
        :return:
        """
        move_distance = self.PLAYER_WIDTH / 2
        if self.COORD_Y + value >= self.BOUNDARIES[1] - move_distance or self.COORD_Y + value < 0:
            return True
        else:
            return False

    def correct_x_position(self, value=0):
        """
        Correct the players x axis position if the pass the boundary
        :return:
        """
        if self.COORD_X + value > self.BOUNDARIES[0] - self.PLAYER_WIDTH:
            return (self.COORD_X + value) - (self.BOUNDARIES[0] - self.PLAYER_WIDTH)
        elif self.COORD_X + value < 0 < self.COORD_X:
            return (self.COORD_X + value) + self.PLAYER_WIDTH

        return 0

    def correct_y_position(self, value=0):
        """
        Correct the players y axis position if the pass the boundary
        :return:
        """
        if self.COORD_Y + value > self.BOUNDARIES[1] - self.PLAYER_HEIGHT:
            return (self.COORD_Y + value) - (self.BOUNDARIES[0] - self.PLAYER_HEIGHT)
        elif self.COORD_Y + value < 0 < self.COORD_Y:
            return (self.COORD_Y + value) + self.PLAYER_HEIGHT

        return 0

    def update_position(self):
        """
        Change the players position
        :return:
        """
        # Check if the player has hit the boundary
        if self.check_x_boundary(self.COORD_X_CHANGE):
            self.COORD_X_CHANGE = 0

        if self.check_y_boundary(self.COORD_Y_CHANGE):
            self.COORD_Y_CHANGE = 0

        self.COORD_X += self.COORD_X_CHANGE
        self.COORD_Y += self.COORD_Y_CHANGE

        if self.COORD_X_CHANGE is not 0 or self.COORD_Y_CHANGE is not 0:
            return True
        else:
            return False

    def draw_player(self, py_game, game_display):
        """
        Draw the player object on the screen
        :param py_game:
        :param game_display:
        :return:
        """
        py_game.draw.rect(game_display, self.COLOR, [self.COORD_X, self.COORD_Y, self.PLAYER_WIDTH, self.PLAYER_HEIGHT])

    def preform_update(self, py_game, game_display, color):
        """
        Update the screen
        :param py_game: The pygame module instance
        :param game_display: A pygame surface object
        :return: None
        """
        updated_needed = self.update_position()

        if updated_needed or self.VISUAL_UPDATE_NEEDED:
            game_display.fill(color)
            self.draw_player(py_game, game_display)
            py_game.display.update()
            self.VISUAL_UPDATE_NEEDED = False
