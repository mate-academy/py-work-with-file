import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(
            data_file_name,
            mode="r",
            newline="",
            encoding="utf-8"
    ) as infile:
        reader = csv.reader(infile)

        for row in reader:
            if row:
                operation_type = row[0].strip()
                amount = int(row[1].strip())
                if operation_type == "supply":
                    supply_total += amount
                elif operation_type == "buy":
                    buy_total += amount

    result = supply_total - buy_total

    with open(
            report_file_name,
            mode="w",
            newline="",
            encoding="utf-8"
    ) as outfile:
        writer = csv.writer(outfile)

        writer.writerow(["supply", supply_total])
        writer.writerow(["buy", buy_total])

        writer.writerow(["result", result])

    print(f"Report successfully created to file: {report_file_name}")
