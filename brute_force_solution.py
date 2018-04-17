from bit_string_generator import BitStringGenerator


def brute_force(long_string_len, short_string_len):
    result_dict = {''.join(str(y)
                           for y in x): 0 for x in BitStringGenerator(short_string_len)}
    for long_list in BitStringGenerator(long_string_len):
        long_string = ''.join(str(x) for x in long_list)
        for short_list in BitStringGenerator(short_string_len):
            short_string = ''.join(str(x) for x in short_list)
            if short_string in long_string:
                result_dict[short_string] = result_dict[short_string]+1

    # print(result_dict)
    return result_dict
