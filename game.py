import pygame
import random
from enum import Enum
from collections import namedtuple


pygame.init()
font = pygame.font.Font('arial.ttf', 20)

#to avoid typo errors and all
class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y')
BLOCK_SIZE = 20
SPEED = 10

WHITE = (255, 255, 255)
RED = (200, 0, 0)
PRIMARY = (0, 204, 0)
SECONDARY = (204, 204, 0)
BLACK = (0, 0, 0)

class SnakeGame:

    def __init__(self, w=640, h=480):

        self.w = w
        self.h = h

        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()

        # init game state
        self.direction = Direction.RIGHT

        self.head = Point(self.w / 2, self.h / 2)
        # creating init snake
        self.snake = [self.head,
                      Point(self.head.x - BLOCK_SIZE, self.head.y),
                      Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)]

        self.score = 0
        self.food = None
        self._place_food()

    def _place_food(self):
        x = random.randint(0, (self.w-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        y = random.randint(0, (self.h-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE

        self.food = Point(x,y)

        if self.food in self.snake:
            self._place_food()


    def play_step(self):

        # take user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN

        # move snake
        self.move(self.direction)
        self.snake.insert(0, self.head)

        # check for game over
        game_over = False
        if self._is_collision():
            game_over = True
            return game_over, self.score

        # place new food or move
        if self.head == self.food:
            self.score += 1
            self._place_food()
        else:
            self.snake.pop()

        # update ui
        self._update_ui()
        self.clock.tick(SPEED)

        #return score and game status
        return game_over, self.score

    def move(self, direction):
        x = self.head.x
        y = self.head.y

        if direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif direction == Direction.UP:
            y -= BLOCK_SIZE
        elif direction == Direction.DOWN:
            y += BLOCK_SIZE

        self.head = Point(x,y)

    def _is_collision(self):

        # hits the border
        if self.head.x > self.w - BLOCK_SIZE or self.head.x < 0 or self.head.y > self.h-BLOCK_SIZE or self.head.y < 0:
            return True
        # hits body
        if self.head in self.snake[1:]:
            return True
        return False


    def _update_ui(self):
        self.display.fill(BLACK)

        for pt in self.snake:
            pygame.draw.rect(self. display, PRIMARY, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, SECONDARY, pygame.Rect(pt.x+4, pt.y+4, 12, 12), 0, 10)
            pygame.draw.rect(self.display, PRIMARY, pygame.Rect(pt.x+8, pt.y+8, 5, 5), 0, 10)


        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE), 0, 10)

        text = font.render("Score : "+str(self.score), True, WHITE)
        self.display.blit(text, [0,0])
        pygame.display.flip()








if __name__ == '__main__':
    game = SnakeGame()

    #game loop
    while True:
        is_game_over, score = game.play_step()

        #break if game over
        if is_game_over == True:
            break

    print(f'Final Score : {score}')



    pygame.quit()
