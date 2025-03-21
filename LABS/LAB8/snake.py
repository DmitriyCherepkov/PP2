import pygame
import time
import random

snake_speed = 15

# Window size
window_x, window_y = 720, 480

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Snake game')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]

fruit_spawn = True

# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction

# initial score
score = 0

rectangles = []
spawn_time = pygame.time.get_ticks()  # Track time
RECT_WIDTH, RECT_HEIGHT = 20, 30  # Rectangle size
SPACING = 50  # Minimum spacing between rectangles

def is_too_close(new_rect, rect_list, spacing):
    """Check if new rectangle is too close to existing ones."""
    for rect in rect_list:
        existing_rect = pygame.Rect(rect)
        if (abs(existing_rect.x - new_rect.x) < RECT_WIDTH + spacing and 
            abs(existing_rect.y - new_rect.y) < RECT_HEIGHT + spacing):
            return True  # Too close
    return False  # Good position

# displaying Score function
def show_score(choice, color, font, size):
  
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
    
    # create the display surface object 
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
    
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
    
    # displaying text
    game_window.blit(score_surface, score_rect)

# game over function
def game_over():
  
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)
    
    # creating a text surface on which text 
    # will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
    
    # create a rectangular object for the text 
    # surface object
    game_over_rect = game_over_surface.get_rect()
    
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
    
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
    # after 1 second we will quit the program
    time.sleep(1)
    
    # deactivating pygame library
    pygame.quit()
    
    # quit the program
    quit()

# Main Function
while True:            
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # If two keys pressed simultaneously
    # we don't want snake to move into two 
    # directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        
        # increasing the snake speed when a fruit is eaten
        snake_speed += 0.5
        fruit_spawn = False
    else:
        snake_body.pop()
        
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                          random.randrange(1, (window_y//10)) * 10]
        
    fruit_spawn = True
    game_window.fill(black)

    # Spawn rectangle every 10 second (10000 ms)
    if pygame.time.get_ticks() - spawn_time > 1000:
        max_attempts = 100  # Prevent infinite loops
        for _ in range(max_attempts):
            x = random.randint(0, window_x - RECT_WIDTH)  
            y = random.randint(0, window_y - RECT_HEIGHT)  
            new_rect = pygame.Rect(x, y, RECT_WIDTH, RECT_HEIGHT)

            if not is_too_close(new_rect, rectangles, SPACING):
                rectangles.append((x, y, RECT_WIDTH, RECT_HEIGHT))  # Store new rectangle
                spawn_time = pygame.time.get_ticks()  # Reset timer ONLY after success
                break  # Exit loop once a valid position is found

    # Draw all rectangles **AFTER clearing the screen**
    for rect in rectangles:
        pygame.draw.rect(game_window, red, rect)

    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
    
    # Check collision with obstacles (rectangles)
    for rect in rectangles:
        obstacle = pygame.Rect(rect)  # Convert stored tuple to pygame.Rect
        snake_head = pygame.Rect(snake_position[0], snake_position[1], 10, 10)  # Snake head as a rectangle

        if snake_head.colliderect(obstacle):  # Collision detection
            game_over()
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # displaying score continuously
    show_score(1, white, 'times new roman', 20)

    pygame.display.update()
    fps.tick(snake_speed)



