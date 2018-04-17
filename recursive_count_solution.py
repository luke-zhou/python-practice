from bit_string_generator import BitStringGenerator
from time_util import print_timestamp


def count_appear_each_short_string(long_string_len, short_string_len):

    def iterate_position(long_list, short_list, start, count):
        return sum([count_appear(long_list, short_list, i, count) for i in range(start, len(long_list))])

    def count_appear(current_list, short_list, position, short_list_count):

        def is_position_possible(current_list, short_list, position):
            new_list = current_list[:]

            if (position+len(short_list)) > len(current_list):
                return new_list, False

            def is_possible(index):
                return new_list[position+index] == -1 or new_list[position+index] == short_list[index]

            def replace():
                for j in range(len(short_list)):
                    new_list[position+j] = short_list[j]

            find_position = all([is_possible(j)
                                 for j in range(len(short_list))])
            if find_position:
                replace()

            return new_list, find_position

        result_list, possible = is_position_possible(
            current_list, short_list, position)
        if possible:
            short_list_count += 1
            minus_one_count = sum([1 for e in result_list if e == -1])
            possibliity = (-1)**(short_list_count+1) * (2**minus_one_count)
            # print(result_list)
            # print("###"+str(possibliity) + ":" + str(start)+":"+str(start))
            possibliity += iterate_position(result_list,
                                            short_list, position+1, short_list_count)
            return possibliity
        else:
            # print("@@@"+str(start) + ":" + str(short_list_count))
            return 0

    long_list = [-1 for x in range(long_string_len)]
    # print(long_list)
    result_dict = {}
    # short_list = [1, 0, 1, 0, 1, 0]
    for short_list in BitStringGenerator(short_string_len):
        short_string = ''.join(str(x) for x in short_list)
        revert_list = [1 if x == 0 else 0 for x in short_list]
        revert_string = ''.join(str(x) for x in revert_list)
        if revert_string in result_dict:
            result_dict[short_string] = result_dict[revert_string]
        else:
            final_count = iterate_position(long_list, short_list, 0, 0)
            result_dict[short_string] = final_count
        # print_timestamp()
        # print(str(short_list)+":"+str(result_dict[short_string]))

    return result_dict
