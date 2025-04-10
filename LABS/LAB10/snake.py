import pygame
import time
import random

# Initializing pygame
pygame.init()

snake_speed = 15
# Window size
window_x, window_y = 720, 480

# Defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initializing font after pygame.init()
font = pygame.font.SysFont("arial", 30)

# Sound initialization
eat_sound = pygame.mixer.Sound("crash.wav")  # Replace with your sound file path

# Initializing game window
pygame.display.set_caption('Snake game')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# Defining snake default position
snake_position = [100, 50]

# Defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# Fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]

fruit_spawn = True
random_size_x = random.randint(10, 25)
random_size_y = random.randint(10, 25)

# Setting default snake direction towards right
direction = 'RIGHT'
change_to = direction

# Initial score
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

def is_fruit_too_close(fruit_pos, fruit_width, fruit_height, rectangles, spacing):
    """Check if the fruit is too close to any rectangle."""
    for rect in rectangles:
        obstacle = pygame.Rect(rect)
        fruit_rect = pygame.Rect(fruit_pos[0], fruit_pos[1], fruit_width, fruit_height)
        if fruit_rect.colliderect(obstacle):
            return True  # Fruit is too close to an obstacle
    return False  # Fruit is not too close

# Displaying Score function
def show_score(choice, color, font, size):
    # Creating font object score_font
    score_font = pygame.font.SysFont(font, size)
    
    # Create the display surface object score_surface for score
    score_surface = score_font.render('Score : ' + str(score), True, color)
    # Create the display surface object username_surface for username
    username_surface = score_font.render('Username : ' + str(username), True, color)
    
    # Create a rectangular object for the text surface object
    score_rect = score_surface.get_rect()
    username_rect = username_surface.get_rect()

    # Set positions for the text elements
    score_rect.topleft = (10, 10)  # Position the score in the top-left corner
    username_rect.topleft = (10, 40)  # Position the username below the score

    # Displaying text on the screen
    game_window.blit(score_surface, score_rect)
    game_window.blit(username_surface, username_rect)

# Game over function
def game_over():
    # Creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)
    
    # Creating a text surface on which text will be drawn
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    
    # Create a rectangular object for the text surface object
    game_over_rect = game_over_surface.get_rect()
    
    # Setting position of the text
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    
    # Blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
    # After 1 second we will quit the program
    time.sleep(1)
    
    # Deactivating pygame library
    pygame.quit()
    
    # Quit the program
    quit()

# Start of game (username input)
game_started = False
username = ""  # Variable to store username

while not game_started:
    game_window.fill((0, 0, 0))  # Clear screen

    # "Enter your name" prompt
    prompt_text = font.render("Enter your name to start: ", True, (255, 255, 255))
    game_window.blit(prompt_text, (window_x // 4, window_y // 3))

    # Display username
    username_text = font.render("Username: " + username, True, (255, 255, 255))
    game_window.blit(username_text, (window_x // 4, window_y // 2))

    # Update screen
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # If Enter is pressed, start the game
                if username:  # If username is not empty
                    game_started = True
                break
            elif event.key == pygame.K_BACKSPACE:
                # If Backspace is pressed, remove the last character
                username = username[:-1]
            else:
                # Add character to username
                username += event.unicode

# Main game loop (with fruit spawning logic update)
while True:
    # Управление клавишами
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

    # Обновление позиции змейки
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Передвижение змейки
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Механизм роста тела змейки
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        pygame.mixer.Sound.play(eat_sound)
        snake_speed += 0.5
        score += int((random_size_x + random_size_y) * 0.8)  # Учитываем размер яблока при подсчете очков
        fruit_spawn = False
        random_size_x = random.randint(10, 25)  # Новый случайный размер для яблока
        random_size_y = random.randint(10, 25)

    else:
        snake_body.pop()

    if not fruit_spawn:
        # Попытка найти валидное место для появления яблока
        max_attempts = 100  # Макс. количество попыток
        for _ in range(max_attempts):
            # Генерация новой позиции для яблока
            fruit_position = [random.randrange(1, (window_x // 10)) * 10, 
                              random.randrange(1, (window_y // 10)) * 10]

            # Проверка на близость яблока к блокам
            if not is_fruit_too_close(fruit_position, random_size_x, random_size_y, rectangles, SPACING):
                fruit_spawn = True  # Яблоко может появиться
                break  # Завершаем цикл после нахождения валидной позиции

    game_window.fill(black)

    # Отрисовка всех блоков
    for rect in rectangles:
        pygame.draw.rect(game_window, red, pygame.Rect(rect[0], rect[1], RECT_WIDTH, RECT_HEIGHT))

    # Отрисовка змейки
    for pos in snake_body[1:]:  # Пропускаем голову
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # Отрисовка яблока с случайным размером
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], random_size_x, random_size_y))

    # Условия для завершения игры
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    # Проверка на коллизию с блоками
    for rect in rectangles:
        obstacle = pygame.Rect(rect)
        snake_head = pygame.Rect(snake_position[0], snake_position[1], 10, 10)

        if snake_head.colliderect(obstacle):  # Проверка на столкновение с блоками
            game_over()

    # Проверка на столкновение с собственным телом
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # Проверка на коллизию с яблоком (с учетом его размера)
    fruit_rect = pygame.Rect(fruit_position[0], fruit_position[1], random_size_x, random_size_y)
    snake_head = pygame.Rect(snake_position[0], snake_position[1], 10, 10)

    if snake_head.colliderect(fruit_rect):  # Если голова змеи столкнулась с яблоком
        pygame.mixer.Sound.play(eat_sound)
        snake_speed += 0.5
        score += int((random_size_x + random_size_y) * 0.8)  # Учитываем размер яблока при подсчете очков
        fruit_spawn = False
        random_size_x = random.randint(10, 25)
        random_size_y = random.randint(10, 25)

    # Отображение счета
    show_score(1, white, 'times new roman', 20)

    pygame.display.update()
    fps.tick(snake_speed)