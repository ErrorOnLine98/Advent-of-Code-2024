# Solution for day 1 problem part 1
# Adam King 12/13/2024

import numpy as np


def main():
    # Initialize an empty list to hold the reports
    report_list = []

    # Read the file line by line
    with open('input.txt', 'r') as file:
        for line in file:
            # Split the line by spaces, convert each value to an integer, and add it to the list
            report = list(map(int, line.split()))
            report_list.append(report)

    print(report_list)
    # TODO: iterate through the report list to determine which ones are safe


if __name__ == '__main__':
    main()