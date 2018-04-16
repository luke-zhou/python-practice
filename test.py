def main():
    original_list = [0, 1, 2, 3, 4]
    copied_list = original_list[:]
    copied_list[3] = 20
    print(original_list)
    print(copied_list)


def function1():
    current_list = [1, 0, 1, 0, -1, -1, -
                    1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    short_list = [1, 0, 1, 0]
    start = 1
    result_list, position, find = find_the_possible_position(
        current_list, short_list, start)

    print(result_list)
    print(find)
    print(position)


if __name__ == '__main__':
    main()
