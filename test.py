import datetime
import time

def main():
    original_list = [0, 1, 2, 3, 4]
    copied_list = original_list[:]
    copied_list[3] = 20
    print(original_list)
    print(copied_list)

    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print(st)

    short_list = [1, 0, 1, 0]
    short_string = ''.join(str(x) for x in short_list)
    revert_list =[1 if x==0 else 0 for x in short_list]
    revert_string = ''.join(str(x) for x in revert_list)

    print(short_string)
    print(revert_string)

    test_dict ={"one":1, "two":2, "three":3}
    print("one" in test_dict)
    print("four" in test_dict)


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
