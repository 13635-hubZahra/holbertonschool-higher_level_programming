#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys_list = sorted(a_dictionary.keys())
    for key in keys_list:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
