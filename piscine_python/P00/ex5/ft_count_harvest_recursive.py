def ft_count_harvest_recursive():
    harvest_day = int(input("Days until harvest: "))
    harvest_day_recursive(harvest_day)
    print("Harvest time !")


def harvest_day_recursive(harvest_day):
    if harvest_day > 0:
        harvest_day_recursive(harvest_day - 1)
        print("Day", harvest_day)
