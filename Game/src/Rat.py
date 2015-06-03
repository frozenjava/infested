#
# Rat.py
# Josh Artuso
# 06/03/16
#
# This is the Rat class
#


class Rat:

    COORD_X_CHANGE = 0
    COORD_Y_CHANGE = 0

    COLOR = (0, 0, 0)
    RAT_HEIGHT = 10
    RAT_WIDTH = 10

    BOUNDARIES = [800, 600]

    FOLLOW_PLAYER = False

    def __init__(self, coordinates=None, color=None):
        if not coordinates:
            coordinates = [0, 0]

        if not color:
            color = (0, 0, 0)

        self.COORD_X = coordinates[0]
        self.COORD_Y = coordinates[1]
        self.COLOR = color

    def request_update_x(self, value):
        """
        Update the rats x position
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
        Update the rats y position
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
        Check if the rat is at the boundaries of the game
        :param value: The value pixels that the rat will move next
        :return:
        """
        move_distance = self.RAT_WIDTH / 2
        if self.COORD_X + value >= self.BOUNDARIES[0] - move_distance or self.COORD_X + value < 0:
            return True
        else:
            return False

    def check_y_boundary(self, value=0):
        """
        Check if the rat is at the boundaries of the game
        :param value: The value pixels that the rat will move next
        :return:
        """
        move_distance = self.RAT_WIDTH / 2
        if self.COORD_Y + value >= self.BOUNDARIES[1] - move_distance or self.COORD_Y + value < 0:
            return True
        else:
            return False

    def correct_x_position(self, value=0):
        """
        Correct the rats x axis position if the pass the boundary
        :return:
        """
        if self.COORD_X + value > self.BOUNDARIES[0] - self.RAT_WIDTH:
            return (self.COORD_X + value) - (self.BOUNDARIES[0] - self.RAT_WIDTH)
        elif self.COORD_X + value < 0 < self.COORD_X:
            return (self.COORD_X + value) + self.RAT_WIDTH

        return 0

    def correct_y_position(self, value=0):
        """
        Correct the rats y axis position if the pass the boundary
        :return:
        """
        if self.COORD_Y + value > self.BOUNDARIES[1] - self.RAT_HEIGHT:
            return (self.COORD_Y + value) - (self.BOUNDARIES[0] - self.RAT_HEIGHT)
        elif self.COORD_Y + value < 0 < self.COORD_Y:
            return (self.COORD_Y + value) + self.RAT_HEIGHT

        return 0

    def draw_rat(self, py_game, game_display):
        """
        Draw the rat object on the screen
        :param py_game:
        :param game_display:
        :return:
        """
        py_game.draw.rect(game_display, self.COLOR, [self.COORD_X, self.COORD_Y, self.RAT_WIDTH, self.RAT_HEIGHT])

    def preform_update(self):
        pass
