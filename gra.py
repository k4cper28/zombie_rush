from klas import *

# ekran gry
window = pygame.display.set_mode((1280, 780))


# funkcja główna
def main():
    dzialanie = True
    player = Player()
    pocisk = Pocisk()
    zombies = []
    clock = 0
    score = 0
    czas_respawnu = 2
    mapa = pygame.image.load("mapa.png")
    naboj_img = pygame.image.load("nabój.png")
    game_over = pygame.image.load("game_over.png")
    while dzialanie:
        clock += pygame.time.Clock().tick(360) * 8 / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dzialanie = False

        keys = pygame.key.get_pressed()

        if clock >= czas_respawnu:
            clock = 0
            zombies.append(Zombie())
            if czas_respawnu >= 0.5:
                czas_respawnu -= 0.01

        player.tick(keys)

        pocisk.tick(keys)

        for zombie in zombies:
            zombie.tick()
            if zombie.x_cord <= 300:
                player.hp -= 1
                zombies.remove(zombie)

        for zombie in zombies:
            if zombie.hitbox.colliderect(pocisk.hitbox):
                zombies.remove(zombie)
                pocisk.x_cord = -100
                pocisk.y_cord = -100
                pocisk.state = "ready"
                score += 1

        window.blit(mapa, (0, 0))

        if pocisk.state == "fire":
            pocisk.x_cord = pocisk.x_cord + pocisk.speed
            pocisk.draw(pocisk.x_cord, pocisk.y_cord, naboj_img)
            if pocisk.x_cord > 1280:
                pocisk.state = "ready"
        else:
            pocisk.x_cord = player.x_cord + 10
            pocisk.y_cord = player.y_cord + 60

        player.draw()

        score_img = pygame.font.Font.render(pygame.font.SysFont("arial", 48), "wynik: " + str(score), True, (0, 0, 0))
        window.blit(score_img, (30, 5))

        for zombie in zombies:
            zombie.draw()

        if player.hp == 0:
            window.blit(game_over, (0, 0))
            window.blit(score_img, (525, 340))
            pygame.display.update()
            time.sleep(7)
            player.hp = 3
            dzialanie = False
            menu()
        pygame.display.update()


def menu():
    dzialanie = True
    background = pygame.image.load("menu.png")
    play_button = Button(525, 340)
    while dzialanie:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dzialanie = False

        if play_button.tick():
            dzialanie = False
            main()

        window.blit(background, (0, 0))
        play_button.draw(window)

        pygame.display.update()


# inicjowanie funkcji głównej
if __name__ == "__main__":
    menu()
