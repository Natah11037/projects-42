import os
from sys import exit
from PIL import Image

from source.controller.graph import Graph
from source.controller.models import SimulationViewState

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
try:
    import pygame
except ImportError:
    print("Pygame is not installed. Please install it to run the visualizer.")
    exit(1)


class Visualizer:
    def __init__(
        self,
        graph: Graph,
        initial_state: SimulationViewState,
        advance_turn,
        path_map: str,
    ):
        self.screen_width = 0
        self.screen_height = 0
        self.size = None
        self.graph = graph
        self.state = initial_state
        self.advance_turn = advance_turn
        self.zone_frames = []
        self.zone_frame = 0
        self.zone_animation_timer = 0
        self.drone_frames = []
        self.drone_frame = 0
        self.drone_animation_timer = 0
        self.sprite_index = 0

        self.path_map = path_map
        self.window = None
        self.background = None
        self.clock = None

    def setup_screen_size(self):
        pygame.init()
        desktop_size = pygame.display.get_desktop_sizes()[0]
        self.screen_width, self.screen_height = desktop_size
        self.size = (self.screen_width, self.screen_height)

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
                if event.key == pygame.K_SPACE:
                    self.state = self.advance_turn()

    def set_sonic_zone_image(self, image: str):
        gif = Image.open(image)

        for frame in range(gif.n_frames):
            gif.seek(frame)

            frame_image = gif.convert("RGBA")

            frame_image = pygame.image.fromstring(
                frame_image.tobytes(), frame_image.size, "RGBA"
            )

            frame_image = pygame.transform.scale(frame_image, (100, 100))

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

    def set_sonic_drone_image(self, image_info: tuple[str, tuple[int, int]]):
        gif = Image.open(image_info[0])
        frames = []

        for frame in range(gif.n_frames):
            gif.seek(frame)

            frame_image = gif.convert("RGBA")

            frame_image = pygame.image.fromstring(
                frame_image.tobytes(), frame_image.size, "RGBA"
            )

            frame_image = pygame.transform.scale(frame_image, image_info[1])

            frames.append(frame_image)

        self.drone_frames.append(frames)

    def get_zone_position(self, zone):
        zones = list(self.graph.zones.values())

        zone_rect = pygame.Rect(
            self.screen_width * 0.05,
            self.screen_height * 0.10,
            self.screen_width * 0.95,
            self.screen_height * 0.65,
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

    def draw_turns(self):
        font = pygame.font.Font(None, 36)
        turns_text = font.render(f"Turns: {self.state.turn}", True, (255, 255, 255))
        self.window.blit(turns_text, (20, 20))

    def draw_connections(self, zone_a, zone_b):
        x1, y1 = self.get_zone_position(zone_a)
        x2, y2 = self.get_zone_position(zone_b)

        pygame.draw.line(
            self.window,
            (0, 255, 0),
            (x1, y1),
            (x2, y2),
            width=10,
        )

    def draw_sonic_drones(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.drone_animation_timer > 50:
            self.drone_frame += 1
            self.drone_animation_timer = current_time

        for drone_index, drone in enumerate(self.state.drones):
            if drone.connection_zone_names:
                zone_a = self.graph.zones[drone.connection_zone_names[0]]
                zone_b = self.graph.zones[drone.connection_zone_names[1]]
                zone_a_position = self.get_zone_position(zone_a)
                zone_b_position = self.get_zone_position(zone_b)
                x = (zone_a_position[0] + zone_b_position[0]) // 2
                y = (zone_a_position[1] + zone_b_position[1]) // 2
            else:
                zone = self.graph.zones[drone.zone_name]
                x, y = self.get_zone_position(zone)

            drone_animation = self.drone_frames[drone_index % len(self.drone_frames)]
            image = drone_animation[self.drone_frame % len(drone_animation)]

            image_rect = image.get_rect(center=(x, y))

            self.window.blit(image, image_rect)

    def draw(self):
        if self.background:
            self.window.blit(self.background, (0, 0))

        for connection in self.graph.connections:
            self.draw_connections(connection.zone1, connection.zone2)
        self.draw_sonic_zones()
        self.draw_sonic_drones()
        self.draw_turns()

        pygame.display.update()

    def run(self):
        self.setup_screen_size()
        self.setup_window()
        self.set_background("source/view/utilities/" "sonic_map.png")
        self.set_sonic_zone_image("source/view/utilities/sonic_ring.gif")
        drone_images = [
            ("source/view/utilities/sonic-drone.gif", (75, 75)),
            ("source/view/utilities/tails-drone.gif", (115, 115)),
            ("source/view/utilities/amy-drone.gif", (115, 115)),
            ("source/view/utilities/knuckle-drone.gif", (70, 70)),
            ("source/view/utilities/cream-drone.gif", (70, 70)),
            ("source/view/utilities/metal-sonic-drone.gif", (80, 80)),
            ("source/view/utilities/shadow-drone.gif", (150, 150)),
        ]
        for drone_image in drone_images:
            self.set_sonic_drone_image(drone_image)

        while True:
            self.handle_events()
            self.draw()

            self.clock.tick(120)
