import csv


def create_report(data_file_name: str, report_file_name: str) -> csv:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            operation = row[0]
            amount = int(row[1])
            if operation == "supply":
                total_supply += amount
            elif operation == "buy":
                total_buy += amount

    result = total_supply - total_buy

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{total_supply}\n")
        report_file.write(f"buy,{total_buy}\n")
        report_file.write(f"result,{result}\n")
