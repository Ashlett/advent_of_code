
if __name__ == '__main__':

    from day05_lib import Almanac

    with open("input_day5.txt", "r") as f:
        almanac = f.read()

    print(Almanac(almanac).get_lowest_location())
