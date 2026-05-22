import csv


def create_report(data_file_name: str, report_file_name: str) -> any:
    with open(data_file_name) as f:
        data = csv.reader(f)
        print(data)

        supply = 0
        buy = 0

        for row in data:
            if not row:
                continue
            elif row[0] == "supply":
                supply += int(row[1])
            elif row[0] == "buy":
                buy += int(row[1])

        with open(report_file_name,
                  mode="w",
                  encoding="utf-8",
                  newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["supply", supply])
            writer.writerow(["buy", buy])
            writer.writerow(["result", supply - buy])
