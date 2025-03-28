import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    open_file = open(data_file_name, newline="")
    try:
        read_csv = csv.reader(open_file)
        for row in read_csv:
            name, amount = row
            amount = int(amount)
            if name == "supply":
                total_supply += amount
            elif name == "buy":
                total_buy += amount
    finally:
        open_file.close()

    total_result = total_supply - total_buy

    open_file = open(report_file_name, "w", newline="")
    try:
        write_csv = csv.writer(open_file)
        write_csv.writerow(["supply", total_supply])
        write_csv.writerow(["buy", total_buy])
        write_csv.writerow(["result", total_result])
    finally:
        open_file.close()
