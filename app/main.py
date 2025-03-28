import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    count_supply = 0
    count_buy = 0
    with open(data_file_name, "r") as input_file:
        csv_reader = csv.reader(input_file)
        for row in csv_reader:
            if row[0] == "supply":
                count_supply += int(row[1])
            if row[0] == "buy":
                count_buy += int(row[1])
        count_all = count_supply - count_buy

        with open(report_file_name, "w", newline="") as report_file:
            writer = csv.writer(report_file)
            writer.writerow(["supply", count_supply])
            writer.writerow(["buy", count_buy])
            writer.writerow(["result", count_all])
