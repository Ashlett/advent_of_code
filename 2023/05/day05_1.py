
if __name__ == '__main__':

    from day05_lib import get_lowest_location

    with open("input_day5.txt", "r") as f:
        almanac = f.read()

    print(get_lowest_location(almanac))
