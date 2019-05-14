
import pygame
import ast
from constants import *
# Define some colors

size = (SIZE_X, SIZE_Y)
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("AAADP - Automato Automatico Autonomo Destruidor de Poeira")
font = pygame.font.Font(None, 24)


def draw_map(DISPLAY, MAP_X, MAP_Y):
	mult = SIZE_X / MAP_X
	for i in range(MAP_X):
		for j in range(MAP_Y):
			pygame.draw.rect(DISPLAY, BLUE, (i * mult, j * mult, mult - 1, mult - 1))


def get_state(DISPLAY, consult):
	for index in range(len(consult) - 1, -1, -1):
		state = consult[index]
		mapa = state[2]
		mult = SIZE_X / int(mapa[0])
		pygame.display.update()
		robo = state[0]
		dock = state[1]
		lixos = state[3]
		lixeiras = state[4]

		draw_map(DISPLAY, mapa[0], mapa[1])
		pygame.draw.rect(DISPLAY, GREEN, (dock[0] * mult, dock[1] * mult, mult - 1, mult - 1))
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
			elevadores = state[5]
			for i in range(len(elevadores)):
				pygame.draw.rect(DISPLAY, GOLD, (elevadores[i][0] * mult, elevadores[i][1] * mult, mult - 1, mult - 1))
		except:
			pass
		pygame.draw.rect(DISPLAY, BLACK, (robo[0] * mult, robo[1] * mult, mult - 1, mult - 1))
		pygame.display.update()
		pygame.time.wait(20)
	pygame.time.wait(5000)


def main():
	pygame.init()
	DISPLAY = pygame.display.set_mode((SIZE_X, SIZE_Y), 0, 32)
	DISPLAY.fill(WHITE)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					f = open("./result.txt", "r")
					result = ast.literal_eval(f.read())
					get_state(DISPLAY, result)


main()
