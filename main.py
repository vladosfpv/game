from Player import *
from Rocket import *
from Functions import *

connection = sqlite3.connect("db.db")
cursor = connection.cursor()

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("game")
clock = pygame.time.Clock()
score = 0
create_db()


def start_the_game():
    rockets = pygame.sprite.Group()
    player = Player()
    name = t_input.get_value()
    add_player(name)

    global score
    running = True
    alive = True
    left = False
    right = False
    up = False
    down = False

    time1_score = time.time()
    time1 = time.time()
    while running:
        time_score = time.time() - time1_score
        if (time.time() - time1) >= 1:
            random_number = random.randint(1, 4)
            if random_number == 1:
                rocket = Rocket(random.randint(0, WIDTH), 0)
            elif random_number == 2:
                rocket = Rocket(0, random.randint(0, HEIGHT))
            elif random_number == 3:
                rocket = Rocket(WIDTH, random.randint(0, HEIGHT))
            elif random_number == 4:
                rocket = Rocket(random.randint(0, WIDTH), HEIGHT)
            rockets.add(rocket)
            time1 = time.time()
        # Держим цикл на правильной скорости
        clock.tick(FPS)

        # Обработчик событий
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                left = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                right = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                up = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                down = True
            if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                left = False
            if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                right = False
            if event.type == pygame.KEYUP and event.key == pygame.K_UP:
                up = False
            if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                down = False

        # Обновление
        player.update(left, right, up, down)

        # Проверка коллизии
        if pygame.sprite.spritecollideany(player, rockets):
            player.kill()
            alive = False
            score = int(time_score * 100)
            set_score(name, score)
            top_players = get_top_users()
            # for top_player in top_players:
            #     label = menu.add.label(f"{top_player[0]} : {top_player[1]}")
            #     table.add_row(label)
            if len(top_players) == 1:
                label1.set_title(f"{top_players[0][0]} : {top_players[0][1]}")
            elif len(top_players) == 2:
                label1.set_title(f"{top_players[0][0]} : {top_players[0][1]}")
                label2.set_title(f"{top_players[1][0]} : {top_players[1][1]}")
            elif len(top_players) == 3:
                label1.set_title(f"{top_players[0][0]} : {top_players[0][1]}")
                label2.set_title(f"{top_players[1][0]} : {top_players[1][1]}")
                label3.set_title(f"{top_players[2][0]} : {top_players[2][1]}")
            elif len(top_players) == 4:
                label1.set_title(f"{top_players[0][0]} : {top_players[0][1]}")
                label2.set_title(f"{top_players[1][0]} : {top_players[1][1]}")
                label3.set_title(f"{top_players[2][0]} : {top_players[2][1]}")
                label4.set_title(f"{top_players[3][0]} : {top_players[3][1]}")
            elif len(top_players) == 5:
                label1.set_title(f"{top_players[0][0]} : {top_players[0][1]}")
                label2.set_title(f"{top_players[1][0]} : {top_players[1][1]}")
                label3.set_title(f"{top_players[2][0]} : {top_players[2][1]}")
                label4.set_title(f"{top_players[3][0]} : {top_players[3][1]}")
                label5.set_title(f"{top_players[4][0]} : {top_players[4][1]}")

        # Рендеринг
        screen.fill(BLACK)
        if alive:
            player.draw(screen)
        else:
            break
        rockets.update(player.rect.x, player.rect.y)
        rockets.draw(screen)
        draw_text(screen, f"Time: {int(time_score)}", 20, 50, 15)

        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()


menu = pygame_menu.Menu('Welcome', 800, 600, theme=pygame_menu.themes.THEME_DEFAULT)
top_players = get_top_users()
lbl = menu.add.label("Your task is to avoid asteroids, don't let them kill you!")
lbl.resize(WIDTH - 400, 35)
top_lbl = menu.add.label("Top 5:")
top_lbl.resize(WIDTH - 750, 30)
table = menu.add.table()

# for top_player in top_players:
#     label = menu.add.label(f"{top_player[0]} : {top_player[1]}")
#     table.add_row(label)
label1 = menu.add.label("1st place")
label2 = menu.add.label("2nd place")
label3 = menu.add.label("3rd place")
label4 = menu.add.label("4th place")
label5 = menu.add.label("5th place")
table.add_row(label1)
table.add_row(label2)
table.add_row(label3)
table.add_row(label4)
table.add_row(label5)
if len(top_players) == 1:
    label1.set_title(f"{top_players[0][0]} : {top_players[0][1]}")
elif len(top_players) == 2:
    label1.set_title(f"{top_players[0][0]} : {top_players[0][1]}")
    label2.set_title(f"{top_players[1][0]} : {top_players[1][1]}")
elif len(top_players) == 3:
    label1.set_title(f"{top_players[0][0]} : {top_players[0][1]}")
    label2.set_title(f"{top_players[1][0]} : {top_players[1][1]}")
    label3.set_title(f"{top_players[2][0]} : {top_players[2][1]}")
elif len(top_players) == 4:
    label1.set_title(f"{top_players[0][0]} : {top_players[0][1]}")
    label2.set_title(f"{top_players[1][0]} : {top_players[1][1]}")
    label3.set_title(f"{top_players[2][0]} : {top_players[2][1]}")
    label4.set_title(f"{top_players[3][0]} : {top_players[3][1]}")
elif len(top_players) == 5:
    label1.set_title(f"{top_players[0][0]} : {top_players[0][1]}")
    label2.set_title(f"{top_players[1][0]} : {top_players[1][1]}")
    label3.set_title(f"{top_players[2][0]} : {top_players[2][1]}")
    label4.set_title(f"{top_players[3][0]} : {top_players[3][1]}")
    label5.set_title(f"{top_players[4][0]} : {top_players[4][1]}")

t_input = menu.add.text_input('Name :', default='Player')
img = menu.add.image("images/rrr.png")
img.resize(120, 90)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)
