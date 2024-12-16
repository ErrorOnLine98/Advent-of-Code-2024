# Solution for day 1 problem part 2
# Adam King 12/12/2024

import numpy as np


def main():
    # Load input text file and convert it to an array
    data = np.loadtxt("input.txt", dtype=int)
    data_list = data.tolist()

    # Extract the first and second columns
    left_list = data[:, 0].tolist()  # First column
    right_list = data[:, 1].tolist()  # Second column

    total_similarity_score = 0

    # Calculate total similarity score
    for i in range(len(left_list)):
        left_num = left_list[i]
        occurrences = right_list.count(left_num)
        similarity_score = left_num * occurrences
        total_similarity_score += similarity_score

    print(f"\nTotal similarity score = {total_similarity_score}")


if __name__ == '__main__':
    main()
