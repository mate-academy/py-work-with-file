import csv


def create_report(data_file_name: str, report_file_name: str) -> None:

    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r") as data_file:
        csv_reader = csv.reader(data_file)
        for line in csv_reader:
            if not line:
                continue
            elif line[0] == "supply":
                total_supply += int(line[1])
            else:
                total_buy += int(line[1])

    with open(report_file_name, "w") as report:
        report.write(f"supply,{total_supply}\n")
        report.write(f"buy,{total_buy}\n")
        report.write(f"result,{total_supply - total_buy}\n")
