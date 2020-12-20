# from algoritm import measure_time


def bubble_sort(unorted_list):
    swappings_found = True
    while swappings_found:
        swappings_found = False
        for i in range(len(unorted_list) - 1):
            if unorted_list[i] > unorted_list[i + 1]:
                unorted_list[i], unorted_list[i + 1] = unorted_list[i + 1], unorted_list[i]
                swappings_found = True
    return unorted_list



