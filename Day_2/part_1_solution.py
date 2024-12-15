# Adam King 12/13/2024


def is_safe_report(report):
    # Check if the report is either all increasing or all decreasing
    increasing = True
    decreasing = True

    for i in range(1, len(report)):
        difference = report[i] - report[i - 1]

        # Check the difference condition
        if abs(difference) < 1 or abs(difference) > 3:
            return False

        # Check increasing or decreasing condition
        if difference < 0:
            increasing = False
        if difference > 0:
            decreasing = False

    # A report is safe if it's either strictly increasing or strictly decreasing
    return increasing or decreasing


def main():
    # Initialize an empty list to hold the reports
    report_list = []

    # Read the file line by line
    with open('input.txt', 'r') as file:
        for line in file:
            # Split the line by spaces, convert each value to an integer, and add it to the list
            report = list(map(int, line.split()))
            report_list.append(report)

    # Count the number of safe reports
    safe_count = 0
    for report in report_list:
        if is_safe_report(report):
            safe_count += 1

    print(f"Safe reports: {safe_count}")


if __name__ == '__main__':
    main()
