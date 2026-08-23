import csv


def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    opened_file = open(data_file_name, "r")
    reader = csv.reader(opened_file)
    supply_count = 0
    buy_count = 0
    for row in reader:
        operation = row[0]
        amount = int(row[1])
        if operation == "supply":
            supply_count += amount
        else:
            buy_count += amount
    result = supply_count - buy_count
    with open(
            report_file_name,
            "w",
            newline=""
    ) as write_file:
        writer = csv.writer(write_file)
        writer.writerow(["supply", supply_count])
        writer.writerow(["buy", buy_count])
        writer.writerow(["result", result])
