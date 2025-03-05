import requests
import pygame
from PIL import Image
from io import BytesIO
pygame.init()
screen = pygame.display.set_mode([1920,1080])
clock = pygame.time.Clock()
game_run = True
while game_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            url = "http://"+ {open("ip.txt").read().replace("/n","")} +"/click"
            r = requests.post(url)

    url = "http://" + {open("ip.txt").read().replace("/n", "")} + "/move"
    r = requests.post(url,json={"x":pygame.mouse.get_pos()[0],"y":pygame.mouse.get_pos()[1]})
    keys = pygame.key.get_pressed()

    pressed_keys = [pygame.key.name(i) for i in range(len(keys)) if keys[i]]  # Get names of pressed keys

    print(pressed_keys)

    # Send pressed keys to the server

    if pressed_keys:  # Only send if there are pressed keys
        url = "http://" + {open("ip.txt").read().replace("/n", "")} + "/keys"
        r = requests.post(f"http://{open("ip.txt").read().replace("/n","")}:5000/keys", json={"keys": pressed_keys})

    url = "http://" + {open("ip.txt").read().replace("/n", "")} + "/screenshot"
    r = requests.post(url)
    Image.open(BytesIO(r.content)).save("screenshot.png")
    screen.blit(pygame.image.load("screenshot.png").convert_alpha(), (0,0))
    pygame.display.flip()
    clock.tick(15)

