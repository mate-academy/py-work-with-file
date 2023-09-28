from csv import reader, writer


def create_report(data_file_name: str, report_file_name: str) -> None:
    operation_totals = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as data_file:
        csv_reader = reader(data_file)

        for row in csv_reader:
            operation_type, amount = row
            amount = int(amount)
            operation_totals[operation_type] += amount

    supply_total = operation_totals["supply"]
    buy_total = operation_totals["buy"]
    result = supply_total - buy_total

    with open(report_file_name, "w", newline="") as report_file:
        csv_writer = writer(report_file)

        csv_writer.writerow(["supply", supply_total])
        csv_writer.writerow(["buy", buy_total])
        csv_writer.writerow(["result", result])
