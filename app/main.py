import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0
    with open(data_file_name, "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row[0] == "supply":
                total_supply += int(row[1])
            elif row[0] == "buy":
                total_buy += int(row[1])

    result_value = total_supply - total_buy

    with open(report_file_name, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["supply", total_supply])
        writer.writerow(["buy", total_buy])
        writer.writerow(["result", result_value])
