import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply: int = 0
    buy: int = 0
    result: int = 0
    with open(data_file_name) as file1:
        csvreader = csv.reader(file1)
        for row in csvreader:
            if row[0] == "supply":
                supply += int(row[1])
            if row[0] == "buy":
                buy += int(row[1])
    result = supply - buy

    report = [("supply", supply), ("buy", buy), ("result", result)]
    file1.close()

    with open(report_file_name, "w", newline="") as file2:
        csv.writer(file2).writerows(report)
