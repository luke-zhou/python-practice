def generate_combinations(short_list, count):
    result_lists = [short_list]
    result_list = short_list[:]
    for i in range(1, count):
        for j in range(len(result_list)):
            print('to do')

    return result_lists


if __name__ == '__main__':
    short_list = [1, 1, 1, 1]
    result = generate_combinations(short_list, 1)
    print(result)

    short_list = [1, 1, 1, 1]
    result = generate_combinations(short_list, 2)
    print(result)
