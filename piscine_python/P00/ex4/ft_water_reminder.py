def ft_water_reminder():
    water = input("Days since last watering: ")
    if int(water) > 2:
        print("Water the plants!")
    else:
        print("Plant are fine")
