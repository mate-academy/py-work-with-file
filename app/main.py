import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data:
        rows = csv.reader(data)

        supply = 0
        buy = 0

        for row in rows:
            if not row:
                continue

            if row[0] == "supply":
                supply += int(row[1])

            elif row[0] == "buy":
                buy += int(row[1])

        result = supply - buy

    with open(report_file_name, "w", newline="") as report:
        writer = csv.writer(report)
        writer.writerow(["supply", supply])
        writer.writerow(["buy", buy])
        writer.writerow(["result", result])
