import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name,
              mode="r",
              newline="",
              encoding="utf-8") as data_file:
        csv_reader = csv.reader(data_file)

        for row in csv_reader:
            if row and len(row) == 2:
                operation_type = row[0].strip()
                try:
                    amount = int(row[1].strip())
                except ValueError:
                    continue

                if operation_type == "supply":
                    supply_total += amount
                elif operation_type == "buy":
                    buy_total += amount

    result_total = supply_total - buy_total

    with open(report_file_name,
              mode="w",
              newline="",
              encoding="utf-8") as report_file:
        csv_writer = csv.writer(report_file)
        csv_writer.writerow(["supply", supply_total])
        csv_writer.writerow(["buy", buy_total])
        csv_writer.writerow(["result", result_total])
