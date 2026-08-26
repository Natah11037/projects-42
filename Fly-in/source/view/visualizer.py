import pygame
import tkinter as tk
from sys import exit


class Visualizer:
    def __init__(self):
        self.screen_width = 0
        self.screen_height = 0
        self.size = None

        self.window = None
        self.background = None
        self.clock = None

    def setup_screen_size(self):
        root = tk.Tk()
        root.withdraw()

        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        self.size = (self.screen_width, self.screen_height)

        root.destroy()

    def setup_window(self):
        pygame.init()

        self.window = pygame.display.set_mode(self.size, pygame.FULLSCREEN)
        pygame.display.set_caption("Natah's Fly-in")

        self.clock = pygame.time.Clock()

    def load_image(self, image: str):
        file = pygame.image.load(image)
        file = file.convert()
        file = pygame.transform.scale(file, self.size)

        return file

    def set_background(self, image: str):
        self.background = self.load_image(image)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

    def draw(self):
        if self.background:
            self.window.blit(self.background, (0, 0))

        pygame.display.update()

    def run(self):
        self.setup_screen_size()
        self.setup_window()

        while True:
            self.handle_events()
            self.set_background("source/view/utilities/1200px-Pelican_Town.png")
            self.draw()

            self.clock.tick(120)
