import csv


def create_report(data_file_name: str, report_file_name: str) -> None:

    sum_supply = 0
    sum_buy = 0

    with open(data_file_name, "r") as current:

        csv_doc = csv.reader(current)

        for file_ in csv_doc:
            if file_[0] == "supply":
                sum_supply += int(file_[1])
            elif file_[0] == "buy":
                sum_buy += int(file_[1])

    # result = [["supply", sum_supply],
    #           ["buy", sum_buy],
    #           ["result", sum_supply - sum_buy]]

    with open(report_file_name, "w", newline="") as report:

        csv_writer = csv.writer(report)
        csv_writer.writerows([
            ["supply", sum_supply],
            ["buy", sum_buy],
            ["result", sum_supply - sum_buy]])
