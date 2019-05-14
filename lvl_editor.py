#
#
#   Created by Olivato :D
#
#

import pygame, sys

from pygame.locals import *
from constants import *
import os

n = 20
m = 20
SIZE = 700


def draw_map(DISPLAY, MAP_X, MAP_Y, lixos, dock, lixeiras, elevadores, robo):
	mult = SIZE / MAP_X
	for i in range(MAP_X):
		for j in range(MAP_Y):
			pygame.draw.rect(DISPLAY, BLUE, (i * mult, j * mult, mult - 1, mult - 1))
	try:
		pygame.draw.rect(DISPLAY, GREEN, (dock[0] * mult, dock[1] * mult, mult - 1, mult - 1))
	except:
		pass
	try:
		for i in range(len(lixos)):
			pygame.draw.rect(DISPLAY, RED, (lixos[i][0] * mult, lixos[i][1] * mult, mult - 1, mult - 1))
	except:
		pass
	try:
		for i in range(len(lixeiras)):
			pygame.draw.rect(DISPLAY, PINK, (lixeiras[i][0] * mult, lixeiras[i][1] * mult, mult - 1, mult - 1))
	except:
		pass
	try:
		for i in range(len(elevadores)):
			pygame.draw.rect(DISPLAY, GOLD, (elevadores[i][0] * mult, elevadores[i][1] * mult, mult - 1, mult - 1))
	except:
		pass
	try:
		pygame.draw.rect(DISPLAY, BLACK, (robo[0] * mult, robo[1] * mult, mult - 1, mult - 1))
	except:
		pass
	pygame.display.update()


def main():
	pygame.init()
	DISPLAY = pygame.display.set_mode((SIZE, SIZE), 0, 32)
	pygame.display.set_caption('Robo Paint Pre-Alpha Tech Demo v0.1')
	DISPLAY.fill(WHITE)
	mapa = [n, m]
	robo = []
	dock = []
	lixos = []
	lixeiras = []
	color = RED
	elevadores = []
	lixo_count = 0
	draw_map(DISPLAY, n, m, lixos, dock, lixeiras, elevadores, robo)
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				query = "'solucao_bp([[" + str(robo[0]) + "," + str(robo[1]) + ",0]," + str(dock) + "," + str(
					[n, m, lixo_count]) + "," + str(lixos) + "," + str(lixeiras) + "," + str(elevadores) + "],Sol)"
				bashCommand = "swipl -s sweeper.pl -g " + query + ",write(Sol),halt' > result.txt"
				print("Executando PROLOG... Aguarde. Pode demorar")
				os.system(bashCommand)

				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_0:
					color = GOLD
				if event.key == pygame.K_1:
					color = RED
				if event.key == pygame.K_2:
					color = PINK
				if event.key == pygame.K_3:
					color = GREEN
				if event.key == pygame.K_4:
					color = BLACK

			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				mouse_rel = [int(pos[0] / (SIZE / n)), int(pos[1] / (SIZE / n))]
				if color == RED:
					lixos.append(mouse_rel)
					lixo_count += 1
				if color == GOLD:
					elevadores.append(mouse_rel)
				if color == PINK:
					lixeiras.append(mouse_rel)
				if color == BLACK:
					robo = mouse_rel
				if color == GREEN:
					dock = mouse_rel

				draw_map(DISPLAY, n, m, lixos, dock, lixeiras, elevadores, robo)

		pygame.display.update()


main()
