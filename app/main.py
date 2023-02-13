import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file, \
            open(report_file_name, "w", newline="") as report_file:

        supply_sum = 0
        buy_sum = 0

        for item in data_file.readlines():
            if item.split(",")[0] == "supply":
                supply_sum += int(item.split(",")[1])
            if item.split(",")[0] == "buy":
                buy_sum += int(item.split(",")[1])
        result = supply_sum - buy_sum

        writer = csv.writer(report_file)
        content = [("supply", supply_sum),
                   ("buy", buy_sum),
                   ("result", result)]
        writer.writerows(content)
