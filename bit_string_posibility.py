from bit_string import BitString


def main():
    long_string_len = 10
    short_string_len = 3
    brute_force(long_string_len, short_string_len)
    # possibility_calculation(long_string_len, short_string_len)

    result = possibility_calculation(long_string_len, short_string_len)
    print(result)


def possibility_calculation(long_string_len, short_string_len):
    long_list = [-1 for x in range(long_string_len)]
    print(long_list)

    short_list = [1, 1, 0]
    # for short_list in BitString(short_string_len):

    final_count = iterate_position(long_list, short_list, 0, 0)
    return final_count


def iterate_position(long_list, short_list, start, count):
    result = 0
    for i in range(start, len(long_list)):
        result += count_appear(long_list, short_list, i, count)
    # print(result)
    return result


def count_appear(current_list, short_list, start, short_list_count):
    result_list, position, find = find_the_possible_position(
        current_list, short_list, start)
    if find:
        short_list_count += 1
        minus_one_count = sum([1 for e in result_list if e == -1])
        possibliity = (-1)**(short_list_count+1) * (2**minus_one_count)
        print(result_list)
        print("###"+str(possibliity) + ":" + str(position)+":"+str(start))
        possibliity += iterate_position(result_list,
                                        short_list, position+1, short_list_count)
        return possibliity
    else:
        print("@@@"+str(start) + ":" + str(short_list_count))
        return 0


def find_the_possible_position(current_list, short_list, start):
    new_list = current_list[:]
    for i in range(start, len(new_list)-len(short_list)+1):
        find_position = True
        for j in range(len(short_list)):
            if new_list[i+j] != -1 and new_list[i+j] != short_list[j]:
                find_position = False
                break
        if find_position:
            for j in range(len(short_list)):
                new_list[i+j] = short_list[j]
            return new_list, i, True
    return new_list, -1, False


def brute_force(long_string_len, short_string_len):
    result_dict = {''.join(str(y)
                           for y in x): 0 for x in BitString(short_string_len)}
    for long_list in BitString(long_string_len):
        long_string = ''.join(str(x) for x in long_list)
        for short_list in BitString(short_string_len):
            short_string = ''.join(str(x) for x in short_list)
            if short_string in long_string:
                result_dict[short_string] = result_dict[short_string]+1

    print(result_dict)
    posibility = sum([v/(2**long_string_len)
                      for v in result_dict.values()])/len(result_dict)
    print(posibility)


def generate_sub_string_set(index):
    if index == 0:
        return [[1], [0]]
    else:
        result = generate_sub_string_set(index-1)
        new_result = [list+[e] for e in [1, 0] for list in result]
        return new_result


if __name__ == '__main__':
    main()
