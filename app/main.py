import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    supply = 0
    buy = 0

    for line in data_file:
        line_value = line.split(",")
        if line_value[0] == "supply":
            supply += int(line_value[1])
        if line_value[0] == "buy":
            buy += int(line_value[1])
    result = supply - buy
    report_data = [
        ["supply", str(supply)],
        ["buy", str(buy)],
        ["result", str(result)]
    ]
    with open(report_file_name, "w", newline='') as outfile:
        csv_writer = csv.writer(outfile)
        csv_writer.writerows(report_data)
