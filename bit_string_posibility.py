from recursive_count_solution import count_appear_each_short_string
from brute_force_solution import brute_force
from time_util import print_timestamp
import sys


def main():
    long_string_len = int(sys.argv[1])
    short_string_len = int(sys.argv[2])

    def calculate_possibility(result_dict):
        possibility = sum([v/(2**long_string_len)
                           for v in result_dict.values()])/len(result_dict)
        # total_appear = sum(result_dict.values())
        # for (k, v) in result_dict.items():
        #     print(k+":"+str(total_appear/v))
        return possibility

    print_timestamp()
    result_dict = brute_force(long_string_len, short_string_len)
    possibility = calculate_possibility(result_dict)
    print(possibility)

    print_timestamp()
    result_dict = count_appear_each_short_string(
        long_string_len, short_string_len)
    possibility = calculate_possibility(result_dict)
    print(possibility)


if __name__ == '__main__':
    main()
