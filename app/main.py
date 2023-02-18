import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file, open(
        report_file_name, "w", newline=""
    ) as result_file:
        supply = 0
        buy = 0
        for line in data_file.readlines():
            line = line[:-1].split(",")
            if line[0] == "supply":
                supply += int(line[1])
            elif line[0] == "buy":
                buy += int(line[1])
        result_info = [
            ["supply", supply],
            ["buy", buy],
            ["result", supply - buy],
        ]
        writer = csv.writer(result_file)
        writer.writerows(result_info)
