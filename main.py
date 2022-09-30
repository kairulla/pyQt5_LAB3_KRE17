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
    array = random_array(4, 5)
    print_array(array)

    i = 0
    max_value = array[1][i]
    max_i = i
    for i, j in enumerate(array[1]):
        # print("i=", i)
        if j > max_value:
            max_value = j
            max_i = i
    print("max_value=", max_value)
    print("max_i=", max_i)

    if (max_value > array[2][0]):
        temp = array[2][0]
        array[2][0] = max_value
        array[1][max_i] = temp

    print_array(array)


if __name__ == '__main__':
    main()
