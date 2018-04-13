from bit_string import BitString


def main():
    long_string_len = 32
    short_string_len = 5
    result_dict = {''.join(str(y)
                           for y in x): 0 for x in BitString(short_string_len)}
    for long_list in BitString(long_string_len):
        long_string = ''.join(str(x) for x in long_list)
        for short_list in BitString(short_string_len):
            short_string = ''.join(str(x) for x in short_list)
            if short_string in long_string:
                result_dict[short_string] = result_dict[short_string]+1

    # print(result_dict)
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
