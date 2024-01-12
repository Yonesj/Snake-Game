import pygame
from network import Network


def main():
    pygame.init()
    network = Network('localhost', 5050)
    network.start()


if __name__ == '__main__':
    main()
