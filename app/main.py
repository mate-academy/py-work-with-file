import csv
import os


def create_report(data_file_name: str, report_file_name: str) -> None:
    # корінь проєкту (папка на рівні з app/ і tests/)
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, data_file_name)
    report_path = os.path.join(base_dir, report_file_name)

    supply = 0
    buy = 0

    with open(data_path, "r") as data:
        rows = csv.reader(data)
        for row in rows:
            if not row:
                continue
            operation, amount = row[0], int(row[1])
            if operation == "supply":
                supply += amount
            elif operation == "buy":
                buy += amount

    result = supply - buy

    with open(report_path, "w", newline="") as report:
        writer = csv.writer(report)
        writer.writerow(["supply", supply])
        writer.writerow(["buy", buy])
        writer.writerow(["result", result])
