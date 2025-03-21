import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Non-Overlapping Rectangles with Spacing")

# Clock
fps = pygame.time.Clock()

# Store rectangles
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

running = True
while running:
    screen.fill((255,255,255))  # Clear screen

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check if 5 seconds (5000 milliseconds) have passed
    if pygame.time.get_ticks() - spawn_time > 25:
        max_attempts = 100  # Prevent infinite loops
        for _ in range(max_attempts):
            x = random.randint(0, WIDTH - RECT_WIDTH)  
            y = random.randint(0, HEIGHT - RECT_HEIGHT)  
            new_rect = pygame.Rect(x, y, RECT_WIDTH, RECT_HEIGHT)

            if not is_too_close(new_rect, rectangles, SPACING):
                rectangles.append((x, y, RECT_WIDTH, RECT_HEIGHT))  # Store new rectangle
                spawn_time = pygame.time.get_ticks()  # Reset timer
                break  # Exit loop once a valid position is found

    # Draw all rectangles
    for rect in rectangles:
        pygame.draw.rect(screen, (255, 0, 0), rect)

    pygame.display.update()  # Refresh screen
    fps.tick(60)  # Limit FPS

pygame.quit()
