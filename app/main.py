import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as source,
          open(report_file_name, "w") as target):
        source_reader = csv.reader(source, delimiter=",")
        target_writer = csv.writer(target, delimiter=",")
        supply, buy = 0, 0
        for row in source_reader:
            if row[0] == "supply":
                supply += int(row[1])
            if row[0] == "buy":
                buy += int(row[1])
        result = supply - buy
        target_writer.writerow(["supply", supply])
        target_writer.writerow(["buy", buy])
        target_writer.writerow(["result", result])
