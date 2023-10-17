import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as file:
        for line in file:
            if "supply" in line:
                supply += int(line.split(",")[-1])
            else:
                buy += int(line.split(",")[-1])

    with open(report_file_name, "w", newline="") as report_file:
        writer = csv.writer(report_file)
        writer.writerows([["supply", supply], ["buy", buy],
                          ["result", supply - buy]])
