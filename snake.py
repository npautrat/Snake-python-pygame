import subprocess
import sys
import os

try:
    import pygame
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
    import pygame

import random

pygame.init()
WIDTH, HEIGHT = 300, 300
pygame.display.set_caption("Jeu Snake ")

v = {
    # Variables principales
    "screen": pygame.display.set_mode((600, 600)),
    "pomme": pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Pomme 1.png')), (20, 20)),
    "compteur_pomme": 0,
    "compteur_pomme2": 0,
    "compteur_pomme_a": 1,
    "running": True,
    "x": 310,
    "y": 310,
    "pommeco": [(random.randint(0, 14) * 20 + 150, random.randint(0, 14) * 20 + 150)],
    "clock": pygame.time.Clock(),
    "x_random": random.randint(0, 14) * 20 + 150,
    "y_random": random.randint(0, 14) * 20 + 150,
    "debut_line_y": 150,
    "debut_line_x": 150,
    "xspeed": 20,
    "yspeed": 0,
    "block_size": 20,
    "snake_segments": [(310, 310)],
    "attendpress": True,
    "debut": True,
    # Couleurs
    "WHITE": (255, 255, 255),
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "GRAY": (200, 200, 200),
    "BLACK": (0, 0, 0),
    "BEIGE": (245, 245, 220),
    "BROWN": (222, 184, 135),
}

v["text"] = pygame.font.Font(None, 36).render(f'Score : {v["compteur_pomme"]}', True, (0, 0, 0))
keys = pygame.key.get_pressed()

def draw_line():
    for ydl in range(v["debut_line_y"], v["debut_line_y"] + HEIGHT + 1, v["block_size"]):
        pygame.draw.line(v["screen"], v["GRAY"], (v["debut_line_x"], ydl), (v["debut_line_x"] + WIDTH, ydl))

    for xdl in range(v["debut_line_x"], v["debut_line_x"] + WIDTH + 1, v["block_size"]):
        pygame.draw.line(v["screen"], v["GRAY"], (xdl, v["debut_line_y"]), (xdl, v["debut_line_y"] + HEIGHT))

def color_block():
    for ycb in range(v["debut_line_y"], v["debut_line_y"] + HEIGHT, v["block_size"]):
        for xcb in range(v["debut_line_x"], v["debut_line_x"] + WIDTH, v["block_size"]):
            if (xcb // v["block_size"] + ycb // v["block_size"]) % 2 == 0:
                color = v["BROWN"]
            else:
                color = v["BEIGE"]
            pygame.draw.rect(v["screen"], color, (xcb, ycb, v["block_size"], v["block_size"]))

def mouv_press():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and v["debut"]:
        v["xspeed"] = -v["block_size"]
        v["yspeed"] = 0
        v["debut"] = False
    if keys[pygame.K_RIGHT] and v["debut"]:
        v["xspeed"] = v["block_size"]
        v["yspeed"] = 0
        v["debut"] = False
    if keys[pygame.K_UP] and v["debut"]:
        v["xspeed"] = 0
        v["yspeed"] = -v["block_size"]
        v["debut"] = False
    if keys[pygame.K_DOWN] and v["debut"]:
        v["xspeed"] = 0
        v["yspeed"] = v["block_size"]
        v["debut"] = False

    if keys[pygame.K_LEFT] and v["xspeed"] == 0:
        v["xspeed"] = -v["block_size"]
        v["yspeed"] = 0
    if keys[pygame.K_RIGHT] and v["xspeed"] == 0:
        v["xspeed"] = v["block_size"]
        v["yspeed"] = 0
    if keys[pygame.K_UP] and v["yspeed"] == 0:
        v["xspeed"] = 0
        v["yspeed"] = -v["block_size"]
    if keys[pygame.K_DOWN] and v["yspeed"] == 0:
        v["xspeed"] = 0
        v["yspeed"] = v["block_size"]
    if keys[pygame.K_ESCAPE]:
        v["running"] = False

def collis():
    global v
    block_snake = pygame.Rect(v["x"], v["y"], v["block_size"], v["block_size"])
    block_rouge = pygame.Rect(v["x_random"], v["y_random"], v["block_size"], v["block_size"])

    if v["x"] < v["debut_line_x"] or v["x"] >= WIDTH + v["debut_line_x"] or \
        v["y"] < v["debut_line_y"] or v["y"] >= HEIGHT + v["debut_line_y"]:
        v["running"] = False

    if block_snake.colliderect(block_rouge):
        v["compteur_pomme"] += 1
        v["compteur_pomme2"] += 1
        v["text"] = pygame.font.Font(None, 36).render(f'Score : {v["compteur_pomme"]}', True, (0, 0, 0))
        while True:
            v["x_random"] = random.randint(0, 14) * 20 + 150
            v["y_random"] = random.randint(0, 14) * 20 + 150
            if (v["x_random"], v["y_random"]) not in v["snake_segments"]:
                break

def maj_snake():
    nouvelle_tete = (v["x"], v["y"])
    v["snake_segments"].insert(0, nouvelle_tete)

    if v["compteur_pomme2"] > 0:
        v["compteur_pomme2"] -= 1
    else:
        v["snake_segments"].pop()

    if nouvelle_tete in v["snake_segments"][1:]:
        v["running"] = False

    for seg in v["snake_segments"]:
        pygame.draw.rect(v["screen"], v["GREEN"], (*seg, v["block_size"], v["block_size"]))

def plein_de_pomme():
    pomme_random = (v["x_random"], v["y_random"])
    v["pommeco"].insert(0, pomme_random)

    if v["compteur_pomme_a"] > 0:
        v["compteur_pomme_a"] -= 1
    else:
        v["pommeco"].pop()

    for segpomme in v["pommeco"]:
        v["screen"].blit(v["pomme"], segpomme)

while v["running"]:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            v["running"] = False
    v["screen"].fill(v["WHITE"])
    v["text_rect"] = v["text"].get_rect(center=(70, 20))
    v["screen"].blit(v["text"], v["text_rect"])
    color_block()
    maj_snake()
    draw_line()
    mouv_press()
    collis()
    plein_de_pomme()

    if not v["debut"]:
        v["x"] += v["xspeed"]
        v["y"] += v["yspeed"]

    if v["compteur_pomme"] == 224:
        v["running"] = False

    pygame.display.flip()
    v["clock"].tick(10)

print('Petitestereggcarjenestmarredecodera1heuredumatinlejourdelancarjaipasdeviedoncvasyprofitezbiendelapresentationiguesscarlajesuischezmesgrandsparents')
pygame.quit()
sys.exit()