import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    file_line = open(data_file_name, "r")
    count_sup = 0
    count_buy = 0
    for lines in file_line:
        line = lines.split(",")
        if line[0] == "supply":
            count_sup += int(line[1])
        elif line[0] == "buy":
            count_buy += int(line[1])
    file_line.close()

    with open(report_file_name, "w", newline="") as report:
        writer = csv.writer(report)
        writer.writerow(["supply", count_sup])
        writer.writerow(["buy", count_buy])
        writer.writerow(["result", count_sup - count_buy])
