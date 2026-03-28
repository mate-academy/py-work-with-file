import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file,\
            open(report_file_name, "w", newline="") as result_file:
        supply = 0
        buy = 0
        for i in data_file:
            split_line = i[:-1].split(",")
            if split_line[0] == "supply":
                supply += int(split_line[1])
            elif split_line[0] == "buy":
                buy += int(split_line[1])
        res = supply - buy
        result_info = [
            ["supply", supply],
            ["buy", buy],
            ["result", res]
        ]
        writer = csv.writer(result_file)
        writer.writerows(result_info)
