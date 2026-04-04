import csv


def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    with open(data_file_name, "r", newline="") as f:
        reader = csv.reader(f)
        supply = ["supply", 0]
        buy = ["buy", 0]
        for row in reader:
            if row[0] == "supply":
                supply[1] += int(row[1])
            if row[0] == "buy":
                buy[1] += int(row[1])
        result = ["result", supply[1] - buy[1]]
    with open(report_file_name, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(supply)
        writer.writerow(buy)
        writer.writerow(result)
