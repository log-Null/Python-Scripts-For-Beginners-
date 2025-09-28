import os
import pygame
import calendar
import random
import sys

# --- Setup ---
os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()
WIDTH, HEIGHT = 900, 650
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dark Autumn Calendar")
CLOCK = pygame.time.Clock()

# --- Load Images ---
bg_image = pygame.image.load("assets/background.png").convert()
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

cat_image = pygame.image.load("assets/cat.png").convert_alpha()
cat_image = pygame.transform.scale(cat_image, (120, 70))

leaf_image = pygame.image.load("assets/leaf.png").convert_alpha()
leaf_image = pygame.transform.scale(leaf_image, (30, 30))

cloud_image = pygame.image.load("assets/cloud.png").convert_alpha()
cloud_image = pygame.transform.scale(cloud_image, (140, 70))

moon_image = pygame.image.load("assets/moon.png").convert_alpha()
moon_image = pygame.transform.scale(moon_image, (50, 50))

# --- Colors ---
TEXT_COLOR = (200, 150, 100)
BUTTON_HOVER_COLOR = (150, 60, 0)
HIGHLIGHT_COLOR = (70, 40, 30)

# --- Calendar Settings ---
current_year = 2025
current_month = 9
BUTTON_W, BUTTON_H = 80, 50
START_X, START_Y = 80, 150
buttons = []
leaves = []
cats = []
clouds = []
is_night = True  # default night mode
score = 0
font_score = pygame.font.SysFont("Courier", 28, bold=True)

# --- Calendar Functions ---
def create_calendar_buttons():
    global buttons
    buttons = []
    month_cal = calendar.monthcalendar(current_year, current_month)
    for row_idx, week in enumerate(month_cal):
        for col_idx, day in enumerate(week):
            if day == 0:
                continue
            x = START_X + col_idx*(BUTTON_W+10)
            y = START_Y + row_idx*(BUTTON_H+10)
            rect = pygame.Rect(x, y, BUTTON_W, BUTTON_H)
            buttons.append({"rect": rect, "day": day})

