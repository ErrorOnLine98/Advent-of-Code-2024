# Solution for day 1 problem part 1
# Adam King 12/12/2024

import numpy as np


def main():
    # Load input text file and convert it to an array
    data = np.loadtxt("input.txt", dtype=int)
    data_list = data.tolist()

    # Sort the 2d array column-wise
    sorted_list = np.sort(data_list, axis=0)

    # Find the distance between each pair in the array and add them up
    total_distance = 0
    for i in range(len(sorted_list)):
        total_distance += np.abs(sorted_list[i][0] - sorted_list[i][1])

    print("Total distance = " + str(total_distance))


if __name__ == '__main__':
    main()
