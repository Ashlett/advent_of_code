def get_lowest_location(almanac):
    map_order = [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
    ]
    seeds, maps = parse_almanac(almanac)
    locations = []
    for seed in seeds:
        for map_name in map_order:
            for destination, source, length in maps[map_name]:
                if seed in range(source, source + length):
                    seed += destination - source
                    break
        locations.append(seed)
    return min(locations)


def parse_almanac(almanac: str):
    almanac = almanac.splitlines(keepends=False)
    in_map = None
    maps = {}
    for line in almanac:
        line = line.strip()
        if line.startswith("seeds:"):
            _, seeds = line.split(":")
            seeds = [int(seed) for seed in seeds.split()]
        elif line.endswith("map:"):
            in_map = line.split()[0]
            maps[in_map] = []
        elif line == "":
            in_map = None
        elif in_map:
            destination, source, length = [int(num) for num in line.split()]
            maps[in_map].append((destination, source, length))
    return seeds, maps
