def main():
    examples_lines = get_lines("example.txt")
    input_lines = get_lines("input.txt")

    parse_one(examples_lines)
    parse_one(input_lines)

    parse_two(examples_lines)
    parse_two(input_lines)


def parse_one(lines):
    list_a = []
    list_b = []
    for line in lines:
        a, b = line.split()
        list_a.append(int(a))
        list_b.append(int(b))
    list_a.sort()
    list_b.sort()

    total_distance = 0
    for i in range(len(list_a)):
        distance = abs(list_a[i] - list_b[i])
        total_distance += distance
    print(total_distance)


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
