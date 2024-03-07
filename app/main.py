import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r", newline="") as input_file:
        csv_reader = csv.reader(input_file)

        supply_count = 0
        buy_count = 0

        for row in csv_reader:
            if row[0] == "supply":
                supply_count += int(row[1])
            elif row[0] == "buy":
                buy_count += int(row[1])

        result = supply_count - buy_count

    with open(report_file_name, "w", newline="") as output_file:
        csv_writer = csv.writer(output_file)

        csv_writer.writerow(["supply", str(supply_count)])
        csv_writer.writerow(["buy", str(buy_count)])
        csv_writer.writerow(["result", str(result)])
