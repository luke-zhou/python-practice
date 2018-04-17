def generate_combinations(short_list, count):

    def get_merged_list(r_list):
        def merge(r_list, short_list, index):
            t_list_copy = r_list[:]
            for i in range(index):
                t_list_copy.pop()
            return t_list_copy + short_list

        def isMatch(r_list, short_list, index):
            t_list_copy = r_list[:]
            match = True
            for i in range(index):
                num = t_list_copy.pop()
                match = match and (short_list[i] == num)
            return match

        result = [merge(r_list, short_list, i)
                  for i in range(len(r_list)) if isMatch(r_list, short_list, i)]
        result.append(short_list if not r_list else r_list+[-1]+short_list)
        return result

    result_list = []
    result_lists = [result_list]

    for i in range(count):
        new_result_lists = []
        for r_list in result_lists:
            new_result_lists.extend(get_merged_list(r_list))
        result_lists = new_result_lists
    return result_lists


if __name__ == '__main__':
    short_list = [1, 0, 1, 1]
    result = generate_combinations(short_list, 1)
    print(result)

    short_list = [1, 0, 1, 1]
    result = generate_combinations(short_list, 2)
    print(result)

    short_list = [1, 1, 1, 1]
    result = generate_combinations(short_list, 2)
    print(result)

    short_list = [1, 0, 1, 1]
    result = generate_combinations(short_list, 3)
    print(result)
