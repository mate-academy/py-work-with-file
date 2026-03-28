import csv


def create_report(data_file_name: str, report_file_name: str) -> None:

    with open(data_file_name, "r") as data_file:
        total_supply = 0
        total_buy = 0
        csv_reader = csv.reader(data_file)
        for line in csv_reader:
            if line[0] == "supply":
                total_supply += int(line[1])
            if line[0] == "buy":
                total_buy += int(line[1])

    with open(report_file_name, "a") as f:
        f.write(f"supply,{total_supply}\n"
                f"buy,{total_buy}\n"
                f"result,{total_supply - total_buy}\n")
