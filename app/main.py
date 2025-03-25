import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with (open(data_file_name, "r") as f_data,
          open(report_file_name, "w") as f_report):
        reader = csv.reader(f_data)
        for row in reader:
            if len(row) != 2:
                continue
            operation, amount = row[0], row[1]
            if operation == "supply":
                supply_total += int(amount)
            elif operation == "buy":
                buy_total += int(amount)

        result = supply_total - buy_total
        writer = csv.writer(f_report)
        writer.writerow(["supply", supply_total])
        writer.writerow(["buy", buy_total])
        writer.writerow(["result", result])
