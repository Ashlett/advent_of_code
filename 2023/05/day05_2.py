
if __name__ == '__main__':

    from day05_lib import AlmanacV2

    with open("input_day5.txt", "r") as f:
        almanac = f.read()

    print(AlmanacV2(almanac).get_lowest_location())
