import pygame
import time
import random
import psycopg2
import json

# Initialize pygame
pygame.init()

snake_speed = 15
window_x, window_y = 720, 480

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

font = pygame.font.SysFont("arial", 30)
eat_sound = pygame.mixer.Sound("crash.wav")  # Your sound file path

pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()

snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]
fruit_spawn = True
random_size_x = random.randint(10, 25)
random_size_y = random.randint(10, 25)

direction = 'RIGHT'
change_to = direction
score = 0

rectangles = []
spawn_time = pygame.time.get_ticks()
RECT_WIDTH, RECT_HEIGHT = 20, 30
SPACING = 50

# DB credentials
host = "localhost"
port = "5432"
dbname = "saved_games"
user = "postgres"
password = "1"

def add_scores_to_the_table(username, score):
    try:
        with psycopg2.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT score FROM scores WHERE username = %s
                """, (username,))
                result = cursor.fetchone()

                if result:
                    old_score = result[0]
                    if score > old_score:
                        cursor.execute("""
                            UPDATE scores SET score = %s WHERE username = %s
                        """, (score, username))
                        print("High score updated!")
                else:
                    cursor.execute("""
                        INSERT INTO scores (username, score) VALUES (%s, %s)
                    """, (username, score))
                    print("New user score saved.")

                connection.commit()

    except psycopg2.Error as error:
        print(f"Database error: {error}")
    except Exception as error:
        print(f"Unexpected error: {error}")

def save_game_state(username, score, snake_position, snake_body, direction):
    try:
        with psycopg2.connect(
            host=host, port=port, dbname=dbname, user=user, password=password
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO saved_games (username, score, snake_position_x, snake_position_y, snake_body, direction)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (username) DO UPDATE SET
                        score = EXCLUDED.score,
                        snake_position_x = EXCLUDED.snake_position_x,
                        snake_position_y = EXCLUDED.snake_position_y,
                        snake_body = EXCLUDED.snake_body,
                        direction = EXCLUDED.direction;
                """, (username, score, snake_position[0], snake_position[1],
                      json.dumps(snake_body), direction))
                connection.commit()
                print("Game state saved!")
    except Exception as e:
        print("Error saving game state:", e)

def load_saved_game(username):
    try:
        with psycopg2.connect(
            host=host, port=port, dbname=dbname, user=user, password=password
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT score, snake_position_x, snake_position_y, snake_body, direction FROM saved_games WHERE username = %s", (username,))
                result = cursor.fetchone()
                if result:
                    score = result[0]
                    snake_position = [result[1], result[2]]
                    try:
                        snake_body = json.loads(result[3])  # This will try to decode the snake_body data
                    except (json.JSONDecodeError, TypeError) as e:
                        print(f"Error decoding snake_body data for {username}, returning default body. Error: {e}")
                        snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]  # Fallback to default snake body
                    direction = result[4]
                    return score, snake_position, snake_body, direction
    except Exception as e:
        print("Error loading saved game:", e)
    return 0, [100, 50], [[100, 50], [90, 50], [80, 50]], 'RIGHT'  # default fallback

def is_fruit_too_close(fruit_pos, fruit_width, fruit_height, rectangles, spacing):
    for rect in rectangles:
        obstacle = pygame.Rect(rect)
        fruit_rect = pygame.Rect(fruit_pos[0], fruit_pos[1], fruit_width, fruit_height)
        if fruit_rect.colliderect(obstacle):
            return True
    return False

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    username_surface = score_font.render('Username : ' + str(username), True, color)
    game_window.blit(score_surface, (10, 10))
    game_window.blit(username_surface, (10, 40))

def pause_game():
    paused = True
    pause_font = pygame.font.SysFont("arial", 50)
    pause_text = pause_font.render("Game Paused. Press 'P' to resume.", True, white)
    while paused:
        game_window.blit(pause_text, (window_x // 6, window_y // 3))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False

def game_over(username, score):
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(1)
    add_scores_to_the_table(username, score)
    pygame.quit()
    quit()

# Username input
game_started = False
username = ""

while not game_started:
    game_window.fill((0, 0, 0))
    prompt_text = font.render("Enter your name to start: ", True, white)
    username_text = font.render("Username: " + username, True, white)
    game_window.blit(prompt_text, (window_x // 4, window_y // 3))
    game_window.blit(username_text, (window_x // 4, window_y // 2))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and username:
                game_started = True
            elif event.key == pygame.K_BACKSPACE:
                username = username[:-1]
            else:
                username += event.unicode

# Load saved state if available
score, snake_position, snake_body, direction = load_saved_game(username)
change_to = direction

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: change_to = 'UP'
            if event.key == pygame.K_DOWN: change_to = 'DOWN'
            if event.key == pygame.K_LEFT: change_to = 'LEFT'
            if event.key == pygame.K_RIGHT: change_to = 'RIGHT'
            if event.key == pygame.K_p:
                pause_game()
            if event.key == pygame.K_ESCAPE:
                save_game_state(username, score, snake_position, snake_body, direction)
                print("Game saved and exiting...")
                pygame.quit()
                quit()
                
    if change_to == 'UP' and direction != 'DOWN': direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP': direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT': direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT': direction = 'RIGHT'

    if direction == 'UP': snake_position[1] -= 10
    if direction == 'DOWN': snake_position[1] += 10
    if direction == 'LEFT': snake_position[0] -= 10
    if direction == 'RIGHT': snake_position[0] += 10

    snake_body.insert(0, list(snake_position))

    # Use only collision-based logic for fruit
    fruit_rect = pygame.Rect(fruit_position[0], fruit_position[1], random_size_x, random_size_y)
    snake_head = pygame.Rect(snake_position[0], snake_position[1], 10, 10)

    if snake_head.colliderect(fruit_rect):
        pygame.mixer.Sound.play(eat_sound)
        snake_speed += float((random_size_x + random_size_y) * 0.02)
        score += int((random_size_x + random_size_y) * 0.8)
        fruit_spawn = False
        random_size_x = random.randint(10, 25)
        random_size_y = random.randint(10, 25)
    else:
        snake_body.pop()

    if not fruit_spawn:
        for _ in range(100):
            fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                              random.randrange(1, (window_y // 10)) * 10]
            if not is_fruit_too_close(fruit_position, random_size_x, random_size_y, rectangles, SPACING):
                fruit_spawn = True
                break

    game_window.fill(black)

    for rect in rectangles:
        pygame.draw.rect(game_window, red, pygame.Rect(rect[0], rect[1], RECT_WIDTH, RECT_HEIGHT))

    for pos in snake_body[1:]:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], random_size_x, random_size_y))

    # Game over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over(username, score)
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over(username, score)

    for rect in rectangles:
        if snake_head.colliderect(pygame.Rect(rect[0], rect[1], RECT_WIDTH, RECT_HEIGHT)):
            game_over(username, score)

    if snake_position in snake_body[1:]:
        game_over(username, score)

    show_score(1, white, 'times new roman', 20)
    pygame.display.update()
    fps.tick(snake_speed)