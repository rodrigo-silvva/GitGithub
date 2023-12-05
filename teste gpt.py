import pygame
import sys
import math

# Variáveis iniciais
initial_pos1 = 1.0
initial_pos2 = 4.0
initial_velocity1 = 0.1
initial_velocity2 = -0.1
mass1 = 1.0
mass2 = 1.5
num_frames = 100
boxsize = 5.0

# Função para resolver a colisão entre bola e parede
def resolve_wall_collision(pos, vel):
    if pos < 0 or pos > boxsize:
        vel = -vel  # Inverte a velocidade ao atingir a parede
    return vel

# Inicialização do Pygame
pygame.init()

# Configuração da janela
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Colisão de Bolas")

# Loop principal
pos1 = initial_pos1
pos2 = initial_pos2
vel1 = initial_velocity1
vel2 = initial_velocity2

for frame in range(num_frames):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualiza as posições
    pos1 += vel1
    pos2 += vel2

    # Verifica colisão com parede
    vel1 = resolve_wall_collision(pos1, vel1)
    vel2 = resolve_wall_collision(pos2, vel2)

    # Verifica colisão entre as bolas
    if abs(pos1 - pos2) < 1:
        vel1, vel2 = resolve_collision(vel1, vel2, mass1, mass2)

    # Desenha as bolas na tela
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (int(pos1 / boxsize * 500), 250), 10)
    pygame.draw.circle(screen, (0, 0, 255), (int(pos2 / boxsize * 500), 250), 15)
    pygame.display.flip()

    # Define a taxa de atualização
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()