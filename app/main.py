import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r", newline="") as infile:
        reader = csv.reader(infile)

        for row in reader:
            if row:
                operation, amount = row
                amount = int(amount)

                if operation == "supply":
                    supply_total += amount
                elif operation == "buy":
                    buy_total += amount

    result = supply_total - buy_total

    with open(report_file_name, "w", newline="") as outfile:
        writer = csv.writer(outfile)

        writer.writerow(["supply", supply_total])
        writer.writerow(["buy", buy_total])
        writer.writerow(["result", result])
