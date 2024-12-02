def main():
    examples_lines = get_lines("example.txt")
    input_lines = get_lines("input.txt")

    parse_one(examples_lines)
    parse_one(input_lines)

    # parse_two(examples_lines)
    # parse_two(input_lines)


def parse_one(lines):
    correct = 0
    for line in lines:
        x = is_safe_one(line)
        y = is_safe_two(line)

        if x and y:
            correct += 1

    print(correct)


def is_safe_one(line):
    line_list = line.split()
    x = all(
        int(line_list[i]) < int(line_list[i + 1]) for i in range(len(line_list) - 1)
    )
    y = all(
        int(line_list[i]) > int(line_list[i + 1]) for i in range(len(line_list) - 1)
    )
    return x or y


def is_safe_two(line):
    line_list = line.split()
    return all(
        abs(int(line_list[i]) - int(line_list[i + 1])) in [1, 2, 3]
        for i in range(len(line_list) - 1)
    )


def parse_two(lines):
    list_a = []
    list_b = []
    for line in lines:
        a, b = line.split()
        list_a.append(int(a))
        list_b.append(int(b))

    total_similarity = 0
    for i in range(len(list_a)):
        similarity = list_a[i] * list_b.count(list_a[i])
        total_similarity += similarity
    print(total_similarity)


def get_lines(filepath):
    with open(filepath) as example_file:
        lines = example_file.readlines()

    lines = [line.strip() for line in lines]

    return lines


if __name__ == "__main__":
    main()
