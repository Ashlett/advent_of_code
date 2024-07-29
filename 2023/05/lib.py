from itertools import chain


class Almanac:

    MAP_ORDER = [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
    ]

    def __init__(self, almanac_text: str):
        almanac = almanac_text.splitlines(keepends=False)
        in_map = None
        self.maps = {}
        for line in almanac:
            line = line.strip()
            if line.startswith("seeds:"):
                _, seeds = line.split(":")
                self.seeds = self._get_seeds(seeds)
            elif line.endswith("map:"):
                in_map = line.split()[0]
                self.maps[in_map] = []
            elif line == "":
                in_map = None
            elif in_map:
                destination, source, length = [int(num) for num in line.split()]
                self.maps[in_map].append((destination, source, length))

    def _get_seeds(self, seed_text):
        return [int(seed) for seed in seed_text.split()]

    def _get_location_for_seed(self, seed):
        for map_name in self.MAP_ORDER:
            for destination, source, length in self.maps[map_name]:
                if source <= seed < source + length:
                    seed += destination - source
                    break
        return seed
    #
    # def _seeds_for_locations_from_lowest(self):
    #     location = 0
    #     while True:
    #         seed = location
    #         for map_name in reversed(self.MAP_ORDER):
    #             for destination, source, length in self.maps[map_name]:
    #                 if seed in range(destination, destination + length):
    #                     seed += source - destination
    #         yield seed, location
    #         location += 1

    def get_lowest_location(self):
        # for seed, location in self._seeds_for_locations_from_lowest():
        #     if seed in self.seeds:
        #         return location
        min_location = None
        for seed in self.seeds:
            location = self._get_location_for_seed(seed)
            if min_location is None:
                min_location = location
            else:
                min_location = min(location, min_location)
        return min_location


class AlmanacV2(Almanac):

    def _get_seeds(self, seed_text):
        numbers = [int(seed) for seed in seed_text.split()]
        ranges = []
        for i in range(0, len(numbers), 2):
            start, length = numbers[i:i + 2]
            ranges.append(range(start, start + length))
        return chain(*ranges)


def part_1(almanac_text: str):
    return Almanac(almanac_text).get_lowest_location()


def part_2(almanac_text: str):
    return AlmanacV2(almanac_text).get_lowest_location()