def draw_buttons():
    mx, my = pygame.mouse.get_pos()
    for btn in buttons:
        color_value = 40 if is_night else 70
        temp_surface = pygame.Surface((BUTTON_W,BUTTON_H))
        temp_surface.fill((color_value,color_value,color_value))
        SCREEN.blit(temp_surface, (btn["rect"].x, btn["rect"].y))
        if btn["rect"].collidepoint(mx, my):
            glow_surface = pygame.Surface((BUTTON_W+10,BUTTON_H+10))
            glow_surface.set_alpha(100)
            glow_surface.fill(BUTTON_HOVER_COLOR)
            SCREEN.blit(glow_surface, (btn["rect"].x-5, btn["rect"].y-5))
        font = pygame.font.SysFont("Courier", 22, bold=True)
        text_color = TEXT_COLOR if is_night else (255,200,100)
        text = font.render(str(btn["day"]), True, text_color)
        SCREEN.blit(text, (btn["rect"].x + BUTTON_W//2 - text.get_width()//2,
                           btn["rect"].y + BUTTON_H//2 - text.get_height()//2))

# --- Falling Leaves ---
def spawn_leaves(x, y):
    for _ in range(10):
        leaves.append({"x": x + random.randint(-20,20),
                       "y": y + random.randint(-20,20),
                       "speed": random.uniform(1,3),
                       "angle": random.uniform(0,360),
                       "rotation_speed": random.uniform(-3,3)})

def draw_leaves():
    for leaf in leaves:
        leaf["angle"] += leaf["rotation_speed"]
        rotated = pygame.transform.rotate(leaf_image, leaf["angle"])
        SCREEN.blit(rotated, (leaf["x"], leaf["y"]))
        leaf["y"] += leaf["speed"]
        leaf["x"] += random.choice([-0.5,0.5])
    leaves[:] = [l for l in leaves if l["y"] < HEIGHT]

# --- Cats ---
def init_cats():
    for _ in range(4):
        cats.append({"x": random.randint(0, WIDTH-120),
                     "y": HEIGHT-130,
                     "speed": random.uniform(0.8, 1.5),
                     "pause_timer": random.randint(0,120)})

def draw_cats():
    for cat in cats:
        if cat["pause_timer"] > 0:
            cat["pause_timer"] -= 1
        else:
            SCREEN.blit(cat_image, (cat["x"], cat["y"]))
            cat["x"] += cat["speed"]
            if cat["x"] > WIDTH:
                cat["x"] = -120
                cat["pause_timer"] = random.randint(60,180)

# --- Clouds ---
def init_clouds():
    for _ in range(3):
        clouds.append({"x": random.randint(0, WIDTH-140),
                       "y": random.randint(20, 120),
                       "speed": random.uniform(0.2, 0.6)})

def draw_clouds():
    for cloud in clouds:
        if is_night:
            dark_cloud = cloud_image.copy()
            dark_cloud.fill((60,60,80,0), special_flags=pygame.BLEND_RGBA_MULT)
            SCREEN.blit(dark_cloud, (cloud["x"], cloud["y"]))
        else:
            SCREEN.blit(cloud_image, (cloud["x"], cloud["y"]))
        cloud["x"] += cloud["speed"]
        if cloud["x"] > WIDTH:
            cloud["x"] = -140
            cloud["y"] = random.randint(20, 120)

# --- Background ---
def draw_background():
    if is_night:
        dark_bg = bg_image.copy()
        dark_bg.fill((50,30,40,50), special_flags=pygame.BLEND_RGBA_MULT)
        SCREEN.blit(dark_bg, (0,0))
    else:
        SCREEN.blit(bg_image, (0,0))

# --- Header ---
def draw_header():
    # Highlighted month rectangle
    rect_width, rect_height = 300, 60
    rect_x, rect_y = WIDTH//2 - rect_width//2, 20
    pygame.draw.rect(SCREEN, HIGHLIGHT_COLOR, (rect_x, rect_y, rect_width, rect_height), border_radius=12)
    font = pygame.font.SysFont("Courier", 36, bold=True)
    month_name = calendar.month_name[current_month]
    text = font.render(f"{month_name} {current_year}", True, TEXT_COLOR)
    SCREEN.blit(text, (WIDTH//2 - text.get_width()//2, rect_y + rect_height//2 - text.get_height()//2))
    # Prev/Next arrows
    pygame.draw.polygon(SCREEN, TEXT_COLOR, [(20,50),(50,35),(50,65)])
    pygame.draw.polygon(SCREEN, TEXT_COLOR, [(WIDTH-50,50),(WIDTH-20,35),(WIDTH-50,65)])

# --- Month Navigation ---
def next_month():
    global current_month, current_year
    current_month += 1
    if current_month > 12:
        current_month = 1
        current_year += 1
    create_calendar_buttons()

def prev_month():
    global current_month, current_year
    current_month -= 1
    if current_month < 1:
        current_month = 12
        current_year -= 1
    create_calendar_buttons()

# --- Initialize ---
create_calendar_buttons()
init_cats()
init_clouds()

# --- Main Loop ---
running = True
while running:
    CLOCK.tick(60)
    draw_background()
    draw_clouds()
    draw_cats()
    draw_leaves()
    draw_buttons()
    draw_header()

    # Draw score
    score_text = font_score.render(f"Score: {score}", True, (255, 220, 120))
    SCREEN.blit(score_text, (WIDTH - 150, 20))

    # Draw toggle icon (top-left)
    SCREEN.blit(moon_image, (10,10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx,my = event.pos
            # Click calendar buttons -> spawn leaves
            for btn in buttons:
                if btn["rect"].collidepoint(mx,my):
                    spawn_leaves(btn["rect"].x+BUTTON_W//2, btn["rect"].y+BUTTON_H//2)
            # Click leaves -> collect score
            for leaf in leaves[:]:
                leaf_rect = leaf_image.get_rect(topleft=(leaf["x"], leaf["y"]))
                if leaf_rect.collidepoint(mx,my):
                    leaves.remove(leaf)
                    score += 1
            # Toggle night/day
            if 10 < mx < 60 and 10 < my < 60:
                is_night = not is_night
            # Prev/Next month
            if 20 < mx < 50 and 35 < my < 65:
                prev_month()
            if WIDTH-50 < mx < WIDTH-20 and 35 < my < 65:
                next_month()

    pygame.display.flip()
