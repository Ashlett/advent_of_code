if __name__ == '__main__':

    from lib import part_1, part_2

    with open("input.txt", "r") as f:
        input_text = f.read()

    print("part 1:", part_1(input_text))
    print("part 2:", part_2(input_text))
