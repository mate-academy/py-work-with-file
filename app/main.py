import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        reader = csv.reader(data_file)

        with open(report_file_name, "w", newline="") as report_file:
            writer = csv.writer(report_file)
            supply = 0
            buy = 0

            for operation, amount in reader:
                if operation == "supply":
                    supply += int(amount)
                else:
                    buy += int(amount)

            result = supply - buy
            writer.writerow(["supply", supply])
            writer.writerow(["buy", buy])
            writer.writerow(["result", result])
