#!/usr/bin/env python3


class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(
        self,
        name: str,
        height: int,
        day_since_last_watering: int,
        day: int,
        water_in_tank: int,
    ) -> None:
        self.name = name.title()
        self.height = height
        self.d_s_l_w = day_since_last_watering
        self.day = day
        self.water_in_tank = water_in_tank * 100 / 100

    def water(self) -> None:
        if self.d_s_l_w == 0:
            print(f"🌱💦 {self.name} is getting watered 🌱💦\n")
            raise PlantError(
                f"\033[35mCaught PlantError: The {self.name} plant is "
                f"drowning!🌊\033[0m\n"
            )
        else:
            self.d_s_l_w = 0
        if self.water_in_tank < 20:
            print(f"🌱💦 {self.name} is getting watered 🌱💦\n")
            raise WaterError(
                "\033[35mCaught WaterError: Not enough water in the"
                " tank!🏜️\033[0m\n"
            )
        elif self.water_in_tank > 100:
            print(f"🌱💦 {self.name} is getting watered 🌱💦\n")
            raise WaterError(
                "\033[35mCaught WaterError: Too much water in the"
                " tank!🤿\033[0m\n"
            )
        else:
            self.water_in_tank = self.water_in_tank - 20
        print(f"🌱💦 {self.name} is getting watered 🌱💦\n")

    def day_plus_one(self) -> None:
        if self.d_s_l_w >= 3:
            self.day += 1
            self.d_s_l_w += 1
            print(f"☀️  Day {self.day} for {self.name}!\n")
            raise PlantError(
                f"\033[35mCaught PlantError: The {self.name} plant is "
                f"wilting!🥀\033[0m\n"
            )
        self.day += 1
        self.d_s_l_w += 1
        if self.water_in_tank < 20 and self.day > 5:
            self.water_in_tank == 100
        print(f"☀️  Day {self.day} for {self.name}!\n")


def test_first_PlantError():
    print("\033[36m🔍Testing PlantError...🔍\033[0m\n")
    try:
        sunflower = Plant("Sunflower", 160, 1, 0, 80)
        sunflower.day_plus_one()
        sunflower.water()
        sunflower.water()
    except (WaterError, PlantError) as error:
        print(error)


def test_second_PlantError():
    print("\033[36m🔍Testing second PlantError🔍\033[0m\n")
    try:
        sunflower = Plant("Sunflower", 160, 1, 0, 80)
        for i in range(3):
            sunflower.day_plus_one()
    except (WaterError, PlantError) as error:
        print(error)


def test_first_WaterError():
    print("\033[36m🔍Testing WaterError...🔍\033[0m\n")
    try:
        sunflower = Plant("Sunflower", 160, 1, 0, 80)
        for i in range(5):
            sunflower.day_plus_one()
            sunflower.water()
    except (WaterError, PlantError) as error:
        print(error)


def test_second_WaterError():
    print("\033[36m🔍Testing second WaterError🔍\033[0m\n")
    try:
        sunflower = Plant("Sunflower", 160, 1, 0, 120)
        sunflower.water()
    except (WaterError, PlantError) as error:
        print(error)


def test_all():
    sunflower = Plant("Sunflower", 160, 1, 0, 80)
    rose = Plant("Rose", 50, 1, 0, 80)
    tulip = Plant("Tulip", 40, 1, 0, 80)
    iris = Plant("Iris", 45, 1, 0, 120)
    print("\033[36m🔍Testing catching all garden errors...🔍\033[0m\n")
    try:
        sunflower.day_plus_one()
        sunflower.water()
        sunflower.water()
    except GardenError as e:
        print(e)
    try:
        for i in range(3):
            rose.day_plus_one()
    except GardenError as e:
        print(e)
    try:
        for i in range(5):
            tulip.day_plus_one()
            tulip.water()
    except GardenError as e:
        print(e)
    try:
        iris.water()
    except GardenError as e:
        print(e)


if __name__ == "__main__":
    test_all()
