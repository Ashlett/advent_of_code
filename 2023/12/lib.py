import itertools


def part_1(input_text: str) -> int:
    possible_count = 0

    for line in input_text.splitlines():
        springs, counts = line.split(" ")
        counts = [int(n) for n in counts.split(",")]
        total_broken = sum(counts)
        known_broken = springs.count("#")
        unknown_broken = total_broken - known_broken
        unknown_working = springs.count("?") - unknown_broken
        unknown = "#" * unknown_broken + "." * unknown_working

        for permutation in set(itertools.permutations(unknown)):
            new_springs = ""
            permutation = iter(permutation)
            for char in springs:
                if char == "?":
                    new_springs += next(permutation)
                else:
                    new_springs += char
            new_broken = new_springs.replace(".", " ").split()
            new_counts = [len(group) for group in new_broken]
            if new_counts == counts:
                possible_count += 1

    return possible_count


def part_2(input_text: str) -> int:
    return 0
