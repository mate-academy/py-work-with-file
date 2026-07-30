import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_sum, buy_sum = 0, 0

    with open(data_file_name, "r") as f:
        content = csv.reader(f)
        for operation, value in content:
            if operation == "supply":
                supply_sum += int(value)
            if operation == "buy":
                buy_sum += int(value)
    result = supply_sum - buy_sum

    with open(report_file_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows([
            ["supply", supply_sum],
            ["buy", buy_sum],
            ["result", result]
        ])


if __name__ == "__main__":
    create_report("apples.csv", "test.csv")
