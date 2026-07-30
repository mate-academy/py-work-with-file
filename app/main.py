# write your code here
import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    data_dict = {}

    with open(f"./{data_file_name}", "r") as data_file:
        reader = csv.reader(data_file)

        for row in reader:
            if len(row) >= 2:
                key = row[0]
                value = int(row[1])
            if key in data_dict:
                data_dict[key] += value
            else:
                data_dict[key] = value
    supply = data_dict["supply"]
    buy = data_dict["buy"]
    result = supply - buy

    report_dict = {
        "supply": supply,
        "buy": buy,
        "result": result
    }

    with (
        open(f"./{report_file_name}", mode="w", newline="")
        as report_file
    ):
        writer = csv.writer(report_file)

        for key, value in report_dict.items():
            writer.writerow([key, value])
