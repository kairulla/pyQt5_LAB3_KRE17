import random


def random_array(n, m, max_value=20):
    array = []
    for i in range(0, n):
        sub_array = []
        for j in range(m):
            number = random.randint(0, max_value)
            sub_array.append(number)
        array.append(sub_array)
    return array


def print_array(array):
    print()
    for i in array:
        for j in i:
            print("%d\t" % j, end='')
        print()


def main():
    my_array = random_array(4, 5)
    print_array(my_array)
    # b_max = b_min = my_array[1][0]
    # b_max_row = b_min_row = 1
    # b_max_col = b_min_col = 0

    # for row, r in enumerate(my_array):
    #     for col in range(my_array[1][]):
    #         # print(cell, end=' ')
    #         if (col > b_max):
    #             b_max = col
    #             b_max_col = col
    #         if (col < b_min):
    #             b_min = col
    #             b_min_col = col
    # print()

    # print("b_max = " + str(b_max))
    # print("b_max_row = " + str(b_max_row))
    # print("b_max_col = " + str(b_max_col))
    # print("b_min = " + str(b_min))
    # print("b_min_row = " + str(b_min_row))
    # print("b_min_col = " + str(b_min_col))



    # b_max = b_min = my_array[0][0]
    # b_max_row = b_min_row = b_max_col = b_min_col = 0
    #
    # for row, r in enumerate(my_array):
    #     for col, cell in enumerate(r):
    #         # print(cell, end=' ')
    #         if (cell > b_max):
    #             b_max = cell
    #             b_max_col = col
    #             b_max_row = row
    #         if (cell < b_min):
    #             b_min = cell
    #             b_min_col = col
    #             b_min_row = row
    # print()
    #
    # print("b_max = " + str(b_max))
    # print("b_max_row = " + str(b_max_row))
    # print("b_max_col = " + str(b_max_col))
    # print("b_min = " + str(b_min))
    # print("b_min_row = " + str(b_min_row))
    # print("b_min_col = " + str(b_min_col))


if __name__ == '__main__':
    main()
