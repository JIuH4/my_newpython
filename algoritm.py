import time
from matplotlib import pyplot
from timeit import default_timer as timer
import math
import random
from sort import bubble_sort


def measure_time(fn, *args):
    start = timer()
    fn(*args)
    end = timer()
    print(end - start)
    return end - start


string_multiply = lambda n, *args: "s" * n * 25000000
constant_lambda = lambda n, *args: "s" * 25000000

serched_list = list


def linear_search(data, *args):
    searched_item = data[-1]
    for item in data:
        if item == searched_item:
            return item
    return None


def binary_search(data, *args):
    searched_item = data[-1]
    n = len(data)
    left = 0
    right = n - 1

    while left <= right:
        middle = (left + right) // 2
        if searched_item < data[middle]:
            right = middle - 1
        elif searched_item > data[middle]:
            left = middle + 1
        else:
            print(middle)
            return middle


if __name__ == "__main__":
    n_s = range(1, 500)

    # outputs = [measure_time(string_multiply, n) for n in n_s]
    #
    # outputs_const = [measure_time(constant_lambda, n) for n in n_s]
    #
    # linear_output = [measure_time(linear_search, (list(range(n * 250000)))) for n in n_s]
    #
    # bynary_output = [measure_time(binary_search, (list(range(n * 2500000)))) for n in n_s]

    buble_output = [measure_time(bubble_sort, list(range(n * 2, 1, -1))) for n in n_s]

    # pyplot.plot(n_s, outputs)
    # pyplot.plot(n_s, outputs_const)
    # pyplot.plot(n_s, linear_output)
    # pyplot.plot(n_s, bynary_output)
    # print(bynary_output)
    # pyplot.legend(["Linear", "Const", "LinearSearch", "Bynary"])
    pyplot.plot(n_s, buble_output)
    pyplot.show()
