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

    def get_location_for_seed(self, seed):
        for map_name in self.MAP_ORDER:
            for destination, source, length in self.maps[map_name]:
                if seed in range(source, source + length):
                    seed += destination - source
                    break
        return seed

    def get_lowest_location(self):
        locations = []
        for seed in self.seeds:
            locations.append(self.get_location_for_seed(seed))
        return min(locations)


class AlmanacV2(Almanac):

    def _get_seeds(self, seed_text):
        numbers = [int(seed) for seed in seed_text.split()]
        ranges = []
        for i in range(0, len(numbers), 2):
            start, length = numbers[i:i + 2]
            ranges.append(range(start, start + length))
        return chain(*ranges)
