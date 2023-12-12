import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            if not line:
                continue
            if line[0] == "supply":
                supply += int(line[1])
            if line[1] == "buy":
                buy += int(line[1])
    result = supply - buy
    with open(report_file_name, "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["supply", supply])
        writer.writerow(["buy", buy])
        writer.writerow(["result", result])
