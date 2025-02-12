import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH = 360
HEIGHT = 640

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Космическая стрелялка")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Частота обновления экрана
clock = pygame.time.Clock()
FPS = 60

# Загрузка изображений
player_image = pygame.image.load("player.png").convert_alpha()  # Изображение корабля игрока
bullet_image = pygame.image.load("bullet.png").convert_alpha()  # Изображение пули
asteroid_image = pygame.image.load("asteroid.png").convert_alpha()  # Изображение астероида
enemy_ship_image = pygame.image.load("ship.png").convert_alpha()  # Изображение корабля неприятеля

player_image = pygame.transform.scale(player_image, (50, 50))  # Изменение размера корабля
bullet_image = pygame.transform.scale(bullet_image, (10, 20))  # Изменение размера пули
asteroid_image = pygame.transform.scale(asteroid_image, (40, 40))  # Изменение размера астероида
enemy_ship_image = pygame.transform.scale(enemy_ship_image, (50, 50))

# Флаг завершения игры и таймер
game_over = False
game_over_timer = 0


# Классы
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image  # Используем загруженное изображение
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed = 5

    def update(self):
        # Управление мышью
        mouse_x, _ = pygame.mouse.get_pos()
        self.rect.centerx = mouse_x

        # Ограничение движения в пределах экрана
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_image  # Используем загруженное изображение
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:  # Удаление снаряда за пределами экрана
            self.kill()


class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = asteroid_image  # Используем загруженное изображение
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(2, 5)  # Случайная скорость астероида

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:  # Удаление астероида за пределами экрана
            self.kill()


class EnemyShip(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_ship_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(2, 4)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()

    def shoot(self):
        if random.random() < 0.01:  # Вероятность стрельбы
            bullet = Bullet(self.rect.centerx, self.rect.bottom)
            bullet.speed = 5  # Пули движутся вниз
            all_sprites.add(bullet)
            enemy_bullets.add(bullet)



# Группы спрайтов
all_sprites = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemy_ships = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()

# Создание игрока
player = Player()
all_sprites.add(player)

# Создание астероидов
def create_asteroid():
    asteroid = Asteroid()
    all_sprites.add(asteroid)
    asteroids.add(asteroid)

def create_enemy_ship():
    ship = EnemyShip()
    all_sprites.add(ship)
    enemy_ships.add(ship)


# Функция для отображения текста на экране
def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            player.shoot()

    if random.random() < 0.015:
        create_asteroid()

    if random.random() < 0.005:  # Вероятность появления корабля неприятеля
        create_enemy_ship()

    all_sprites.update()

    for ship in enemy_ships:
        ship.shoot()

    hits = pygame.sprite.groupcollide(bullets, asteroids, True, True)

    enemy_hits = pygame.sprite.groupcollide(bullets, enemy_ships, True, True)

    if pygame.sprite.spritecollideany(player, asteroids) or pygame.sprite.spritecollideany(player,enemy_ships) or pygame.sprite.spritecollideany(player, enemy_bullets):

        game_over = True
    # Конец игры при столкновении


        game_over_timer = pygame.time.get_ticks()  # Запуск таймера

    # Очистка экрана
    screen.fill(BLACK)

    # Отрисовка спрайтов
    all_sprites.draw(screen)

    if game_over:
        draw_text(screen, "GAME OVER", 64, WIDTH // 2, HEIGHT // 2)
        # Проверка времени для завершения игры через 5 секунд
        if pygame.time.get_ticks() - game_over_timer > 3000:
            running = False

    # Обновление экрана
    pygame.display.flip()
    clock.tick(FPS)

# Завершение работы
pygame.quit()
