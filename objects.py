from pygame.draw import circle


#class created in order to change the color of the points dinamicaly respect the closest centroid and his color
class Ball:

    def __init__(self,ball_type,screen,position,radius,color,factor) -> None:

        self.ball_type = ball_type
        self.screen = screen
        self.position = position
        self.radius = radius
        self.color = color
        self.factor = factor

    def draw_ball(self) -> None:

        return circle(self.screen, self.color, self.position * self.factor, self.radius)