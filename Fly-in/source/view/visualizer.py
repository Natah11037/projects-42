import pygame
import tkinter as tk
from sys import exit
from PIL import Image

from source.controller.graph import Graph
from source.controller.simulation import Simulation


class Visualizer:
    def __init__(self, graph: Graph, simulation: Simulation, path_map: str):
        self.screen_width = 0
        self.screen_height = 0
        self.size = None
        self.graph = graph
        self.simulation = simulation
        self.zone_frames = []
        self.zone_frame = 0
        self.zone_animation_timer = 0
        self.drone_frames = []
        self.drone_frame = 0
        self.drone_animation_timer = 0

        self.path_map = path_map
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
        pygame.display.set_caption("Fly-in-the-Sonicverse")

        self.clock = pygame.time.Clock()

    def load_image(self, image: str):
        file = pygame.image.load(image)
        file = file.convert()
        file = pygame.transform.scale(file, self.size)

        return file

    def set_background(self, image: str):
        self.background = self.load_image(image)

    @staticmethod
    def _resolve_color(color: str) -> tuple[int, int, int, int]:
        try:
            return pygame.Color(color)
        except ValueError:
            return pygame.Color("white")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

    def set_sonic_zone_image(self, image: str):
        gif = Image.open(image)

        for frame in range(gif.n_frames):
            gif.seek(frame)

            frame_image = gif.convert("RGBA")

            frame_image = pygame.image.fromstring(
                frame_image.tobytes(), frame_image.size, "RGBA"
            )

            frame_image = pygame.transform.scale(frame_image, (125, 125))

            self.zone_frames.append(frame_image)

    def draw_sonic_zones(self):
        zones = list(self.graph.zones.values())

        current_time = pygame.time.get_ticks()

        if current_time - self.zone_animation_timer > 100:
            self.zone_frame += 1
            self.zone_frame %= len(self.zone_frames)
            self.zone_animation_timer = current_time

        image = self.zone_frames[self.zone_frame]

        for zone in zones:

            image = self.zone_frames[self.zone_frame].copy()
            image.fill(
                self._resolve_color(zone.color),
                special_flags=pygame.BLEND_RGBA_MULT,
            )

            x, y = self.get_zone_position(zone)

            image_rect = image.get_rect(center=(int(x), int(y)))

            self.window.blit(image, image_rect)

    def set_sonic_drone_image(self, image: str):
        gif = Image.open(image)

        for frame in range(gif.n_frames):
            gif.seek(frame)

            frame_image = gif.convert("RGBA")

            frame_image = pygame.image.fromstring(
                frame_image.tobytes(), frame_image.size, "RGBA"
            )

            frame_image = pygame.transform.scale(frame_image, (150, 150))

            self.drone_frames.append(frame_image)

    def get_zone_position(self, zone):
        zones = list(self.graph.zones.values())

        zone_rect = pygame.Rect(
            self.screen_width * 0.10,
            self.screen_height * 0.25,
            self.screen_width * 0.80,
            self.screen_height * 0.40,
        )

        min_x = min(current_zone.x for current_zone in zones)
        max_x = max(current_zone.x for current_zone in zones)
        min_y = min(current_zone.y for current_zone in zones)
        max_y = max(current_zone.y for current_zone in zones)

        display_rect = zone_rect.inflate(-130, -130)
        x_ratio = 0.5 if max_x == min_x else (zone.x - min_x) / (max_x - min_x)
        y_ratio = 0.5 if max_y == min_y else (zone.y - min_y) / (max_y - min_y)

        x = display_rect.left + display_rect.width * x_ratio
        y = display_rect.top + display_rect.height * y_ratio

        return int(x), int(y)

    def draw_sonic_drones(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.drone_animation_timer > 50:
            self.drone_frame += 1
            self.drone_frame %= len(self.drone_frames)
            self.drone_animation_timer = current_time

        for drone in self.simulation.drones:
            x, y = self.get_zone_position(drone.current_zone)

            image = self.drone_frames[self.drone_frame]

            image_rect = image.get_rect(center=(x, y))

            self.window.blit(image, image_rect)

    def draw(self):
        if self.background:
            self.window.blit(self.background, (0, 0))

        self.draw_sonic_zones()
        self.draw_sonic_drones()

        pygame.display.update()

    def run(self):
        self.setup_screen_size()
        self.setup_window()
        self.set_background("source/view/utilities/" "sonic_map.png")
        self.set_sonic_zone_image("source/view/utilities/sonic_ring.gif")
        self.set_sonic_drone_image("source/view/utilities/sonic_drone.gif")

        while True:
            self.handle_events()
            self.draw()

            self.clock.tick(120)
