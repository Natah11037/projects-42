def ft_plant_age():
    plant_age = input("Enter plant age in days: ")
    if int(plant_age) > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
