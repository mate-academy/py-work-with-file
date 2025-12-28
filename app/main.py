import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as data_file,\
            open(report_file_name, "w") as report_file:

        for row in csv.reader(data_file):
            # if len(row) == 2:
            if row[0] == "supply":
                supply_total += int(row[1])
            elif row[0] == "buy":
                buy_total += int(row[1])

        csv.writer(report_file).writerow(["supply", supply_total])
        csv.writer(report_file).writerow(["buy", buy_total])
        csv.writer(report_file).writerow(["result", supply_total - buy_total])
